<!-- From: /home/aiteam-linux/gnust/daily_papers_tool/AGENTS.md -->
# Daily Papers Tool - Agent Guide

This document provides essential information for AI coding agents working on the Daily Papers Tool project.

## Project Overview

**Daily Papers Tool** is an automated Python application that fetches, downloads, summarizes, and manages daily trending AI/ML papers from Hugging Face. It uses LLM-powered summarization via **NVIDIA NIM (OpenAI-compatible)** with **LangGraph** orchestration, and stores data in PostgreSQL with MinIO object storage integration.

### Key Features
- Fetches trending papers from Hugging Face API (filtered by upvotes ≥ 10)
- Downloads PDFs from ArXiv
- Generates structured summaries using LangGraph + LangChain + NVIDIA NIM
- Parallel summarization workers with quality gates and retry logic
- Persists data in PostgreSQL database
- Uploads markdown reports to MinIO object storage
- Includes optional Wiki.js sync service

## Technology Stack

| Category | Technology |
|----------|------------|
| **Language** | Python 3.8+ |
| **Web Framework** | FastAPI, Uvicorn |
| **LLM Framework** | LangChain with NVIDIA NIM (OpenAI-compatible) |
| **Graph Orchestration** | LangGraph |
| **Data Validation** | Pydantic v2 |
| **Database** | PostgreSQL + SQLAlchemy ORM |
| **Object Storage** | MinIO |
| **PDF Processing** | PyPDF, PyMuPDF |
| **Scheduling** | `schedule` library |
| **Environment** | python-dotenv |

## Project Structure

```
daily_papers_tool/
├── daily_papers_tool.py          # Main orchestration script (LangGraph entry point)
├── scheduler_service.py          # Cron-like scheduler service
├── llm_provider.py               # LLM factory for NVIDIA NIM
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables (gitignored)
├── .env.copy                     # Environment template
├── .gitignore                    # Git ignore rules
├── README.md                     # User documentation
├── AGENTS.md                     # This file
├── Dockerfile                    # Docker image definition
├── docker-compose.yml            # Docker Compose configuration
├── .dockerignore                 # Docker ignore rules
├── logs/                         # Scheduler logs (gitignored)
│
├── graph/                        # LangGraph workflow package
│   ├── __init__.py
│   ├── state.py                  # DigestState TypedDict schema
│   ├── nodes.py                  # All graph nodes (fetch, download, summarize, etc.)
│   └── builder.py                # Graph wiring & conditional edges
│
├── database/                     # Database layer
│   ├── __init__.py
│   ├── models.py                 # SQLAlchemy ORM models (Paper, PaperSummary, DigestReport)
│   └── db_utils.py               # Database utility functions
│
├── summary_utils/                # Paper processing utilities
│   ├── __init__.py               # Package exports
│   ├── fetch_papers.py           # Hugging Face API client
│   ├── download_papers.py        # ArXiv PDF downloader
│   ├── extract_figure.py         # Figure extraction (experimental)
│   ├── summarize_papers.py       # LLM summarization with Pydantic structured output
│   └── upload_minio.py           # MinIO storage upload
│
├── papers/                       # Temporary PDF storage (gitignored)
│   └── YYYY-MM-DD/              # Date-organized folders
│
├── summaries/                    # Generated markdown reports
│   └── YYYY/MM/                 # Year/month organized structure
│
└── wiki_sync_service/           # OPTIONAL: Wiki.js sync service (separate project)
    ├── wiki_sync_service.py     # Main sync daemon
    ├── sync_to_wiki.py          # Manual sync script
    ├── requirements.txt         # Separate dependencies
    ├── docker-compose.yml       # Docker deployment
    ├── Dockerfile               # Container image
    ├── .env.copy                # Wiki service env template
    ├── README.md                # Wiki service documentation
    └── wiki_utils/              # Wiki utilities
        ├── __init__.py
        ├── download_from_minio.py
        ├── upload_to_wiki.py
        └── wiki_page_operations.py
```

