import os
from dotenv import load_dotenv
load_dotenv(override=True)
import sys
import argparse
from datetime import datetime
import time

# Add current directory to path to import local modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from summary_utils import (
    fetch_daily_papers,
    download_all_papers,
    extract_text_from_pdf,
    summarize_paper,
    extract_first_figure,
    upload_to_minio,
    generate_markdown_from_summary
)
from database.db_utils import (
    save_paper_and_summary,
    save_digest_report,
    check_paper_exists,
    get_engine
)

def generate_markdown_report(summaries, date_str, model_name):
    """Generates a comprehensive Markdown report from the paper summaries."""
    report = f"# 🤗 Daily Hugging Face Paper Digest - {date_str}\n\n"
    report += f"Báo cáo được tạo tự động vào lúc {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} bằng mô hình `{model_name}`.\n\n"
    report += "## 📰 Summary of Papers\n\n"
    
    for i, summary_data in enumerate(summaries, 1):
        paper = summary_data['paper']
        summary = summary_data['summary']
        
        report += f"--- \n\n"
        report += f"## {i}. {paper['title']} *({paper['upvotes']} votes)*\n\n"
        report += f"**Tác giả:** {', '.join(paper['authors'])}\n\n"
        report += f"**Xuất bản lúc:** {paper['published_at'][:10] if paper['published_at'] else 'N/A'}\n\n"
        
        # Generate markdown from structured JSON summary
        if summary:
            report += generate_markdown_from_summary({
                'tags': summary.tags,
                'main_problem': summary.main_problem,
                'main_idea': summary.main_idea,
                'main_results': summary.main_results,
                'conclusion_future_works': summary.conclusion_future_works,
                'publish_papers': summary.publish_papers,
                'patent_ideas': summary.patent_ideas
            }, paper)
        else:
            report += "No summary available.\n\n"
        
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
    
    papers = papers[:2]  # Limit to top 10 papers for processing

    # 2. Download all the papers into a date-specific folder
    print(f"Phase 2: Downloading PDFs into papers/{date_str}...")
    download_dir = os.path.join("papers", date_str)
    download_all_papers(papers, download_dir=download_dir)
    
    # Initialize database
    print("Phase 3: Initializing database...")
    get_engine()
    
    # 4. Read and Summarize each paper
    print("Phase 4: Reading and Summarizing papers...")
    summaries = []
    for i, paper in enumerate(papers):
        print(f"Processing paper {i+1}/{len(papers)}: {paper['title']}")
        
        # Check if paper already has a summary in database
        paper_exists, summary_exists = check_paper_exists(paper['id'])
        
        if summary_exists:
            print(f"Paper {paper['id']} already has a summary in database. Skipping...")
            # Still add to summaries for report generation
            from database.db_utils import get_papers_with_summaries
            existing_summaries = get_papers_with_summaries()
            for existing in existing_summaries:
                if existing['paper']['id'] == paper['id']:
                    summaries.append(existing)
                    break
            time.sleep(5)
            continue
        
        if 'local_path' not in paper or not os.path.exists(paper['local_path']):
            print(f"Skipping paper {paper['id']}: PDF not found.")
            continue
            
        text = extract_text_from_pdf(paper['local_path'])
        summary_json = summarize_paper(paper, text, model=model)
        
        if summary_json:
            # Save to database
            save_paper_and_summary(paper, summary_json, model, len(text))
            
            # Get the saved summary for report generation
            from database.db_utils import get_summary_by_paper_id
            summary_db = get_summary_by_paper_id(paper['id'])
            if summary_db:
                summary_entry = {
                    'paper': paper,
                    'summary': summary_db
                }
                summaries.append(summary_entry)
            else:
                print(f"Failed to retrieve saved summary for {paper['id']}")
        else:
            print(f"Failed to generate summary for {paper['id']}")
        
        # Extract overview figure
        # print(f"Extracting overview figure for {paper['id']}...")
        # figure_filename = extract_first_figure(paper['id'], download_dir)
        
        # if figure_filename:
        #     summary_entry['figure_path'] = os.path.join(download_dir, figure_filename)
        #     print(f"Figure extracted: {summary_entry['figure_path']}")
        
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
