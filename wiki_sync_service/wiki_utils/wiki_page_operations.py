import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def get_page_by_path(path, wiki_url=None, api_token=None, locale="vi"):
    """Get page ID by path using GraphQL API.
    
    Args:
        path (str): Path of the wiki page (e.g., 'daily-papers/2026/01')
        wiki_url (str, optional): Wiki.js GraphQL endpoint. If None, uses WIKI_URL from .env
        api_token (str, optional): Wiki.js API token. If None, uses WIKI_API_TOKEN from .env
        locale (str): Locale for the page (default: 'vi')
    
    Returns:
        dict: Page data with id, path, and title, or None if page not found
    """
    try:
        wiki_url = wiki_url or os.getenv('WIKI_URL')
        api_token = api_token or os.getenv('WIKI_API_TOKEN')
        
        if not wiki_url:
            print("Error: WIKI_URL not found in .env file.")
            return None
        
        if not api_token:
            print("Error: WIKI_API_TOKEN not found in .env file.")
            return None
        
        query = """
        query($orderBy: PageOrderBy!) {
          pages {
            list(orderBy: $orderBy) {
              id
              path
              title
            }
          }
        }
        """
        
        variables = {
            "orderBy": "TITLE"
        }
        
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            wiki_url,
            json={'query': query, 'variables': variables},
            headers=headers,
            timeout=30
        )
        
        response.raise_for_status()
        result = response.json()
        
        # Check for GraphQL errors
        if 'errors' in result:
            print(f"GraphQL errors: {result['errors']}")
            return None
        
        # Find the page with matching path
        pages = result.get('data', {}).get('pages', {}).get('list', [])
        for page in pages:
            if page.get('path') == path:
                return page
        
        print(f"Page not found with path: {path}")
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error getting page by path from Wiki.js: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error getting page by path: {e}")
        return None


def get_page_content(page_id, wiki_url=None, api_token=None, locale="vi"):
    """Get the content of an existing wiki page using GraphQL API by page ID.
    
    Args:
        page_id (int): ID of the wiki page
        wiki_url (str, optional): Wiki.js GraphQL endpoint. If None, uses WIKI_URL from .env
        api_token (str, optional): Wiki.js API token. If None, uses WIKI_API_TOKEN from .env
        locale (str): Locale for the page (default: 'vi')
    
    Returns:
        dict: Page data including content, title, and id, or None if page not found
    """
    try:
        wiki_url = wiki_url or os.getenv('WIKI_URL')
        api_token = api_token or os.getenv('WIKI_API_TOKEN')
        
        if not wiki_url:
            print("Error: WIKI_URL not found in .env file.")
            return None
        
        if not api_token:
            print("Error: WIKI_API_TOKEN not found in .env file.")
            return None
        
        query = """
        query($id: Int!) {
          pages {
            single(id: $id) {
              id
              path
              title
              content
              createdAt
              updatedAt
              locale
              description
            }
          }
        }
        """
        
        variables = {
            "id": page_id
        }
        
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            wiki_url,
            json={'query': query, 'variables': variables},
            headers=headers,
            timeout=30
        )
        
        response.raise_for_status()
        result = response.json()
        
        # Check for GraphQL errors
        if 'errors' in result:
            print(f"GraphQL errors: {result['errors']}")
            return None
        
        page_data = result.get('data', {}).get('pages', {}).get('single')
        return page_data
        
    except requests.exceptions.RequestException as e:
        print(f"Error getting page content from Wiki.js: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error getting page content: {e}")
        return None


def update_page_content(page_id, content, path, wiki_url=None, api_token=None, tags=["papers-summary", "huggingface-papers"]):
    """Update an existing wiki page using GraphQL API.
    
    Args:
        page_id (int): ID of the page to update
        content (str): New markdown content
        path (str): Path of the page
        wiki_url (str, optional): Wiki.js GraphQL endpoint. If None, uses WIKI_URL from .env
        api_token (str, optional): Wiki.js API token. If None, uses WIKI_API_TOKEN from .env
        tags (list): List of tags for the page (default: None - keeps existing)
    
    Returns:
        dict: Response from Wiki.js API, or None if update failed
    """
    try:
        wiki_url = wiki_url or os.getenv('WIKI_URL')
        api_token = api_token or os.getenv('WIKI_API_TOKEN')
        
        if not wiki_url:
            print("Error: WIKI_URL not found in .env file.")
            return None
        
        if not api_token:
            print("Error: WIKI_API_TOKEN not found in .env file.")
            return None
        
        # Build the mutation with optional title parameter
        query = """
        mutation($id: Int!, $content: String!, $path: String!, $tags: [String!]) {
          pages {
            update(
              id: $id,
              content: $content,
              path: $path,
              tags: $tags,
              isPublished: true
            ) {
              responseResult {
                succeeded
                message
              }
              page {
                id
                content
              }
            }
          }
        }
        """
        
        variables = {
            "id": page_id,
            "content": content,
            "path": path,
            "tags": tags
        }
        
        
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            wiki_url,
            json={'query': query, 'variables': variables},
            headers=headers,
            timeout=30
        )
        
        response.raise_for_status()
        result = response.json()
        
        # Check for GraphQL errors
        if 'errors' in result:
            print(f"GraphQL errors: {result['errors']}")
            return None
        
        # Check if the mutation was successful
        response_result = result.get('data', {}).get('pages', {}).get('update', {}).get('responseResult', {})
        if response_result.get('succeeded'):
            print(f"Successfully updated wiki page (ID: {page_id})")
            return result
        else:
            print(f"Wiki.js update failed: {response_result.get('message', 'Unknown error')}")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error updating wiki page: {e}")
        if hasattr(e, 'response') and e.response is not None:
            try:
                print(f"Response: {e.response.text}")
            except:
                pass
        return None
    except Exception as e:
        print(f"Unexpected error updating wiki page: {e}")
        return None


def create_monthly_index_link(date_str, digest_path):
    """Create a markdown link for the monthly index page.
    
    Args:
        date_str (str): Date in YYYY-MM-DD format (e.g., "2026-02-12")
        digest_path (str): Path to the digest page (e.g., "/daily-paper/2026/02/daily_digest_2026-02-12")
    
    Returns:
        str: Markdown formatted link
    """
    # Convert YYYY-MM-DD to DD-MM-YYYY
    from datetime import datetime
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%d-%m-%Y")
    except:
        formatted_date = date_str
    
    # Create the link in Vietnamese format
    link = f"- [[{formatted_date}]*Tóm tắt các bài báo thuộc top ngày {formatted_date}*](/{digest_path})"
    return link


def get_monthly_index_path(date_str):
    """Get the path for the monthly index page based on date.
    
    Args:
        date_str (str): Date in YYYY-MM-DD format (e.g., "2026-02-12")
    
    Returns:
        str: Path to monthly index page (e.g., "daily-papers/2026/02")
    """
    parts = date_str.split("-")
    if len(parts) == 3:
        year = parts[0]
        month = parts[1]
        return f"daily-papers/{year}/{month}"
    return None