## Build and Run Commands

### Setup Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.copy .env
# Edit .env with your credentials (user-managed, do not read)
```

### Run Main Application
```bash
# Run with defaults (today's date, moonshotai/kimi-k2.5 model)
python daily_papers_tool.py

# Run for specific date
python daily_papers_tool.py --date 2026-01-02

# Run with specific NVIDIA NIM model
python daily_papers_tool.py --model moonshotai/kimi-k2.5

# Full example
python daily_papers_tool.py --date 2026-01-02 --model moonshotai/kimi-k2.5
```

### Run Scheduler Service

#### Option 1: Native Python
```bash
# Run scheduler (runs daily at 12:00 VN time)
python scheduler_service.py

# Run immediately for testing
python scheduler_service.py --run-now

# Run with specific model
python scheduler_service.py --run-now --model moonshotai/kimi-k2.5

# Run specific date (testing only)
python scheduler_service.py --run-now --date 2026-01-02
```

#### Option 2: Docker (Recommended for Production)
```bash
# Build and start the scheduler container
docker-compose up -d

# View logs
docker-compose logs -f daily-papers-scheduler

# View scheduler-specific logs
tail -f logs/scheduler.log

# Stop the service
docker-compose down

# Rebuild after code changes
docker-compose up -d --build
```

**Docker Features:**
- Auto-restart on failure (`restart: unless-stopped`)
- Vietnam timezone (UTC+7) configured
- Logs persisted to `./logs/` directory
- Summaries persisted to `./summaries/` directory
- Health checks every minute

### Run Wiki Sync Service (Optional)
```bash
cd wiki_sync_service
pip install -r requirements.txt
cp .env.copy .env
# Edit .env with credentials

# Run the service
python wiki_sync_service.py

# Or use Docker
docker-compose up -d
```

## Environment Variables

Create a `.env` file in the project root with these variables:

| Variable | Required | Description |
|----------|----------|-------------|
| `NVIDIA_API_KEY` | Yes | NVIDIA NIM API key from build.nvidia.com |
| `NVIDIA_BASE_URL` | No | NVIDIA NIM endpoint (default: `https://integrate.api.nvidia.com/v1`) |
| `DATABASE_URL` | Yes | PostgreSQL connection string (e.g., `postgresql://user:pass@localhost:5432/db`) |
| `MINIO_ACCESS_KEY` | Yes | MinIO access key |
| `MINIO_SECRET_KEY` | Yes | MinIO secret key |
| `MINIO_ENDPOINT` | No | MinIO endpoint (default: `localhost:9000`) |
| `MINIO_BUCKET` | No | MinIO bucket name (default: `daily-papers`) |
| `MINIO_SECURE` | No | Use HTTPS (default: `false`) |
| `API_PASSWORD` | No | Password for future API endpoints |
| `LLM_MODEL` | No | Default model for scheduler (default: `moonshotai/kimi-k2.5`) |
| `MAX_PAPERS_PER_BATCH` | No | Limit concurrent papers to respect 40 RPM (default: `1`) |
| `SUMMARY_MAX_RETRIES` | No | Max retry attempts for failed summaries (default: `2`) |
| `RUN_ON_STARTUP` | No | Run job immediately on scheduler startup (default: `false`) |

**Note:** The `.env.copy` file serves as a template with empty values. Never commit `.env` files with real credentials. The user manages `.env` contents directly — do not read or inspect the `.env` file.

## Code Style Guidelines

### Language
- **Primary:** English for code, comments, and documentation
- **Secondary:** Vietnamese is used for some user-facing output and log messages (particularly in `scheduler_service.py`)

### Import Style
```python
# Standard library first
import os
import sys
from datetime import datetime

# Third-party libraries
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Local imports
from summary_utils import fetch_daily_papers
from database.db_utils import save_paper_and_summary
```

