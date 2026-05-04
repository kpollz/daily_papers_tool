"""
LangGraph builder and conditional edge logic for the daily digest workflow.
"""
import os
from dotenv import load_dotenv

load_dotenv(override=False)

from langgraph.graph import StateGraph, END
from langgraph.types import Send

from graph.state import DigestState
from graph.nodes import (
    fetch_papers_node,
    download_pdfs_node,
    filter_duplicates_node,
    extract_text_node,
    summarize_worker_node,
    summarize_sequential_node,
    quality_gate_node,
    save_to_db_node,
    generate_report_node,
    upload_minio_node,
    cleanup_node,
    retry_failed_node,
)


def after_fetch(state: DigestState) -> str:
    """Conditional edge after fetch: skip entirely if no papers found."""
    if not state.get("papers"):
        return END
    return "download"


def after_filter_dup(state: DigestState) -> str:
    """Conditional edge after filter: skip to report if nothing left to process."""
    if not state.get("papers_to_process"):
        return "generate_report"
    return "extract"


def dispatch_summarization(state: DigestState):
    """
    Map phase: dispatch one parallel worker per paper.
    Returns list of Send objects.
    """
    papers = state.get("papers_to_process", [])
    if not papers:
        return []

    limit = int(os.getenv("MAX_PAPERS_PER_BATCH", 5))
    if len(papers) > limit:
        print(f"Warning: {len(papers)} papers exceed batch limit ({limit}). Processing first {limit} only.")
        papers = papers[:limit]

    print(f"Dispatching {len(papers)} parallel summarization tasks")
    return [Send("summarize_worker", {"paper": p}) for p in papers]


def after_quality_gate(state: DigestState) -> str:
    """Conditional edge after quality gate: retry or proceed."""
    failed = state.get("failed_papers", [])
    retry_count = state.get("retry_count", 0)
    max_retries = int(os.getenv("SUMMARY_MAX_RETRIES", 2))

    if len(failed) > 0 and retry_count < max_retries:
        return "retry"
    return "save_db"


def build_digest_graph():
    """Build and compile the digest workflow graph."""
    workflow = StateGraph(DigestState)

    # Register all nodes
    workflow.add_node("fetch", fetch_papers_node)
    workflow.add_node("download", download_pdfs_node)
    workflow.add_node("filter_dup", filter_duplicates_node)
    workflow.add_node("extract", extract_text_node)
    workflow.add_node("summarize_worker", summarize_worker_node)
    workflow.add_node("summarize_sequential", summarize_sequential_node)
    workflow.add_node("quality_gate", quality_gate_node)
    workflow.add_node("retry", retry_failed_node)
    workflow.add_node("save_db", save_to_db_node)
    workflow.add_node("generate_report", generate_report_node)
    workflow.add_node("upload_minio", upload_minio_node)
    workflow.add_node("cleanup", cleanup_node)

    # Wire edges
    workflow.set_entry_point("fetch")

    workflow.add_conditional_edges(
        "fetch",
        after_fetch,
        {
            END: END,
            "download": "download",
        },
    )

    workflow.add_edge("download", "filter_dup")

    workflow.add_conditional_edges(
        "filter_dup",
        after_filter_dup,
        {
            "generate_report": "generate_report",
            "extract": "extract",
        },
    )

    # Choose between sequential (batch=1) and parallel (batch>1) processing
    batch_limit = int(os.getenv("MAX_PAPERS_PER_BATCH", 1))
    if batch_limit <= 1:
        # Sequential: process all papers one-by-one
        workflow.add_edge("extract", "summarize_sequential")
        workflow.add_edge("summarize_sequential", "quality_gate")
    else:
        # Parallel: dispatch multiple workers
        workflow.add_conditional_edges(
            "extract",
            dispatch_summarization,
            ["summarize_worker"],
        )
        workflow.add_edge("summarize_worker", "quality_gate")

    workflow.add_conditional_edges(
        "quality_gate",
        after_quality_gate,
        {
            "retry": "retry",
            "save_db": "save_db",
        },
    )

    workflow.add_edge("retry", "quality_gate")
    workflow.add_edge("save_db", "generate_report")
    workflow.add_edge("generate_report", "upload_minio")
    workflow.add_edge("upload_minio", "cleanup")
    workflow.add_edge("cleanup", END)

    return workflow.compile()
