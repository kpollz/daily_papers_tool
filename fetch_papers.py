import requests
from datetime import datetime

def fetch_daily_papers(date_str=None):
    """
    Fetches the list of daily papers from Hugging Face API.
    If date_str is provided (format YYYY-MM-DD), it fetches papers for that date.
    Otherwise, it fetches the latest daily papers.
    """
    url = "https://huggingface.co/api/daily_papers"
    params = {}
    if date_str:
        params['date'] = date_str
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        papers_data = response.json()
        
        extracted_papers = []
        for item in papers_data:
            paper = item.get('paper', {})
            paper_info = {
                'id': paper.get('id'),
                'title': paper.get('title'),
                'authors': [author.get('name') for author in paper.get('authors', [])],
                'published_at': paper.get('publishedAt'),
                'hf_url': f"https://huggingface.co/papers/{paper.get('id')}",
                'arxiv_url': f"https://arxiv.org/abs/{paper.get('id')}",
                'pdf_url': f"https://arxiv.org/pdf/{paper.get('id')}.pdf",
                'github_url': paper.get('githubRepo', "N/A")
            }
            extracted_papers.append(paper_info)
        
        return extracted_papers
    except Exception as e:
        print(f"Error fetching papers: {e}")
        return []

if __name__ == "__main__":
    # Test with a specific date
    test_date = "2026-01-06"
    print(f"Fetching papers for {test_date}...")
    papers = fetch_daily_papers(test_date)
    print(f"Found {len(papers)} papers.")
    for i, p in enumerate(papers[:None], 1):
        print(f"{i}. {p}")