### Code Patterns
- Use `load_dotenv(override=True)` at the top of entry-point scripts
- Add `sys.path.append(os.path.dirname(os.path.abspath(__file__)))` for local imports
- Use Pydantic models for structured LLM output (see `summary_utils/summarize_papers.py`)
- Database sessions should use try/except/finally pattern with proper cleanup
- LangGraph nodes receive `state: DigestState` and return `dict` of state updates
- Use `operator.add` reducer for parallel-accumulated list fields in graph state

### Function Documentation
```python
def function_name(param1, param2):
    """
    Brief description of what the function does.
    
    Args:
        param1: Description
        param2: Description
        
    Returns:
        Description of return value
    """
    pass
```

## Database Schema

### Papers Table
- `id` (String, PK): ArXiv ID
- `title` (String): Paper title
- `authors` (JSON): List of author names
- `published_at` (DateTime): Publication date
- `hf_url`, `arxiv_url`, `pdf_url`, `github_url` (String): URLs
- `upvotes` (Integer): Hugging Face upvotes
- `created_at` (DateTime): Record creation time

### PaperSummaries Table
- `id` (Integer, PK, Auto-increment)
- `paper_id` (String, FK): Reference to papers.id
- `tags` (JSON): AI/ML keywords
- `main_problem`, `main_idea`, `main_results`, `conclusion_future_works` (Text): Summary sections
- `publish_papers`, `patent_ideas` (JSON): Brainstorming ideas
- `model_used` (String): LLM model name
- `processed_at` (DateTime)
- `extracted_text_length` (Integer)

### DigestReports Table
- `id` (Integer, PK, Auto-increment)
- `date_str` (String): Date in YYYY-MM-DD format
- `report_path` (String): Local file path
- `minio_object_name` (String): MinIO object path
- `paper_count` (Integer)
- `model_used` (String)
- `created_at` (DateTime)

