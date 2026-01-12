# Wiki Sync Service

Automated service to synchronize markdown files from MinIO to Wiki.js.

## Overview

This service periodically checks MinIO for new summary files and automatically uploads them to Wiki.js. It tracks which files have been synced to avoid duplicate uploads.

## Features

- 🔄 Automatic periodic checking of MinIO for new files
- 📝 Syncs markdown files to Wiki.js via GraphQL API
- ✅ Tracks synced files to avoid duplicates
- 🐳 Docker support with docker-compose
- 🔧 Configurable check intervals and prefixes
- 🛡️ Graceful shutdown handling

## Setup

### Environment Variables

Create a `.env` file in the `wiki_sync_service` directory with the following variables:

```env
# MinIO Configuration
MINIO_ENDPOINT=minio.smartsolar.io.vn
MINIO_PORT=9000
MINIO_ACCESS_KEY=your_minio_access_key
MINIO_SECRET_KEY=your_minio_secret_key
MINIO_BUCKET=dtung.vu
MINIO_SECURE=true

# Wiki.js Configuration
WIKI_URL=https://your-wiki-site.com/graphql
WIKI_API_TOKEN=your_wiki_api_token
WIKI_LOCALE=vi

# Service Configuration (Optional)
CHECK_INTERVAL=300  # Check interval in seconds (default: 300 = 5 minutes)
PREFIX=summaries/   # Prefix to filter objects in MinIO (default: summaries/)
```

### Running Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the service:
```bash
python wiki_sync_service.py
```

3. Run with custom options:
```bash
# Check every 10 minutes
python wiki_sync_service.py --interval 600

# Custom prefix
python wiki_sync_service.py --prefix "documents/"

# Custom state file location
python wiki_sync_service.py --state-file /path/to/state.json
```

### Running with Docker

1. Build and run with docker-compose:
```bash
docker-compose up -d
```

2. View logs:
```bash
docker-compose logs -f
```

3. Stop the service:
```bash
docker-compose down
```

4. Rebuild after code changes:
```bash
docker-compose up -d --build
```

### Running with Docker (Manual)

1. Build the image:
```bash
docker build -t wiki-sync-service .
```

2. Run the container:
```bash
docker run -d \
  --name wiki-sync-service \
  --restart unless-stopped \
  --env-file .env \
  -v $(pwd)/data:/app/data \
  wiki-sync-service
```

## Usage

### Command Line Options

```bash
python wiki_sync_service.py [OPTIONS]

Options:
  --interval SECONDS    Check interval in seconds (default: 300)
  --prefix PREFIX       Prefix to filter objects (default: summaries/)
  --bucket BUCKET       MinIO bucket name (overrides .env)
  --state-file PATH     Path to state file (default: .synced_files.json)
```

### Manual Sync

You can also manually sync specific files using the `sync_to_wiki.py` script:

```bash
# Sync by date
python sync_to_wiki.py --date 2026-01-07

# Sync specific file
python sync_to_wiki.py --object summaries/daily_digest_2026-01-07.md
```

## How It Works

1. **Periodic Checking**: The service checks MinIO at regular intervals (default: 5 minutes)
2. **Object Listing**: Lists all objects matching the prefix (default: `summaries/`)
3. **Filtering**: Filters for markdown files (`.md` extension)
4. **State Tracking**: Compares against previously synced files (stored in `.synced_files.json`)
5. **Sync**: For each new file:
   - Downloads content from MinIO
   - Generates appropriate title and path for Wiki.js
   - Uploads to Wiki.js via GraphQL API
   - Marks as synced in state file

## State File

The service maintains a state file (`.synced_files.json` by default) to track which files have been synced. This file contains:

```json
{
  "synced_files": [
    "summaries/daily_digest_2026-01-07.md",
    "summaries/daily_digest_2026-01-08.md"
  ],
  "last_updated": "2026-01-12T10:30:00"
}
```

To reset and re-sync all files, simply delete this file.

## Troubleshooting

### Service not finding files

- Check that `MINIO_BUCKET` and `PREFIX` are correct
- Verify MinIO credentials are correct
- Check MinIO endpoint and port settings

### Upload failures

- Verify `WIKI_URL` and `WIKI_API_TOKEN` are correct
- Check Wiki.js API token permissions
- Review service logs for specific error messages

### Files not being detected

- Ensure file naming matches expected pattern (e.g., `summaries/daily_digest_YYYY-MM-DD.md`)
- Check that files end with `.md` extension
- Verify state file isn't corrupted (delete it to reset)

## Development

### Project Structure

```
wiki_sync_service/
├── wiki_utils/              # Utility modules
│   ├── __init__.py
│   ├── download_from_minio.py
│   └── upload_to_wiki.py
├── wiki_sync_service.py     # Main service daemon
├── sync_to_wiki.py          # Manual sync script
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker image definition
├── docker-compose.yml       # Docker Compose configuration
└── README.md               # This file
```

## License

Part of the daily_papers_tool project.

