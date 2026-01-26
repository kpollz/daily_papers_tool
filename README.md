# Hugging Face Daily Paper Digest Tool

An automated tool that fetches, downloads, and summarizes daily trending papers from Hugging Face using AI-powered analysis.

## Features

- **Automated Paper Fetching**: Retrieves the daily paper list directly from the Hugging Face API
- **Smart PDF Management**: Downloads papers from ArXiv and organizes them by date
- **Automatic Cleanup**: Deletes PDFs after processing to save disk space
- **AI Summarization**: Uses LLM to read and summarize papers into structured formats
- **Flexible LLM Support**: Choose between OpenAI GPT-4 mini or Google Gemini
- **Markdown Reporting**: Generates comprehensive reports with summaries and links

## What's New

### Recent Updates

- **Date-based Organization**: PDFs are now organized into `papers/YYYY-MM-DD/` folders
- **Automatic Cleanup**: PDF files are automatically deleted after processing
- **Gemini Support**: Added Google Gemini as an alternative LLM provider
- **CLI Arguments**: New command-line options for date and model selection

## Components

| File | Purpose |
|------|---------|
| `fetch_papers.py` | Fetches the paper list from Hugging Face API |
| `download_papers.py` | Downloads PDFs from ArXiv |
| `summarize_papers.py` | Extracts text and generates summaries using LLM |
| `daily_papers_tool.py` | Main orchestration script |
| `api.py` | FastAPI REST API server |

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kpollz/daily_papers_tool.git
   cd daily_papers_tool
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**:
   
   Tạo file `.env` trong thư mục gốc:
   ```env
   API_PASSWORD=your_secure_password_here
   OPENAI_API_KEY=your-api-key-here
   ```
   
   Hoặc export trực tiếp:
   ```bash
   export API_PASSWORD="your_secure_password_here"
   export OPENAI_API_KEY="your-api-key-here"
   ```

## Usage

### Command Line Interface

#### Basic Usage (Today's Date, OpenAI GPT-4 mini)

```bash
python daily_papers_tool.py
```

#### Specific Date with Default Model

```bash
python daily_papers_tool.py --date 2026-01-02
```

#### Using Google Gemini

```bash
python daily_papers_tool.py --model gemini-2.5-flash
```

#### Specific Date with Gemini

```bash
python daily_papers_tool.py --date 2026-01-02 --model gemini-2.5-flash
```

### REST API (FastAPI)

Dự án đã được nâng cấp với FastAPI để cung cấp REST API endpoint dễ sử dụng.

#### Khởi động API Server

```bash
# Cách 1: Sử dụng uvicorn trực tiếp
uvicorn api:app --host 0.0.0.0 --port 8000

# Cách 2: Chạy trực tiếp file api.py
python api.py
```

Sau khi khởi động, API sẽ chạy tại: `http://localhost:8000`

#### Cấu hình Authentication

1. Tạo file `.env` trong thư mục gốc của dự án
2. Thêm mật khẩu API:

```env
API_PASSWORD=your_secure_password_here
```

#### Sử dụng API

##### POST Request (JSON Body)

```bash
curl -X POST "http://localhost:8000/generate-digest" \
  -u "username:your_secure_password_here" \
  -H "Content-Type: application/json" \
  -d '{
    "day": 15,
    "month": 1,
    "year": 2026,
    "model": "gpt-4.1-mini"
  }'
```

##### GET Request (Query Parameters)

```bash
curl -X GET "http://localhost:8000/generate-digest?day=15&month=1&year=2026&model=gpt-4.1-mini" \
  -u "username:your_secure_password_here"
```

##### Sử dụng Python requests

```python
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:8000/generate-digest"
auth = HTTPBasicAuth("username", "your_secure_password_here")

# POST method
response = requests.post(
    url,
    auth=auth,
    json={
        "day": 15,
        "month": 1,
        "year": 2026,
        "model": "gpt-4.1-mini"
    }
)

print(response.json())

# GET method
response = requests.get(
    url,
    auth=auth,
    params={
        "day": 15,
        "month": 1,
        "year": 2026,
        "model": "gpt-4.1-mini"
    }
)

print(response.json())
```

#### API Endpoints

| Endpoint | Method | Mô tả |
|----------|--------|-------|
| `/` | GET | Kiểm tra trạng thái API |
| `/generate-digest` | POST | Tạo tóm tắt với JSON body |
| `/generate-digest` | GET | Tạo tóm tắt với query parameters |

#### API Response

