"""
LangGraph state schema for the daily digest workflow.
"""
from typing import Annotated, TypedDict


def summaries_reducer(existing: list[dict], new: list[dict]) -> list[dict]:
    """
    Custom reducer for summaries field.
    
    - Parallel workers APPEND new summaries (new paper IDs not in existing).
    - Quality gate / retry REPLACE the list (new IDs are subset of existing).
    - Empty new list clears the field (e.g. all summaries failed quality gate).
    """
    if not existing:
        return new or []
    if not new:
        return []
    
    new_ids = {s.get("paper", {}).get("id") for s in new}
    existing_ids = {s.get("paper", {}).get("id") for s in existing}
    
    # If new is a subset of existing → this is a filter/replacement operation
    if new_ids.issubset(existing_ids):
        return new
    
    # Otherwise → workers appending new summaries
    return existing + new


class DigestState(TypedDict):
    """Shared state for the digest graph workflow."""
    date_str: str
    papers: list[dict]
    papers_to_process: list[dict]
    summaries: Annotated[list[dict], summaries_reducer]
    failed_papers: list[dict]
    final_report: str
    report_path: str
    model_name: str
    retry_count: int
    paper_limit: int
    force_update: bool
