"""
Database models for paper summaries using SQLAlchemy with PostgreSQL
"""
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Text, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

load_dotenv()

Base = declarative_base()

class Paper(Base):
    """Paper model - stores basic paper information from Hugging Face"""
    __tablename__ = 'papers'
    
    id = Column(String, primary_key=True)  # ArXiv ID
    title = Column(String, nullable=False)
    authors = Column(JSON)  # List of authors
    published_at = Column(DateTime)
    hf_url = Column(String)
    arxiv_url = Column(String)
    pdf_url = Column(String)
    github_url = Column(String)
    upvotes = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship to summary
    summary = relationship("PaperSummary", back_populates="paper", uselist=False)

class PaperSummary(Base):
    """Paper summary model - stores LLM-generated summary in structured format"""
    __tablename__ = 'paper_summaries'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    paper_id = Column(String, ForeignKey('papers.id'), nullable=False)
    
    # LLM-generated fields
    tags = Column(JSON)  # List of tags/keywords
    main_problem = Column(Text)
    main_idea = Column(Text)
    main_results = Column(Text)
    conclusion_future_works = Column(Text)
    
    # Brainstorming section
    publish_papers = Column(JSON)  # List of 3 research directions
    patent_ideas = Column(JSON)  # List of 3 patent ideas
    
    # Metadata
    model_used = Column(String)  # e.g., "gpt-4.1-mini", "gemini-2.5-flash"
    processed_at = Column(DateTime, default=datetime.utcnow)
    extracted_text_length = Column(Integer)  # Track how much text was processed
    
    # Relationship to paper
    paper = relationship("Paper", back_populates="summary")

class DigestReport(Base):
    """Daily digest report model - stores generated markdown reports"""
    __tablename__ = 'digest_reports'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    date_str = Column(String, nullable=False)  # YYYY-MM-DD format
    report_path = Column(String)  # Local file path
    minio_object_name = Column(String)  # MinIO object name
    paper_count = Column(Integer)
    model_used = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

def init_db():
    """Initialize database connection and create tables"""
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("DATABASE_URL not found in environment variables")
    
    # URL-encode password to handle special characters like @
    try:
        if 'postgresql://' in database_url:
            # Remove postgresql:// prefix
            url_without_prefix = database_url.replace('postgresql://', '')
            
            # Split by @ to separate credentials from host
            # Use rsplit to split from right (important when password contains @)
            parts = url_without_prefix.rsplit('@', 1)
            
            if len(parts) == 2:
                credentials_part = parts[0]
                host_part = parts[1]
                
                # Split credentials by : to get user and password
                # Use split with maxsplit=1 to handle passwords that contain :
                cred_parts = credentials_part.split(':', 1)
                
                if len(cred_parts) == 2:
                    user = cred_parts[0]
                    password = cred_parts[1]
                    
                    # URL-encode password
                    encoded_password = quote_plus(password, safe='')
                    
                    # Reconstruct URL
                    database_url = "postgresql://{}:{}@{}".format(user, encoded_password, host_part)
                    
                    print("Successfully encoded DATABASE_URL password")
    except Exception as e:
        print("Warning: Could not parse DATABASE_URL, using as-is: {}".format(e))
    
    engine = create_engine(database_url, echo=False)
    Base.metadata.create_all(engine)
    return engine

def get_session(engine):
    """Create a new database session"""
    Session = sessionmaker(bind=engine)
    return Session()