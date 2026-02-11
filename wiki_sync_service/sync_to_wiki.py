#!/usr/bin/env python3
"""
Sync markdown files from MinIO to Wiki.js

This script fetches markdown files from MinIO server and uploads them to Wiki.js.
"""

import os
import argparse
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from wiki_utils import download_from_minio, read_content_from_minio, upload_to_wiki
from datetime import datetime


def format_date_for_title(date_str):
    """Convert date from YYYY-MM-DD to DD-MM-YYYY format for title.
    
    Args:
        date_str (str): Date in YYYY-MM-DD format
    
    Returns:
        str: Date in DD-MM-YYYY format
    """
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d-%m-%Y")
    except:
        return date_str


def extract_date_from_filename(object_name):
    """Extract date from object name (e.g., summaries/daily_digest_2026-01-07.md).
    
    Returns:
        str: Date string (YYYY-MM-DD) or None if not found
    """
    try:
        filename = os.path.basename(object_name)
        if 'daily_digest_' in filename:
            date_part = filename.replace('daily_digest_', '').replace('.md', '')
            datetime.strptime(date_part, "%Y-%m-%d")
            return date_part
    except:
        pass
    return None


def sync_file_to_wiki(object_name, wiki_title=None, wiki_path=None, bucket_name=None, locale="vi"):
    """Syncs a single file from MinIO to Wiki.js.
    
    Args:
        object_name (str): Object name/path in MinIO (e.g., 'summaries/daily_digest_2026-01-07.md')
        wiki_title (str, optional): Title for the wiki page. If None, extracts from object_name
        wiki_path (str, optional): Path for the wiki page. If None, generates from object_name
        bucket_name (str, optional): MinIO bucket name. If None, uses MINIO_BUCKET from .env
        locale (str): Locale for the wiki page (default: 'en')
    
    Returns:
        bool: True if sync was successful, False otherwise
    """
    print(f"--- Syncing {object_name} from MinIO to Wiki.js ---")
    
    # Read content from MinIO
    print(f"Step 1: Downloading content from MinIO...")
    content = read_content_from_minio(object_name, bucket_name=bucket_name)
    
    if content is None:
        print("Failed to download content from MinIO. Aborting.")
        return False
    
    print(f"Content downloaded successfully ({len(content)} characters)")
    
    # Generate wiki title and path if not provided
    if wiki_title is None or wiki_path is None:
        date_str = extract_date_from_filename(object_name)
        if date_str:
            if wiki_title is None:
                # Title format: DD-MM-YYYY (e.g., 07-01-2026)
                wiki_title = format_date_for_title(date_str)
            if wiki_path is None:
                # Path format: daily-papers/daily_digest_YYYY-MM-DD (e.g., daily-papers/daily_digest_2026-01-07)
                wiki_path = f"daily-papers/{date_str.replace("-","/")[:-3]}/daily_digest_{date_str}"
        else:
            # Fallback: use object name
            base_name = os.path.basename(object_name).replace('.md', '')
            if wiki_title is None:
                wiki_title = base_name.replace('_', ' ').title()
            if wiki_path is None:
                wiki_path = object_name.replace('.md', '').replace('summaries/', 'daily-papers/').lstrip('/')
    
    # Upload to Wiki.js
    print(f"Step 2: Uploading to Wiki.js...")
    print(f"  Title: {wiki_title}")
    print(f"  Path: {wiki_path}")
    
    result = upload_to_wiki(
        content=content,
        title=wiki_title,
        path=wiki_path,
        locale=locale
    )
    
    if result:
        print(f"--- Successfully synced {object_name} to Wiki.js ---")
        return True
    else:
        print(f"--- Failed to sync {object_name} to Wiki.js ---")
        return False


def sync_by_date(date_str, bucket_name=None, locale="vi"):
    """Syncs a daily digest file by date.
    
    Args:
        date_str (str): Date in YYYY-MM-DD format
        bucket_name (str, optional): MinIO bucket name
        locale (str): Locale for the wiki page (default: 'vi')
    
    Returns:
        bool: True if sync was successful, False otherwise
    """
    object_name = f"summaries/daily_digest_{date_str}.md"
    # Title format: DD-MM-YYYY (e.g., 07-01-2026)
    wiki_title = format_date_for_title(date_str)
    # Path format: daily-papers/daily_digest_YYYY-MM-DD (e.g., daily-papers/daily_digest_2026-01-07)
    wiki_path = f"daily-papers/{date_str.replace("-","/")[:-3]}/daily_digest_{date_str}"
    
    return sync_file_to_wiki(
        object_name=object_name,
        wiki_title=wiki_title,
        wiki_path=wiki_path,
        bucket_name=bucket_name,
        locale=locale
    )


def main():
    parser = argparse.ArgumentParser(
        description="Sync markdown files from MinIO to Wiki.js",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Sync a specific file by object name
  python sync_to_wiki.py --object summaries/daily_digest_2026-01-07.md
  
  # Sync by date
  python sync_to_wiki.py --date 2026-01-07
  
  # Sync today's digest
  python sync_to_wiki.py --date today
  
  # Sync with custom title and path
  python sync_to_wiki.py --object summaries/daily_digest_2026-01-07.md \\
                         --title "My Custom Title" \\
                         --path research/papers/2026-01-07
        """
    )
    
    parser.add_argument(
        '--object',
        type=str,
        help='MinIO object name/path (e.g., summaries/daily_digest_2026-01-07.md)'
    )
    
    parser.add_argument(
        '--date',
        type=str,
        help='Date in YYYY-MM-DD format, or "today" for today\'s date'
    )
    
    parser.add_argument(
        '--title',
        type=str,
        help='Custom title for the wiki page'
    )
    
    parser.add_argument(
        '--path',
        type=str,
        help='Custom path for the wiki page (e.g., research/summaries/2026-01-07)'
    )
    
    parser.add_argument(
        '--bucket',
        type=str,
        help='MinIO bucket name (overrides MINIO_BUCKET from .env)'
    )
    
    parser.add_argument(
        '--locale',
        type=str,
        default='en',
        help='Locale for the wiki page (default: en)'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.object and not args.date:
        parser.error("Either --object or --date must be specified")
    
    if args.object and args.date:
        parser.error("Cannot specify both --object and --date")
    
    # Handle date
    if args.date:
        if args.date.lower() == 'today':
            date_str = datetime.now().strftime("%Y-%m-%d")
        else:
            date_str = args.date
            # Validate date format
            try:
                datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                parser.error(f"Invalid date format: {date_str}. Expected YYYY-MM-DD")
        
        success = sync_by_date(date_str, bucket_name=args.bucket, locale=args.locale)
    else:
        # Sync by object name
        success = sync_file_to_wiki(
            object_name=args.object,
            wiki_title=args.title,
            wiki_path=args.path,
            bucket_name=args.bucket,
            locale=args.locale
        )
    
    exit(0 if success else 1)


if __name__ == "__main__":
    main()

