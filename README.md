# Hugging Face Daily Paper Digest Tool

This tool automates the process of fetching, downloading, and summarizing daily trending papers from Hugging Face.

## Features
- **Automated Fetching**: Retrieves the daily paper list directly from the Hugging Face API.
- **PDF Downloader**: Automatically downloads paper PDFs from ArXiv.
- **AI Summarization**: Uses LLM to read and summarize each paper into a structured format.
- **Markdown Reporting**: Generates a comprehensive report with summaries and links.

## Components
- `fetch_papers.py`: Fetches the paper list.
- `download_papers.py`: Downloads PDFs.
- `summarize_papers.py`: Extracts text and generates summaries.
- `daily_papers_tool.py`: Orchestrates the entire pipeline.

## Usage
To generate a report for a specific date (e.g., 2026-01-02):
```bash
python3 daily_papers_tool.py
```

## Output
The tool generates a Markdown file named `daily_digest_YYYY-MM-DD.md` containing the structured summaries of all papers for that day.
