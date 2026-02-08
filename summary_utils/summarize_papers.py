import os
from openai import OpenAI
import pypdf
import json

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def summarize_paper(paper_info, text, model="gpt-4.1-mini"):
    """
    Summarizes a paper using LLM based on the extracted text.
    Returns structured JSON data instead of free text.
    """
    prompt = f"""
    You are a research assistant. Please summarize the following research paper based on the title and extracted text.
    
    Title: {paper_info['title']}
    
    Extracted text (first few pages):
    {text[:50000]}

    My template for the summary is as follows:
    ```markdown
    **Tag:**

    ### I. Main Problem:

    ### II. Main Idea:

    ### III. Main Results:

    ### IV. Conclusion & Future Works:

    ### V. Brainstorming Space:

    #### 1. Publish Papers:

    #### 2. Patent:
    ```
    
    Please provide a summary in the following JSON format:
    {{
        "tags": ["tag1", "tag2", "tag3"],
        "main_problem": "Core problems that this work aims to solve",
        "main_idea": "Main ideas and approaches that the authors propose",
        "main_results": "Key findings or performance metrics",
        "conclusion_future_works": "Final message and future research directions",
        "publish_papers": [
            "Research direction idea 1",
            "Research direction idea 2", 
            "Research direction idea 3"
        ],
        "patent_ideas": [
            "Patent idea 1 focused on real-world phone applications",
            "Patent idea 2 focused on real-world phone applications",
            "Patent idea 3 focused on real-world phone applications"
        ]
    }}
    
    Notes:
    - All content should be based on the extracted text only
    - Use Vietnamese language for all fields except tags and some Technical Name, ex: Vision-Language Action not Thị giác-Ngôn ngữ-Hành động.
    - Tags should be common AI/ML keywords (e.g., RAG, Diffusion, GAN, LLMs, etc.)
    - Patent ideas should focus on practical applications, especially for mobile phones
    - Patent ideas should explain concepts clearly without using technical abbreviations from the paper
    - Provide exactly 3 research directions and 3 patent ideas
    - The value of each field should be in Markdown format for better readability 
    """
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes research papers accurately and concisely. Always respond with valid JSON format."},
                {"role": "user", "content": prompt.replace('\ud835', '')}
            ],
            response_format={"type": "json_object"}  # Force JSON output
        )
        
        # Parse the JSON response
        summary_json = json.loads(response.choices[0].message.content)
        return summary_json
        
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response for paper {paper_info['id']}: {e}")
        print(f"Raw response: {response.choices[0].message.content}")
        return None
    except Exception as e:
        print(f"Error summarizing paper {paper_info['id']} with {model}: {e}")
        return None

def extract_text_from_pdf(pdf_path, max_pages=10):
    """Extracts text from a PDF file."""
    text = ""
    try:
        with open(pdf_path, 'rb') as f:
            reader = pypdf.PdfReader(f)
            num_pages = min(len(reader.pages), max_pages)
            for i in range(num_pages):
                text += reader.pages[i].extract_text() + "\n"
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
    return text

def generate_markdown_from_summary(summary_json, paper_info):
    """
    Generates markdown content from structured JSON summary.
    This is used for backward compatibility with the report generation.
    """
    if not summary_json:
        return "Summary generation failed."
    
    markdown = f"""
**Tag:** {', '.join(summary_json.get('tags', []))}

### I. Main Problem:
{summary_json.get('main_problem', 'N/A')}

### II. Main Idea:
{summary_json.get('main_idea', 'N/A')}

### III. Main Results:
{summary_json.get('main_results', 'N/A')}

### IV. Conclusion & Future Works:
{summary_json.get('conclusion_future_works', 'N/A')}

### V. Brainstorming Space:

#### 1. Publish Papers:
"""
    
    for i, idea in enumerate(summary_json.get('publish_papers', []), 1):
        markdown += f"{i}. {idea}\n"
    
    markdown += "\n#### 2. Patent:\n"
    for i, idea in enumerate(summary_json.get('patent_ideas', []), 1):
        markdown += f"{i}. {idea}\n"
    
    return markdown

if __name__ == "__main__":
    # Test with one of the downloaded papers
    sample_paper = {
        'id': '2512.23959',
        'title': 'Improving Multi-step RAG with Hypergraph-based Memory for Long-Context Complex Relational Modeling',
        'hf_url': 'https://huggingface.co/papers/2512.23959',
        'arxiv_url': 'https://arxiv.org/abs/2512.23959'
    }
    pdf_path = "papers/2512.23959.pdf"
    if os.path.exists(pdf_path):
        print(f"Extracting text from {pdf_path}...")
        text = extract_text_from_pdf(pdf_path)
        print("Summarizing...")
        summary_json = summarize_paper(sample_paper, text)
        print("\n--- Summary (JSON) ---\n")
        print(json.dumps(summary_json, indent=2, ensure_ascii=False))
        
        print("\n--- Summary (Markdown) ---\n")
        markdown = generate_markdown_from_summary(summary_json, sample_paper)
        print(markdown)