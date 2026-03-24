# Daily Papers Tool - Agent Guide

This document provides essential information for AI coding agents working on the Daily Papers Tool project.

## Project Overview

**Daily Papers Tool** is an automated Python application that fetches, downloads, summarizes, and manages daily trending AI/ML papers from Hugging Face. It uses LLM-powered summarization (Google Gemini) and stores data in PostgreSQL with MinIO object storage integration.

### Key Features
- Fetches trending papers from Hugging Face API (filtered by upvotes ≥ 10)
- Downloads PDFs from ArXiv
- Generates structured summaries using LangChain + Google Gemini
- Persists data in PostgreSQL database
- Uploads markdown reports to MinIO object storage
- Includes optional Wiki.js sync service

## Technology Stack

| Category | Technology |
|----------|------------|
| **Language** | Python 3.8+ |
| **Web Framework** | FastAPI, Uvicorn |
| **LLM Framework** | LangChain with Google Generative AI |
| **Data Validation** | Pydantic v2 |
| **Database** | PostgreSQL + SQLAlchemy ORM |
| **Object Storage** | MinIO |
| **PDF Processing** | PyPDF, PyMuPDF |
| **Scheduling** | `schedule` library |
| **Environment** | python-dotenv |

## Project Structure

```
daily_papers_tool/
├── daily_papers_tool.py          # Main orchestration script (entry point)
├── scheduler_service.py          # Cron-like scheduler service
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
# Edit .env with your credentials
```

### Run Main Application
```bash
# Run with defaults (today's date, gemini-2.0-flash model)
python daily_papers_tool.py

# Run for specific date
python daily_papers_tool.py --date 2026-01-02

# Run with specific model
python daily_papers_tool.py --model gemini-2.5-flash

# Full example
python daily_papers_tool.py --date 2026-01-02 --model gemini-2.5-pro
```

### Run Scheduler Service

#### Option 1: Native Python
```bash
# Run scheduler (runs daily at 12:00 VN time)
python scheduler_service.py

# Run immediately for testing
python scheduler_service.py --run-now

# Run with specific model
python scheduler_service.py --run-now --model gemini-2.5-flash

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
| `GOOGLE_API_KEY` | Yes | Google Gemini API key |
| `DATABASE_URL` | Yes | PostgreSQL connection string (e.g., `postgresql://user:pass@localhost:5432/db`) |
| `MINIO_ACCESS_KEY` | Yes | MinIO access key |
| `MINIO_SECRET_KEY` | Yes | MinIO secret key |
| `MINIO_ENDPOINT` | No | MinIO endpoint (default: `localhost:9000`) |
| `MINIO_BUCKET` | No | MinIO bucket name (default: `daily-papers`) |
| `MINIO_SECURE` | No | Use HTTPS (default: `false`) |
| `API_PASSWORD` | No | Password for future API endpoints |
| `LLM_MODEL` | No | Default model for scheduler (default: `gemini-2.0-flash`) |
| `RUN_ON_STARTUP` | No | Run job immediately on scheduler startup (default: `false`) |

**Note:** The `.env.copy` file serves as a template with empty values. Never commit `.env` files with real credentials.

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

## Testing Strategy

**Current State:** The project does not have formal unit tests. Testing is done manually:

1. **Manual Testing:** Run with specific dates and verify output
   ```bash
   python daily_papers_tool.py --date 2026-01-02 --model gemini-2.0-flash
   ```

2. **Scheduler Testing:**
   ```bash
   python scheduler_service.py --run-now --date 2026-01-02
   ```

3. **Database Verification:** Check PostgreSQL tables after run

4. **MinIO Verification:** Check uploaded files in MinIO bucket

5. **Logging:** Check `scheduler.log` for scheduler activity

## Security Considerations

1. **API Keys:** Never commit `.env` files or hardcode API keys
2. **Database URLs:** Passwords with special characters (`@`, `:`) are URL-encoded in `database/models.py`
3. **Rate Limiting:** 5-second delays between paper processing to respect ArXiv
4. **File Cleanup:** PDF files are deleted after successful processing
5. **Docker:** Wiki sync service uses environment files, not baked-in credentials

## Workflow Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  Phase 1: Fetch Papers                                       │
│  - Call Hugging Face API                                     │
│  - Filter by upvotes (min 10)                                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Phase 2: Download PDFs                                      │
│  - Download from ArXiv                                       │
│  - Store in papers/YYYY-MM-DD/                               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Phase 3: Database Init & Duplicate Check                    │
│  - Initialize SQLAlchemy engine                              │
│  - Skip papers already in database                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Phase 4: Summarize Papers                                   │
│  - Extract text from PDF (first 10 pages)                    │
│  - Generate structured summary via Gemini                    │
│  - Save to database                                          │
│  - Delete PDF after processing                               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Phase 5: Generate Report                                    │
│  - Create Markdown digest                                    │
│  - Save to summaries/YYYY/MM/                                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Phase 6: Upload to MinIO                                    │
│  - Upload to summaries/YYYY/MM/ path                         │
│  - Save metadata to database                                 │
└─────────────────────────────────────────────────────────────┘
```

## Common Tasks

### Adding a New LLM Model
1. Update model choices in `daily_papers_tool.py` argument parser
2. Update model choices in `scheduler_service.py` argument parser
3. Test with the new model using `--model` flag

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
1. Enable SQLAlchemy echo: Change `echo=False` to `echo=True` in `database/models.py`
2. Check scheduler logs: `tail -f scheduler.log`
3. Test PDF extraction: Run `summary_utils/summarize_papers.py` directly
4. Verify database connection: Check console output for connection errors

## External Dependencies

| Service | Purpose | Endpoint Format |
|---------|---------|-----------------|
| Hugging Face | Fetch daily papers | `https://huggingface.co/api/daily_papers` |
| ArXiv | Download PDFs | `https://arxiv.org/pdf/{id}.pdf` |
| Google Gemini | LLM summarization | Via `langchain-google-genai` |
| PostgreSQL | Data persistence | `postgresql://user:pass@host:port/db` |
| MinIO | Object storage | `http(s)://endpoint:port` |
| Wiki.js | Documentation (optional) | `https://wiki.example.com/graphql` |
