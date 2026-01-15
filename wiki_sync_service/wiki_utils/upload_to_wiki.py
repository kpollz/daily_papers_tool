import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def upload_to_wiki(content, title, path, wiki_url=None, api_token=None, locale="vi", description="", is_published=True, is_private=False, tags=None):
    """Uploads markdown content to Wiki.js using GraphQL API.
    
    Args:
        content (str): Markdown content to upload
        title (str): Title of the wiki page
        path (str): Path/URL path for the wiki page (e.g., 'daily-papers/daily_digest_2026-01-07')
        wiki_url (str, optional): Wiki.js GraphQL endpoint. If None, uses WIKI_URL from .env
        api_token (str, optional): Wiki.js API token. If None, uses WIKI_API_TOKEN from .env
        locale (str): Locale for the page (default: 'vi')
        description (str): Description of the page (default: empty string)
        is_published (bool): Whether the page should be published immediately (default: True)
        is_private (bool): Whether the page should be private (default: False)
        tags (list): List of tags for the page (default: ['daily-papers-summary'])
    
    Returns:
        dict: Response from Wiki.js API, or None if upload failed
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
        
        if tags is None:
            tags = ["daily-papers-summary"]
        
        query = """
        mutation($content: String!, $title: String!, $path: String!, $editor: String!, $isPublished: Boolean!, $isPrivate: Boolean!, $locale: String!, $description: String!, $tags: [String!]!) {
          pages {
            create(
              content: $content,
              title: $title,
              path: $path,
              editor: $editor,
              isPublished: $isPublished,
              isPrivate: $isPrivate,
              locale: $locale,
              description: $description,
              tags: $tags
            ) {
              responseResult {
                succeeded
                message
                slug
              }
              page {
                id
                path
                title
              }
            }
          }
        }
        """
        
        variables = {
            "content": content,
            "title": title,
            "path": path,
            "editor": "markdown",
            "isPublished": is_published,
            "isPrivate": is_private,
            "locale": locale,
            "description": description,
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
        response_result = result.get('data', {}).get('pages', {}).get('create', {}).get('responseResult', {})
        response_slug = response_result.get('slug', 'Unknown error')
        if response_result.get('succeeded') or response_slug == "PageDuplicateCreate":
            print(f"Successfully uploaded to Wiki.js: {title} at path {path}")
            return result
        else:
            print(f"Wiki.js upload failed: {response_result.get('message', 'Unknown error')}")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error uploading to Wiki.js: {e}")
        if hasattr(e, 'response') and e.response is not None:
            try:
                print(f"Response: {e.response.text}")
            except:
                pass
        return None
    except Exception as e:
        print(f"Unexpected error uploading to Wiki.js: {e}")
        return None