## LangGraph Workflow Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Entry Point: daily_papers_tool.py                                       │
│  - Builds graph via build_digest_graph()                                 │
│  - Invokes with {"date_str": ..., "model_name": ...}                     │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Phase 1: Fetch Papers (fetch_papers_node)                               │
│  - Call Hugging Face API                                                 │
│  - Filter by upvotes (min 10)                                            │
│  - Conditional: if empty → skip to generate_report                       │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Phase 2: Download PDFs (download_pdfs_node)                             │
│  - Download from ArXiv                                                   │
│  - Filter to only successfully downloaded papers                         │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Phase 3: Filter Duplicates (filter_duplicates_node)                     │
│  - Skip papers already summarized in DB                                  │
│  - If all duplicates: load existing summaries, skip to generate_report   │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Phase 4: Extract Text (extract_text_node)                               │
│  - Extract text from PDF (first 10 pages)                                │
│  - Skip papers with empty text extraction                                │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Phase 5: Parallel Summarization (dispatch → summarize_worker_node)      │
│  - Map: dispatch_summarization sends one worker per paper via Send       │
│  - Each worker: get LLM → summarize_paper() → return summary             │
│  - 1-second stagger between workers for rate limiting                    │
│  - Exponential backoff retry on 429/500 errors (max 3 attempts)          │
│  - Reduce: operator.add accumulates into state["summaries"]              │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Phase 6: Quality Gate (quality_gate_node)                               │
│  - Validate summary has all required fields                              │
│  - Validate main_problem ≥ 20 chars, tags non-empty                      │
│  - Failed papers moved to state["failed_papers"]                         │
│  - Conditional: if failed_papers > 0 and retries < max → retry loop      │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Phase 7: Retry Failed (retry_failed_node)                               │
│  - Re-run summarization with higher temperature (0.9)                    │
│  - Loop back to quality_gate                                             │
│  - Increment retry_count                                                 │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Phase 8: Save to DB (save_to_db_node)                                   │
│  - Call save_paper_and_summary() for each valid summary                  │
│  - Continue on individual failures (don't crash)                         │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Phase 9: Generate Report (generate_report_node)                         │
│  - Build Markdown digest from summaries                                  │
│  - Include existing DB summaries if no new papers processed              │
│  - Save to summaries/YYYY/MM/daily_digest_YYYY-MM-DD.md                  │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Phase 10: Upload to MinIO (upload_minio_node)                           │
│  - Upload to summaries/YYYY/MM/ path                                     │
│  - Log warning on failure (don't crash workflow)                         │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Phase 11: Cleanup (cleanup_node)                                        │
│  - Delete temporary PDF files                                            │
│  - Remove empty parent directories                                       │
│  - END                                                                   │
└─────────────────────────────────────────────────────────────────────────┘
```

## Testing Strategy

**Current State:** The project does not have formal unit tests. Testing is done manually:

1. **Manual Testing:** Run with specific dates and verify output
   ```bash
   python daily_papers_tool.py --date 2026-01-02 --model moonshotai/kimi-k2.5
   ```

2. **Scheduler Testing:**
   ```bash
   python scheduler_service.py --run-now --date 2026-01-02
   ```

3. **Graph Compilation Test:**
   ```bash
   python -c "from graph import build_digest_graph; g = build_digest_graph(); print(type(g))"
   ```

4. **LLM Provider Test:**
   ```bash
   python -c "from llm_provider import get_llm; llm = get_llm(); print(type(llm))"
   ```

5. **Database Verification:** Check PostgreSQL tables after run

6. **MinIO Verification:** Check uploaded files in MinIO bucket

7. **Logging:** Check `scheduler.log` for scheduler activity

## Security Considerations

1. **API Keys:** Never commit `.env` files or hardcode API keys
2. **Database URLs:** Passwords with special characters (`@`, `:`) are URL-encoded in `database/models.py`
3. **Rate Limiting:** 1-second stagger between parallel workers; 5-paper batch limit for NVIDIA NIM 40 RPM
4. **File Cleanup:** PDF files are deleted after successful processing
5. **Docker:** Wiki sync service uses environment files, not baked-in credentials

## Common Tasks

### Adding a New LLM Model
1. Update `llm_provider.py` to support the new model ID if needed
2. Update `daily_papers_tool.py` help text for `--model`
3. Update `scheduler_service.py` help text for `--model`
4. Test with the new model using `--model` flag
5. Update `README.md` and `AGENTS.md` model references

### Modifying Database Schema
1. Update `database/models.py` with new columns/models
2. SQLAlchemy will auto-create tables on next run (development only)
3. For production, create migration scripts manually

### Adding New Summary Fields
1. Update `PaperSummary` Pydantic model in `summary_utils/summarize_papers.py`
2. Update `PaperSummary` SQLAlchemy model in `database/models.py`
3. Update prompt template in `summarize_papers.py`
4. Update `generate_markdown_from_summary()` function
5. Update `save_paper_and_summary()` in `database/db_utils.py`

### Debugging Tips
1. **Enable SQLAlchemy echo:** Change `echo=False` to `echo=True` in `database/models.py`
2. **Check scheduler logs:** `tail -f logs/scheduler.log`
3. **Test PDF extraction:** Run `summary_utils/summarize_papers.py` directly
4. **Verify database connection:** Check console output for connection errors
5. **NVIDIA API issues:** Verify `NVIDIA_API_KEY` is set, check 429 rate limit errors in logs
6. **Graph visualization:** Use `graph.get_graph().draw_mermaid()` to inspect workflow

## External Dependencies

| Service | Purpose | Endpoint Format |
|---------|---------|-----------------|
| Hugging Face | Fetch daily papers | `https://huggingface.co/api/daily_papers` |
| ArXiv | Download PDFs | `https://arxiv.org/pdf/{id}.pdf` |
| NVIDIA NIM | LLM summarization | `https://integrate.api.nvidia.com/v1` |
| PostgreSQL | Data persistence | `postgresql://user:pass@host:port/db` |
| MinIO | Object storage | `http(s)://endpoint:port` |
| Wiki.js | Documentation (optional) | `https://wiki.example.com/graphql` |
