"""
Database utility functions for saving and retrieving paper summaries (PostgreSQL)
"""
from datetime import datetime
from .models import init_db, get_session, Paper, PaperSummary, DigestReport
from summary_utils.summarize_papers import generate_markdown_from_summary

# Initialize database engine (lazy initialization)
_engine = None

def get_engine():
    """Get or create the database engine"""
    global _engine
    if _engine is None:
        _engine = init_db()
    return _engine

def save_paper_and_summary(paper_info, summary_json, model_used, text_length):
    """
    Save paper information and its summary to the database.
    Returns the created PaperSummary object.
    """
    session = get_session(get_engine())
    
    try:
        # Check if paper already exists
        existing_paper = session.query(Paper).filter_by(id=paper_info['id']).first()
        
        if existing_paper:
            paper = existing_paper
            print(f"Paper {paper_info['id']} already exists in database. Updating...")
        else:
            # Create new paper record
            paper = Paper(
                id=paper_info['id'],
                title=paper_info['title'],
                authors=paper_info['authors'],
                published_at=datetime.strptime(paper_info['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ') if paper_info.get('published_at') else None,
                hf_url=paper_info['hf_url'],
                arxiv_url=paper_info['arxiv_url'],
                pdf_url=paper_info['pdf_url'],
                github_url=paper_info.get('github_url', 'N/A'),
                upvotes=paper_info.get('upvotes', 0)
            )
            session.add(paper)
            session.commit()
            session.refresh(paper)
        
        # Create or update summary
        existing_summary = session.query(PaperSummary).filter_by(paper_id=paper_info['id']).first()
        
        if existing_summary:
            # Update existing summary
            existing_summary.tags = summary_json.get('tags', [])
            existing_summary.main_problem = summary_json.get('main_problem')
            existing_summary.main_idea = summary_json.get('main_idea')
            existing_summary.main_results = summary_json.get('main_results')
            existing_summary.conclusion_future_works = summary_json.get('conclusion_future_works')
            existing_summary.publish_papers = summary_json.get('publish_papers', [])
            existing_summary.patent_ideas = summary_json.get('patent_ideas', [])
            existing_summary.model_used = model_used
            existing_summary.processed_at = datetime.utcnow()
            existing_summary.extracted_text_length = text_length
            session.commit()
            session.refresh(existing_summary)
            print(f"Updated summary for paper {paper_info['id']}")
            return existing_summary
        else:
            # Create new summary
            summary = PaperSummary(
                paper_id=paper_info['id'],
                tags=summary_json.get('tags', []),
                main_problem=summary_json.get('main_problem'),
                main_idea=summary_json.get('main_idea'),
                main_results=summary_json.get('main_results'),
                conclusion_future_works=summary_json.get('conclusion_future_works'),
                publish_papers=summary_json.get('publish_papers', []),
                patent_ideas=summary_json.get('patent_ideas', []),
                model_used=model_used,
                extracted_text_length=text_length
            )
            session.add(summary)
            session.commit()
            session.refresh(summary)
            print(f"Saved new summary for paper {paper_info['id']}")
            return summary
            
    except Exception as e:
        session.rollback()
        print(f"Error saving paper and summary: {e}")
        raise
    finally:
        session.close()

def get_papers_with_summaries(date_str=None):
    """
    Retrieve papers with their summaries from the database.
    If date_str is provided, filter by publication date.
    Returns list of dictionaries with paper and summary data.
    """
    session = get_session(get_engine())
    
    try:
        query = session.query(Paper).join(PaperSummary)
        
        if date_str:
            # Filter by publication date
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                start_date = date_obj
                end_date = date_obj.replace(hour=23, minute=59, second=59)
                query = query.filter(Paper.published_at >= start_date, Paper.published_at <= end_date)
            except ValueError:
                print(f"Invalid date format: {date_str}")
                return []
        
        papers = query.all()
        
        results = []
        for paper in papers:
            paper_dict = {
                'paper': {
                    'id': paper.id,
                    'title': paper.title,
                    'authors': paper.authors,
                    'published_at': paper.published_at.isoformat() if paper.published_at else None,
                    'hf_url': paper.hf_url,
                    'arxiv_url': paper.arxiv_url,
                    'pdf_url': paper.pdf_url,
                    'github_url': paper.github_url,
                    'upvotes': paper.upvotes
                },
                'summary': paper.summary
            }
            results.append(paper_dict)
        
        return results
        
    except Exception as e:
        print(f"Error retrieving papers with summaries: {e}")
        return []
    finally:
        session.close()

def save_digest_report(date_str, report_path, minio_object_name, paper_count, model_used):
    """
    Save digest report metadata to the database.
    Returns the created DigestReport object.
    """
    session = get_session(get_engine())
    
    try:
        report = DigestReport(
            date_str=date_str,
            report_path=report_path,
            minio_object_name=minio_object_name,
            paper_count=paper_count,
            model_used=model_used
        )
        session.add(report)
        session.commit()
        session.refresh(report)
        print(f"Saved digest report for {date_str}")
        return report
        
    except Exception as e:
        session.rollback()
        print(f"Error saving digest report: {e}")
        raise
    finally:
        session.close()

def get_summary_by_paper_id(paper_id):
    """
    Get a paper summary by its ID.
    Returns the PaperSummary object or None.
    """
    session = get_session(get_engine())
    
    try:
        summary = session.query(PaperSummary).filter_by(paper_id=paper_id).first()
        return summary
    except Exception as e:
        print(f"Error retrieving summary for paper {paper_id}: {e}")
        return None
    finally:
        session.close()

def check_paper_exists(paper_id):
    """
    Check if a paper and its summary already exist in the database.
    Returns (paper_exists, summary_exists)
    """
    session = get_session(get_engine())
    
    try:
        paper = session.query(Paper).filter_by(id=paper_id).first()
        if not paper:
            return (False, False)
        
        summary = session.query(PaperSummary).filter_by(paper_id=paper_id).first()
        return (True, summary is not None)
    except Exception as e:
        print(f"Error checking paper existence: {e}")
        return (False, False)
    finally:
        session.close()