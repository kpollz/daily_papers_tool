"""
LangGraph state schema for the daily digest workflow.
"""
from typing import Annotated, TypedDict
import operator


class DigestState(TypedDict):
    """Shared state for the digest graph workflow."""
    date_str: str
    papers: list[dict]
    papers_to_process: list[dict]
    summaries: Annotated[list[dict], operator.add]
    failed_papers: list[dict]
    final_report: str
    report_path: str
    model_name: str
    retry_count: int
