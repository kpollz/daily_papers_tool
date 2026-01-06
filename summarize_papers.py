import os
from openai import OpenAI
import pypdf

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def summarize_paper(paper_info, text, model="gpt-4.1-mini"):
    """Summarizes a paper using LLM based on the extracted text."""
    # Note: In this environment, gemini-2.5-flash is available via the OpenAI client
    # with the default configuration.
    
    prompt = f"""
    Bạn là một research assistant. Hãy tóm tắt bài nghiên cứu sau đây dựa trên tiêu đề và đoạn văn trích dẫn..
    
    Tiêu đề: {paper_info['title']}
    
    Văn bản được trích xuất (Một vài trang đầu):
    {text[:15000]}  # Limit text to avoid token limits
    
    Vui lòng cung cấp bản tóm tắt theo CHÍNH XÁC định dạng sau:
    ### Main Problem: (Vấn đề cốt lõi mà bài báo đề cập là gì?)
    ### Main Idea: (Giải pháp hoặc phương pháp đề xuất là gì?)
    ### Main Results: (Những phát hiện chính hoặc các chỉ số hiệu suất là gì?)
    ### Conclusion & Future Works: (Thông điệp cuối cùng và hướng nghiên cứu tiếp theo là gì?)

    Lưu ý: 
    - Tất cả nội dung chỉ dựa trên văn bản được trích xuất.
    - Không sử dụng ký tự đặc biệt, chỉ sử dụng thuần LaTex-style cho Markdown.
    - Câu trả lời có ngôn ngữ là Tiếng Việt (trừ tên đề mục).
    """
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Bạn là một trợ lý đắc lực, tóm tắt các bài nghiên cứu một cách chính xác và ngắn gọn."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error summarizing paper {paper_info['id']} with {model}: {e}")
        return "Summary generation failed."

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

# Original summarize_paper removed, replaced by the one above with model parameter

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
        summary = summarize_paper(sample_paper, text)
        print("\n--- Summary ---\n")
        print(summary)