```json
{
  "success": true,
  "message": "Đã tạo tóm tắt thành công cho ngày 2026-01-15",
  "date": "2026-01-15",
  "model": "gpt-4.1-mini",
  "output_file": "summaries/daily_digest_2026-01-15.md",
  "username": "username"
}
```

#### API Documentation

Khi API server đang chạy, bạn có thể truy cập:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Command-Line Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `--date` | string | Today's date | Date in YYYY-MM-DD format |
| `--model` | string | gpt-4.1-mini | LLM model to use (gpt-4.1-mini or gemini-2.5-flash) |

## Output

The tool generates a Markdown file named `daily_digest_YYYY-MM-DD.md` containing:

- Paper title and authors
- Publication date
- **Main Problem**: Core issue addressed
- **Main Idea**: Proposed solution or approach
- **Main Results**: Key findings and metrics
- **Conclusion & Future Works**: Final takeaway and next steps
- **Related Links**: Hugging Face, ArXiv, GitHub, and PDF links

### Example Output Structure

```markdown
# Daily Hugging Face Paper Digest - 2026-01-02

## 1. Paper Title Here

**Authors:** Author One, Author Two, Author Three

**Published:** 2025-12-30

- Main Problem: ...
- Main Idea: ...
- Main Results: ...
- Conclusion & Future Works: ...

### Related Links

| Platform | Link |
| :--- | :--- |
| Hugging Face | [link] |
| ArXiv Abstract | [link] |
| PDF Download | [link] |
| GitHub | [link] |
```

## How It Works

1. **Fetch**: Retrieves the list of trending papers from Hugging Face API
2. **Download**: Downloads PDF files from ArXiv into date-specific folders
3. **Extract**: Extracts text from the first 10 pages of each PDF
4. **Summarize**: Uses LLM (OpenAI or Gemini) to generate structured summaries
5. **Cleanup**: Automatically deletes PDF files and empty folders
6. **Report**: Generates a comprehensive Markdown report with all summaries

## Supported Models

### OpenAI
- `gpt-4.1-mini` (default) - Fast and efficient model

### Google Gemini
- `gemini-2.5-flash` - Latest Gemini model with strong performance

## Environment Setup

### For OpenAI Models

```bash
export OPENAI_API_KEY="sk-..."
```

### For Google Gemini

```bash
export OPENAI_API_KEY="your-gemini-api-key"
```

Note: Both models use the same environment variable in this setup due to the OpenAI-compatible API configuration.

## File Organization

```
daily_papers_tool/
├── daily_papers_tool.py          # Main script
├── fetch_papers.py               # API fetching
├── download_papers.py            # PDF downloading
├── summarize_papers.py           # LLM summarization
├── README.md                      # Documentation
└── papers/                        # Temporary storage (auto-cleaned)
    └── 2026-01-02/               # Date-specific folder
        └── (PDFs stored here, then deleted)
```

## Performance Considerations

- **Download Time**: ~1-2 seconds per paper (respects ArXiv rate limits)
- **Summarization Time**: ~10-30 seconds per paper (depends on model and paper length)
- **Total Time**: ~2-5 minutes for 7 papers (typical daily digest)

## Troubleshooting

### Issue: "No papers found"
- Check your internet connection
- Verify the date format is correct (YYYY-MM-DD)
- Try a different date to confirm API is working

### Issue: "Permission denied" or "403 error"
- Verify your API key is correct
- Check that the API key has the necessary permissions
- Ensure environment variable is properly set

### Issue: "PDF extraction failed"
- Some PDFs may have text extraction issues
- The tool will skip those papers and continue
- Check the console output for specific errors

### Issue: Model not found
- Update the openai package: `pip install --upgrade openai`
- Verify the model name is correct (gpt-4.1-mini or gemini-2.5-flash)

## Contributing

Contributions are welcome! Please feel free to submit a pull request with improvements.

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

## Changelog

### Version 2.1 (Latest)
- **Added FastAPI REST API**: API endpoint với Basic Authentication
- **Flexible Input**: Nhận day, month, year riêng biệt thay vì date string
- **API Documentation**: Swagger UI và ReDoc tự động
- **Environment-based Security**: Mật khẩu API từ file .env

### Version 2.0
- Added date-based folder organization
- Implemented automatic PDF cleanup
- Added Google Gemini support
- Added CLI arguments for date and model selection
- Improved report generation with model information

### Version 1.0
- Initial release with basic functionality
- OpenAI GPT-4 mini support
- Markdown report generation
