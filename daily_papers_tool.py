import os
from dotenv import load_dotenv
load_dotenv()
import sys
import argparse
from datetime import datetime
import time

# Add current directory to path to import local modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fetch_papers import fetch_daily_papers
from download_papers import download_all_papers
from summarize_papers import extract_text_from_pdf, summarize_paper
from extract_figure import extract_first_figure
from upload_minio import upload_to_minio

def generate_markdown_report(summaries, date_str, model_name):
    """Generates a comprehensive Markdown report from the paper summaries."""
    report = f"# 🤗 Daily Hugging Face Paper Digest - {date_str}\n\n"
    report += f"Báo cáo được tạo tự động vào lúc {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} bằng mô hình `{model_name}`.\n\n"
    report += "## 📰 Summary of Papers\n\n"
    
    for i, summary_data in enumerate(summaries, 1):
        paper = summary_data['paper']
        summary = summary_data['summary']
        
        report += f"--- \n\n"
        report += f"## {i}. {paper['title']}\n\n"
        report += f"**Tác giả:** {', '.join(paper['authors'])}\n\n"
        report += f"**Xuất bản lúc:** {paper['published_at'][:10]}\n\n"
        
        report += summary.strip() + "\n\n"
        
        # Add the overview figure if available
        if 'figure_path' in summary_data:
            report += "### Overview Figure\n\n"
            report += f"![Overview Figure]({summary_data['figure_path']})\n\n"
        
        links = [
            ("Hugging Face", paper.get('hf_url', 'N/A')),
            ("ArXiv Abstract", paper.get('arxiv_url', 'N/A')),
            ("PDF Download", paper.get('pdf_url', 'N/A')),
            ("Github Repository", paper.get('github_url'))
        ]

        report += "### Các đường dẫn liên quan\n\n"
        report += "| Nền tảng | Đường dẫn |\n"
        report += "| :--- | :--- |\n"
        for platform, link in links:
            # if platform == "GitHub" and "Github:" in link:
            #     link = link.replace("Github:", "").strip()
            
            if link.startswith('http'):
                report += f"| {platform} | [{link}]({link}) |\n"
            else:
                report += f"| {platform} | {link} |\n"
        report += "\n"
        
    return report

def run_daily_digest(date_str, model="gpt-4.1-mini"):
    """Main function to run the daily paper digest process."""
    print(f"--- Starting Daily Paper Digest for {date_str} using {model} ---")
    
    # 1. Get the paper list
    print("Phase 1: Fetching paper list...")
    papers = fetch_daily_papers(date_str)
    if not papers:
        print("No papers found or error in fetching. Exiting.")
        return
    print(f"Found {len(papers)} papers.")
    
    # 2. Download all the papers into a date-specific folder
    print(f"Phase 2: Downloading PDFs into papers/{date_str}...")
    download_dir = os.path.join("papers", date_str)
    download_all_papers(papers, download_dir=download_dir)
    
    # 3 & 4. Read and Summarize each paper
    print("Phase 3 & 4: Reading and Summarizing papers...")
    summaries = []
    for i, paper in enumerate(papers):
        print(f"Processing paper {i+1}/{len(papers)}: {paper['title']}")
        
        if 'local_path' not in paper or not os.path.exists(paper['local_path']):
            print(f"Skipping paper {paper['id']}: PDF not found.")
            continue
            
        text = extract_text_from_pdf(paper['local_path'])
        summary_text = summarize_paper(paper, text, model=model)
        
        # Extract overview figure
        # print(f"Extracting overview figure for {paper['id']}...")
        # figure_filename = extract_first_figure(paper['id'], download_dir)
        summary_entry = {
            'paper': paper,
            'summary': summary_text
        }
        
        # if figure_filename:
        #     summary_entry['figure_path'] = os.path.join(download_dir, figure_filename)
        #     print(f"Figure extracted: {summary_entry['figure_path']}")
        
        summaries.append(summary_entry)
        
        # Delete the PDF file after processing
        # try:
        #     os.remove(paper['local_path'])
        #     print(f"Deleted temporary file: {paper['local_path']}")
        # except Exception as e:
        #     print(f"Error deleting file {paper['local_path']}: {e}")
        # Be polite to ArXiv
        time.sleep(5)
        
    # 5. Make a comprehension Markdown Report
    print("Phase 5: Generating Markdown Report...")
    markdown_report = generate_markdown_report(summaries, date_str, model)
    
    if not os.path.exists("summaries"):
        os.makedirs("summaries", exist_ok=True)
    report_filename = f"summaries/daily_digest_{date_str}.md"
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write(markdown_report)
        
    print(f"--- Digest Complete. Report saved to {report_filename} ---")
    
    # 6. Upload to MinIO
    print("Phase 6: Uploading to MinIO...")
    minio_object_name = f"summaries/daily_digest_{date_str}.md"
    upload_to_minio(report_filename, minio_object_name)
        
    return report_filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hugging Face Daily Paper Digest Tool")
    parser.add_argument("--date", type=str, help="Date in YYYY-MM-DD format", default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument("--model", type=str, choices=["gpt-4.1-mini", "gemini-2.5-flash"], default="gpt-4.1-mini", 
                        help="LLM model to use for summarization")
    
    args = parser.parse_args()
    run_daily_digest(args.date, model=args.model)
