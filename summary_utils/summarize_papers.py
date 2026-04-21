import os
import sys
import pypdf
import json
from typing import List
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate

# Add parent directory to path for importing llm_provider
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from llm_provider import get_llm

# Define Pydantic models for structured output
class PaperSummary(BaseModel):
    """Structured summary of a research paper."""
    tags: List[str] = Field(
        description="List of AI/ML keywords (e.g., RAG, Diffusion, GAN, LLMs, etc.)"
    )
    main_problem: str = Field(
        description="Core problems that this work aims to solve"
    )
    main_idea: str = Field(
        description="Main ideas and approaches that the authors propose"
    )
    main_results: str = Field(
        description="Key findings or performance metrics"
    )
    conclusion_future_works: str = Field(
        description="Final message and future research directions"
    )
    publish_papers: List[str] = Field(
        description="List of exactly 3 research direction ideas"
    )
    patent_ideas: List[str] = Field(
        description="List of exactly 3 patent ideas focused on practical applications, especially for mobile phones"
    )


def summarize_paper(paper_info, text, llm_instance=None):
    """
    Summarizes a paper using LLM based on the extracted text.
    Returns structured JSON data using LangChain with Pydantic model.
    
    Args:
        paper_info: Dictionary with paper metadata (id, title, etc.)
        text: Extracted text from PDF
        llm_instance: Pre-configured LLM instance (if None, creates one via get_llm())
    """
    # Create the prompt template
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful assistant that summarizes research papers accurately and concisely.
You must respond with structured data following the provided schema.

Guidelines:
- All content should be based on the extracted text only
- Use Vietnamese language for all fields except tags and some Technical Name, ex: Vision-Language Action not Thị giác-Ngôn ngữ-Hành động.
- Tags should be common AI/ML keywords (e.g., RAG, Diffusion, GAN, LLMs, etc.)
- Patent ideas should focus on practical applications, especially for mobile phones
- Patent ideas should explain concepts clearly without using technical abbreviations from the paper
- Provide exactly 3 research directions and 3 patent ideas
- The value of each field should be in Markdown format that is used to fill into the template (do not recreate the headings like ### I. Main Problem, ### II. Main Idea,...)"""),
        ("human", """Please summarize the following research paper based on the title and extracted text.

Title: {title}

Extracted text (first few pages):
{text}

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

Please provide a structured summary following the schema.""")
    ])
    
    try:
        # Initialize LLM
        llm = llm_instance if llm_instance is not None else get_llm()
        
        # Create structured output chain with Pydantic model
        structured_llm = llm.with_structured_output(PaperSummary)
        
        # Create the chain
        chain = prompt_template | structured_llm
        
        # Clean text - remove problematic unicode characters
        clean_text = text[:50000].replace('\ud835', '')
        
        # Invoke the chain
        result = chain.invoke({
            "title": paper_info['title'],
            "text": clean_text
        })
        
        # Convert Pydantic model to dict for backward compatibility
        return result.model_dump()
        
    except Exception as e:
        print(f"Error summarizing paper {paper_info['id']}: {e}")
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


def generate_markdown_from_summary(summary_json, _paper_info):
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
