# Daily Papers Tool

An automated tool that fetches, downloads, summarizes, and manages daily trending papers from Hugging Face with database persistence and MinIO object storage integration.

## 🌟 Features

- **Automated Paper Fetching**: Retrieves daily trending papers from Hugging Face API with configurable upvote thresholds
- **Intelligent Database Storage**: PostgreSQL database for persistent storage of papers, summaries, and digest reports
- **PDF Processing**: Downloads and extracts text from ArXiv papers
- **AI-Powered Summarization**: Uses LLMs (OpenAI GPT-4 or Google Gemini) to generate structured summaries
- **MinIO Integration**: Uploads generated markdown reports to MinIO object storage
- **Duplicate Prevention**: Skips papers that have already been summarized
- **Organized Storage**: Reports organized by year/month structure

## 📋 Table of Contents

- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Wiki Sync Service (Optional Add-on)](#wiki-sync-service-optional-add-on)
- [Troubleshooting](#troubleshooting)

## 🏗️ Architecture

```mermaid
 graph TD
    
    subgraph "External Services/Tools"
        A[Hugging Face API]
        B[PyMuPDF Python SDK]
        C[PostgreSQL Database]
        D[MinIO Object Storage]
        E[LLM API<br/>OpenAI/Gemini]
    end

    subgraph "Daily Papers Digest Tool"
        B1[Fetch Papers] --> B2[Download PDFs]
        B2 --> B3[Extract Text]
        B3 --> B4[LLM Summarization]
        B4 --> B5[Generate Markdown Report]
        B5 --> B6[Upload to MinIO]
        B6 --> B7[Save to PostgreSQL]
    end

    
    A --> B1
    A --> B2
    B --> B3
    E --> B4
    D --> B6
    C --> B7
```

**Note**: The `wiki_sync_service` is a separate, optional add-on project that can be used to automatically sync content from MinIO to Wiki.js. It operates independently from the main application as shown below:

```mermaid
graph LR
    A[MinIO Storage] -->|Pull Summaries| B[Wiki Sync Service]
    B -->|Push Content| C[Wiki.js]
```

## 📦 Prerequisites

- Python 3.8 or higher
- PostgreSQL 12 or higher
- MinIO server (for object storage)
- OpenAI API key or Google Gemini API key

**Optional (for Wiki Sync Service)**:
- Wiki.js instance
- Additional Python dependencies (see wiki_sync_service/requirements.txt)

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/kpollz/daily_papers_tool.git
cd daily_papers_tool
```

### 2. Set Up Python Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL Database

```bash
# Create database
createdb daily_papers_db

# Or use psql
psql -U postgres
CREATE DATABASE daily_papers_db;
\q
```

### 5. Configure Environment Variables

Copy the example environment file and fill in your credentials:

```bash
cp .env.copy .env
```

Edit `.env` with your actual values (see [Configuration](#configuration) section).

## ⚙️ Configuration

Create a `.env` file in the project root with the following variables:

```env
OPENAI_API_KEY=""
MINIO_ACCESS_KEY=""
MINIO_SECRET_KEY=""
API_PASSWORD=""
DATABASE_URL=""
```

## 🚀 Usage

### Main Application

#### Basic Usage (Today's Date, Default Model)

```bash
python daily_papers_tool.py
```

#### Specific Date with Default Model

```bash
python daily_papers_tool.py --date 2026-01-02
```

#### Using Google Gemini Model

```bash
python daily_papers_tool.py --model gemini-2.5-flash
```

#### Complete Example

```bash
python daily_papers_tool.py --date 2026-01-02 --model gemini-2.5-flash
```

#### Command-Line Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `--date` | string | Today's date | Date in YYYY-MM-DD format |
| `--model` | string | gpt-4.1-mini | LLM model to use (gpt-4.1-mini or gemini-2.5-flash) |

## 🗄️ Database Schema

### Papers Table

Stores basic information about papers from Hugging Face.

| Column | Type | Description |
|--------|------|-------------|
| `id` | String (PK) | ArXiv ID |
| `title` | String | Paper title |
| `authors` | JSON | List of authors |
| `published_at` | DateTime | Publication date |
| `hf_url` | String | Hugging Face URL |
| `arxiv_url` | String | ArXiv URL |
| `pdf_url` | String | PDF download URL |
| `github_url` | String | GitHub repository URL |
| `upvotes` | Integer | Number of upvotes |
| `created_at` | DateTime | Record creation time |

### PaperSummaries Table

Stores LLM-generated summaries in structured format.

| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer (PK) | Auto-increment ID |
| `paper_id` | String (FK) | Reference to papers.id |
| `tags` | JSON | List of tags/keywords |
| `main_problem` | Text | Core problem addressed |
| `main_idea` | Text | Proposed solution |
| `main_results` | Text | Key findings |
| `conclusion_future_works` | Text | Conclusion and future work |
| `publish_papers` | JSON | List of research directions |
| `patent_ideas` | JSON | List of patent ideas |
| `model_used` | String | LLM model used |
| `processed_at` | DateTime | Processing timestamp |
| `extracted_text_length` | Integer | Text length processed |

### DigestReports Table

Stores metadata about generated digest reports.

| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer (PK) | Auto-increment ID |
| `date_str` | String | Date in YYYY-MM-DD format |
| `report_path` | String | Local file path |
| `minio_object_name` | String | MinIO object name |
| `paper_count` | Integer | Number of papers |
| `model_used` | String | LLM model used |
| `created_at` | DateTime | Creation timestamp |

## 📊 Output Format

The tool generates a Markdown file named `daily_digest_YYYY-MM-DD.md` containing:

```markdown
# 🤗 Daily Hugging Face Paper Digest - 2026-01-02

Báo cáo được tạo tự động vào lúc 2026-01-02 10:30:00 bằng mô hình `gpt-4.1-mini`.

## 📰 Summary of Papers

---

## 1. Paper Title Here *(15 votes)*

**Tác giả:** Author One, Author Two, Author Three

**Xuất bản lúc:** 2025-12-30

**Tags:** tag1, tag2, tag3

### Main Problem
Core problem description...

### Main Idea
Proposed solution...

### Main Results
Key findings and metrics...

### Conclusion & Future Works
Final takeaway and next steps...

### Publish Papers (Research Directions)
1. Research direction 1
2. Research direction 2
3. Research direction 3

### Patent Ideas
1. Patent idea 1
2. Patent idea 2
3. Patent idea 3

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [link](url) |
| ArXiv Abstract | [link](url) |
| PDF Download | [link](url) |
| Github Repository | [link](url) |
```

## 📁 Project Structure

```
daily_papers_tool/
├── daily_papers_tool.py          # Main orchestration script
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables (create this)
├── .env.copy                     # Environment variables template
├── .gitignore                    # Git ignore rules
├── README.md                     # This file
│
├── database/                     # Database layer
│   ├── __init__.py
│   ├── models.py                 # SQLAlchemy models
│   └── db_utils.py               # Database utility functions
│
├── summary_utils/                # Paper processing utilities
│   ├── __init__.py
│   ├── fetch_papers.py           # Fetch from Hugging Face API
│   ├── download_papers.py        # Download PDFs from ArXiv
│   ├── extract_figure.py         # Extract figures (experimental)
│   ├── summarize_papers.py       # LLM summarization
│   └── upload_minio.py           # Upload to MinIO storage
│
├── papers/                       # Temporary PDF storage
│   └── YYYY-MM-DD/              # Date-specific folders
│
├── summaries/                   # Generated markdown reports
│   └── YYYY/                    # Year
│       └── MM/                  # Month
│           └── daily_digest_YYYY-MM-DD.md
│
└── wiki_sync_service/           # Optional: Wiki.js sync service (separate project)
    ├── sync_to_wiki.py          # Main sync script
    ├── wiki_sync_service.py     # Alternative implementation
    ├── requirements.txt         # Wiki sync dependencies
    ├── .env.copy                # Wiki sync env template
    ├── docker-compose.yml       # Docker configuration
    ├── Dockerfile               # Docker image
    ├── .dockerignore           # Docker ignore rules
    ├── .gitignore              # Git ignore rules
    ├── README.md               # Wiki sync documentation
    └── wiki_utils/             # Wiki utility functions
        ├── __init__.py
        ├── download_from_minio.py
        └── upload_to_wiki.py
```

## 🔌 Supported Models

### OpenAI
- **gpt-4.1-mini** (default) - Fast and efficient model

### Google Gemini
- **gemini-2.5-flash** - Latest Gemini model with strong performance

Both models use the `OPENAI_API_KEY` environment variable due to OpenAI-compatible API configuration.

## 🔄 Workflow

1. **Fetch Papers**: Retrieves daily trending papers from Hugging Face API (filtered by upvotes ≥ 10)
2. **Download PDFs**: Downloads PDF files from ArXiv into date-specific folders
3. **Initialize Database**: Connects to PostgreSQL and creates tables if needed
4. **Check Duplicates**: Skips papers that already have summaries in the database
5. **Extract Text**: Extracts text content from PDF files
6. **Generate Summary**: Uses LLM to create structured JSON summaries
7. **Save to Database**: Persists paper info and summary to PostgreSQL
8. **Generate Report**: Creates comprehensive Markdown report
9. **Upload to MinIO**: Stores the report in MinIO with organized structure (summaries/YYYY/MM/)
10. **Clean Up**: Respects rate limits between paper processing (5 second delay)

## 📝 Environment Variables Reference

### Main Application (.env)

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `OPENAI_API_KEY` | Yes | OpenAI or Gemini API key | `sk-...` |
| `MINIO_ACCESS_KEY` | Yes | MinIO access key | `minioadmin` |
| `MINIO_SECRET_KEY` | Yes | MinIO secret key | `minioadmin` |
| `MINIO_ENDPOINT` | No | MinIO server endpoint (default: localhost:9000) | `localhost:9000` |
| `MINIO_BUCKET` | No | MinIO bucket name (default: daily-papers) | `daily-papers` |
| `MINIO_SECURE` | No | Use HTTPS (default: false) | `false` |
| `DATABASE_URL` | Yes | PostgreSQL connection string | `postgresql://user:pass@localhost:5432/db` |
| `API_PASSWORD` | No | API password for future endpoints | `secure_password` |

## 📚 Wiki Sync Service (Optional Add-on)

The `wiki_sync_service` is a **separate, independent project** that can be used to automatically pull new summaries from MinIO and push them to Wiki.js. It is not part of the main daily_papers_tool application and operates independently.

**Use Case**: If you want to automatically sync your generated paper summaries from MinIO to a Wiki.js instance, you can use this optional add-on service.

### Setting Up Wiki Sync Service

1. Navigate to the wiki_sync_service directory:
```bash
cd wiki_sync_service
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.copy .env
```

Edit `wiki_sync_service/.env` with your credentials


4. Run the sync service:
```bash
# Sync a specific date
python sync_to_wiki.py --date 2026-01-07

# Sync today's digest
python sync_to_wiki.py --date today

# Sync by MinIO object name
python sync_to_wiki.py --object summaries/daily_digest_2026-01-07.md
```

5. Optional: Run with Docker:
```bash
docker-compose up -d
```

For detailed documentation, see [wiki_sync_service/README.md](wiki_sync_service/README.md).

## ⚠️ Troubleshooting

### Issue: "DATABASE_URL not found in environment variables"
- Ensure `.env` file exists in the project root
- Verify `DATABASE_URL` is set correctly
- Check that the file is named `.env` (not `.env.copy`)

### Issue: "No papers found"
- Check internet connection
- Verify the date format is correct (YYYY-MM-DD)
- Try a different date to confirm API is working
- Ensure Hugging Face API is accessible

### Issue: "Permission denied" or "403 error"
- Verify API keys are correct
- Check that the API key has necessary permissions
- Ensure environment variables are properly set and loaded

### Issue: "PDF extraction failed"
- Some PDFs may have text extraction issues
- The tool will skip those papers and continue
- Check console output for specific errors

### Issue: "MinIO connection failed"
- Verify MinIO server is running
- Check `MINIO_ENDPOINT`, `MINIO_ACCESS_KEY`, and `MINIO_SECRET_KEY`
- Ensure firewall allows connection to MinIO port (default: 9000)

### Issue: "PostgreSQL connection failed"
- Verify PostgreSQL server is running
- Check database connection string in `DATABASE_URL`
- Ensure the database exists (`createdb daily_papers_db`)
- Verify user has necessary permissions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request with improvements.

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

For issues, questions, or suggestions, please open an issue on GitHub.

## 📚 Changelog

### Version 3.0 (Current)
- **Added PostgreSQL Database**: Persistent storage for papers, summaries, and reports
- **Added MinIO Integration**: Object storage for markdown reports with organized structure
- **Added Duplicate Prevention**: Skips already-summarized papers to save time and costs
- **Improved Organization**: Year/month structure for summaries in both local storage and MinIO
- **Database Models**: Structured data storage with SQLAlchemy ORM
- **Wiki Sync Service**: Added as optional separate project for Wiki.js integration

### Version 2.0
- Added date-based folder organization
- Added Google Gemini support
- Added CLI arguments for date and model selection
- Improved report generation

### Version 1.0
- Initial release with basic functionality
- OpenAI GPT-4 mini support
- Markdown report generation