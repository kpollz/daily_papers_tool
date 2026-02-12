#!/usr/bin/env python3
"""
Wiki Sync Service - Automated service to sync markdown files from MinIO to Wiki.js

This service periodically checks MinIO for new summary files and automatically
syncs them to Wiki.js.
"""

import os
import json
import time
import signal
import sys
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from wiki_utils import list_objects_in_minio, read_content_from_minio, upload_to_wiki
from wiki_utils import (
    get_page_by_path,
    get_page_content,
    update_page_content,
    create_monthly_index_link,
    get_monthly_index_path
)

# Global flag for graceful shutdown
running = True


def signal_handler(sig, frame):
    """Handle shutdown signals gracefully."""
    global running
    print("\nReceived shutdown signal. Shutting down gracefully...")
    running = False


def load_synced_files(state_file=".synced_files.json"):
    """Load── list of already synced files from state file.
    
    Returns:
        set: Set of object names that have been synced
    """
    if os.path.exists(state_file):
        try:
            with open(state_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return set(data.get('synced_files', []))
        except Exception as e:
            print(f"Error loading state file: {e}")
            return set()
    return set()


def save_synced_files(synced_files, state_file=".synced_files.json"):
    """Save── list of synced files to state file.
    
    Args:
        synced_files (set): Set of object names that have been synced
        state_file (str): Path to state file
    """
    try:
        data = {
            'synced_files': list(synced_files),
            'last_updated': datetime.now().isoformat()
        }
        with open(state_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving state file: {e}")


def extract_date_from_filename(object_name):
    """Extract date from object name (e.g., summaries/daily_digest_2026-01-07.md).
    
    Returns:
        str: Date string (YYYY-MM-DD) or None if not found
    """
    try:
        # Extract filename
        filename = os.path.basename(object_name)
        # Look for date pattern
        if 'daily_digest_' in filename:
            date_part = filename.replace('daily_digest_', '').replace('.md', '')
            # Validate date format
            datetime.strptime(date_part, "%Y-%m-%d")
            return date_part
    except:
        pass
    return None


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


def update_monthly_index(date_str, digest_path):
    """Update── monthly index page with a link to── new digest.
    
    Args:
        date_str (str): Date in YYYY-MM-DD format (e.g., "2026-02-12")
        digest_path (str): Path to── digest page
    
    Returns:
        bool: True if update was successful, False otherwise
    """
    try:
        # Get── monthly index page path
        monthly_index_path = get_monthly_index_path(date_str)
        if not monthly_index_path:
            print(f"Invalid date format: {date_str}")
            return False
        
        print(f"\nUpdating monthly index page: {monthly_index_path}")
        
        # Get── page ID by path first
        locale = os.getenv('WIKI_LOCALE', 'vi')
        page_info = get_page_by_path(monthly_index_path, locale=locale)
        
        if page_info is None:
            print(f"Monthly index page not found: {monthly_index_path}")
            print("Skipping index page update. Please create── page manually.")
            return False
        
        # Get── page content using── ID
        page_id = page_info.get('id')
        page_data = get_page_content(page_id, locale=locale)
        
        if page_data is None:
            print(f"Failed to get content for page ID: {page_id}")
            return False
        
        # Create── new link
        new_link = create_monthly_index_link(date_str, digest_path)
        
        # Prepare updated content
        current_content = page_data.get('content', '')
        
        # Add── new link at── beginning of── content
        if current_content.strip():
            updated_content = new_link + "\n" + current_content
        else:
            # If content is empty, just add── link
            updated_content = new_link
        
        # Update── page
        result = update_page_content(
            page_id=page_id,
            content=updated_content,
            path=page_data.get('path', '')
        )
        
        if result:
            print(f"✓ Successfully updated monthly index: {monthly_index_path}")
            return True
        else:
            print(f"✗ Failed to update monthly index: {monthly_index_path}")
            return False
            
    except Exception as e:
        print(f"Error updating monthly index: {e}")
        import traceback
        traceback.print_exc()
        return False


def sync_object_to_wiki(object_name, synced_files, state_file):
    """Sync a single object from MinIO to Wiki.js.
    
    Args:
        object_name (str): Object name in MinIO
        synced_files (set): Set of already synced files
        state_file (str): Path to state file
    
    Returns:
        bool: True if sync was successful
    """
    if object_name in synced_files:
        return True  # Already synced
    
    print(f"\n{'='*60}")
    print(f"Processing new file: {object_name}")
    print(f"{'='*60}")
    
    # Read content from MinIO
    content = read_content_from_minio(object_name)
    if content is None:
        print(f"Failed to read content from MinIO: {object_name}")
        return False
    
    # Generate wiki title and path
    date_str = extract_date_from_filename(object_name)
    
    if date_str:
        # Title format: DD-MM-YYYY (e.g., 07-01-2026)
        wiki_title = format_date_for_title(date_str)
        # Path format: daily-papers/daily_digest_YYYY-MM-DD (e.g., daily-papers/daily_digest_2026-01-07)
        sub_path = date_str.replace("-","/")[:-3]
        wiki_path = f"daily-papers/{sub_path}/daily_digest_{date_str}"
        
    else:
        # Fallback: use object name
        base_name = os.path.basename(object_name).replace('.md', '')
        wiki_title = base_name.replace('_', ' ').title()
        wiki_path = object_name.replace('.md', '').replace('summaries/', 'daily-papers/').lstrip('/')
    
    # Upload to Wiki.js
    locale = os.getenv('WIKI_LOCALE', 'vi')
    result = upload_to_wiki(
        content=content,
        title=wiki_title,
        path=wiki_path,
        locale=locale
    )
    
    if result:
        # Mark as synced
        synced_files.add(object_name)
        save_synced_files(synced_files, state_file)
        print(f"✓ Successfully synced: {object_name}")
        
        # Update── monthly index page if date is available
        if date_str and wiki_path:
            update_monthly_index(date_str, wiki_path)
        
        return True
    else:
        print(f"✗ Failed to sync: {object_name}")
        return False


def run_service(check_interval=300, prefix="summaries/", bucket_name=None):
    """Run── sync service in a loop.
    
    Args:
        check_interval (int): Interval between checks in seconds (default: 300 = 5 minutes)
        prefix (str): Prefix to filter objects in MinIO (default: 'summaries/')
        bucket_name (str, optional): MinIO bucket name
    """
    global running
    
    # Setup signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # State file location
    state_file = os.getenv('STATE_FILE', '.synced_files.json')
    
    print("="*60)
    print("Wiki Sync Service Starting")
    print("="*60)
    print(f"Check interval: {check_interval} seconds ({check_interval/60:.1f} minutes)")
    print(f"Prefix filter: {prefix}")
    print(f"State file: {state_file}")
    print("="*60)
    
    # Load synced files
    synced_files = load_synced_files(state_file)
    print(f"Loaded {len(synced_files)} previously synced files")
    
    iteration = 0
    while running:
        iteration += 1
        try:
            print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Check #{iteration}: Scanning MinIO for new files...")
            
            # List objects in MinIO
            objects = list_objects_in_minio(prefix=prefix, bucket_name=bucket_name)
            
            if not objects:
                print("No objects found in MinIO (or error occurred)")
            else:
                print(f"Found {len(objects)} object(s) in MinIO")
                
                # Filter for markdown files
                md_objects = [obj for obj in objects if obj.endswith('.md')]
                print(f"Found {len(md_objects)} markdown file(s)")
                
                # Find new files
                new_files = [obj for obj in md_objects if obj not in synced_files]
                
                if new_files:
                    print(f"Found {len(new_files)} new file(s) to sync:")
                    for obj in new_files:
                        print(f"  - {obj}")
                    
                    # Sync each new file
                    for obj in new_files:
                        if not running:  # Check if we should stop
                            break
                        sync_object_to_wiki(obj, synced_files, state_file)
                        time.sleep(2)  # Small delay between syncs
                else:
                    print("No new files to sync")
            
            # Wait for next check
            if running:
                print(f"Waiting {check_interval} seconds until next check...")
                # Sleep in small increments to allow quick shutdown
                for _ in range(check_interval):
                    if not running:
                        break
                    time.sleep(1)
        
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error in service loop: {e}")
            import traceback
            traceback.print_exc()
            if running:
                print("Waiting 60 seconds before retry...")
                time.sleep(60)
    
    print("\n" + "="*60)
    print("Wiki Sync Service Stopped")
    print("="*60)


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Wiki Sync Service - Automated sync from MinIO to Wiki.js",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run with default settings (check every 5 minutes)
  python wiki_sync_service.py
  
  # Check every 10 minutes
  python wiki_sync_service.py --interval 600
  
  # Check every hour
  python wiki_sync_service.py --interval 3600
  
  # Custom prefix
  python wiki_sync_service.py --prefix "documents/"
        """
    )
    
    parser.add_argument(
        '--interval',
        type=int,
        default=300,
        help='Check interval in seconds (default: 300 = 5 minutes)'
    )
    
    parser.add_argument(
        '--prefix',
        type=str,
        default='summaries/',
        help='Prefix to filter objects in MinIO (default: summaries/)'
    )
    
    parser.add_argument(
        '--bucket',
        type=str,
        help='MinIO bucket name (overrides MINIO_BUCKET from .env)'
    )
    
    parser.add_argument(
        '--state-file',
        type=str,
        default='.synced_files.json',
        help='Path to state file for tracking synced files (default: .synced_files.json)'
    )
    
    args = parser.parse_args()
    
    # Set state file in environment for── service
    os.environ['STATE_FILE'] = args.state_file
    
    # Run── service
    run_service(
        check_interval=args.interval,
        prefix=args.prefix,
        bucket_name=args.bucket
    )


if __name__ == "__main__":
    main()