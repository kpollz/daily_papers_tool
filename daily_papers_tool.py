import os
from dotenv import load_dotenv
load_dotenv(override=False)
import sys
import argparse
from datetime import datetime

# Add current directory to path to import local modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def _make_initial_state(date_str: str, model: str, paper_limit: int = 0, force_update: bool = False) -> dict:
    """Build the initial DigestState dict with safe defaults."""
    return {
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
        "force_update": force_update,
    }


def run_daily_digest(date_str, model="moonshotai/kimi-k2.5", paper_limit=0, force_update=False):
    """Main function to run the daily paper digest process via LangGraph."""
    print(f"--- Starting Daily Paper Digest for {date_str} using {model} ---")
    
    # Ensure the LLM provider picks up the selected model
    os.environ["LLM_MODEL"] = model
    
    # Lazy import to avoid circular dependencies during module load
    from graph import build_digest_graph
    graph = build_digest_graph()
    
    result = graph.invoke(_make_initial_state(date_str, model, paper_limit, force_update))
    
    report_path = result.get("report_path")
    if not result.get("papers"):
        print(f"--- Skipping {date_str}: No papers found. ---")
        return None
    elif report_path:
        print(f"--- Digest Complete. Report saved to {report_path} ---")
    else:
        print("--- Digest Complete. No report generated. ---")
    return report_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hugging Face Daily Paper Digest Tool")
    parser.add_argument("--date", type=str, help="Date in YYYY-MM-DD format", default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument("--model", type=str, default=None,
                        help="LLM model ID for NVIDIA NIM (default: from .env)")
    parser.add_argument("--limit", type=int, default=0,
                        help="Limit number of papers to process (default: 0 = all)")
    parser.add_argument("--force", action="store_true",
                        help="Force re-summarize all papers and overwrite existing DB entries")
    
    args = parser.parse_args()
    model = args.model or os.getenv('LLM_MODEL', 'moonshotai/kimi-k2.5')
    run_daily_digest(args.date, model=model, paper_limit=args.limit, force_update=args.force)
