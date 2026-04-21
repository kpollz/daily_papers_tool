import os
from dotenv import load_dotenv
load_dotenv(override=True)
import sys
import argparse
from datetime import datetime

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
            if link.startswith('http'):
                report += f"| {platform} | [{link}]({link}) |\n"
            else:
                report += f"| {platform} | {link} |\n"
        report += "\n"
        
    return report

def run_daily_digest(date_str, model="google/gemma-4-31b-it", paper_limit=0):
    """Main function to run the daily paper digest process via LangGraph."""
    print(f"--- Starting Daily Paper Digest for {date_str} using {model} ---")
    
    # Ensure the LLM provider picks up the selected model
    os.environ["LLM_MODEL"] = model
    
    # Lazy import to avoid circular dependencies during module load
    from graph import build_digest_graph
    graph = build_digest_graph()
    
    result = graph.invoke({
        "date_str": date_str,
        "model_name": model,
        "papers": [],
        "papers_to_process": [],
        "summaries": [],
        "failed_papers": [],
        "final_report": "",
        "report_path": "",
        "retry_count": 0,
        "paper_limit": paper_limit,
    })
    
    report_path = result.get("report_path")
    if report_path:
        print(f"--- Digest Complete. Report saved to {report_path} ---")
    else:
        print("--- Digest Complete. No report generated. ---")
    return report_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hugging Face Daily Paper Digest Tool")
    parser.add_argument("--date", type=str, help="Date in YYYY-MM-DD format", default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument("--model", type=str, default="google/gemma-4-31b-it",
                        help="LLM model ID for NVIDIA NIM (default: google/gemma-4-31b-it)")
    parser.add_argument("--limit", type=int, default=0,
                        help="Limit number of papers to process (default: 0 = all)")
    
    args = parser.parse_args()
    run_daily_digest(args.date, model=args.model, paper_limit=args.limit)
