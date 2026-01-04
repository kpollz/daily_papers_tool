import os
import requests
import time

def download_pdf(url, save_path):
    """Downloads a PDF from a URL and saves it to save_path."""
    if os.path.exists(save_path):
        print(f"File already exists: {save_path}")
        return True
    
    try:
        print(f"Downloading {url}...")
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Saved to {save_path}")
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

def download_all_papers(papers, download_dir="papers", number_of_papers=None):
    """Downloads all PDFs for a list of papers."""
    if not os.path.exists(download_dir):
        os.makedirs(download_dir, exist_ok=True)
    
    downloaded_files = []
    for paper in papers[:number_of_papers]:
        paper_id = paper['id']
        pdf_url = paper['pdf_url']
        # Clean filename: replace / with _ if any
        safe_id = paper_id.replace('/', '_')
        save_path = os.path.join(download_dir, f"{safe_id}.pdf")
        
        if download_pdf(pdf_url, save_path):
            paper['local_path'] = save_path
            downloaded_files.append(save_path)
        
        # Be polite to ArXiv
        time.sleep(1)
    
    return downloaded_files

if __name__ == "__main__":
    from fetch_papers import fetch_daily_papers
    
    test_date = "2026-01-02"
    papers = fetch_daily_papers(test_date)
    # Just download the first 2 for testing to save time and bandwidth
    download_all_papers(papers[:2])
