"""
Wiki integration utilities package.
Exports functions for downloading from MinIO, uploading to Wiki.js, and managing wiki pages.
"""

from .download_from_minio import download_from_minio, read_content_from_minio, get_minio_client, list_objects_in_minio
from .upload_to_wiki import upload_to_wiki
from .wiki_page_operations import (
    get_page_by_path,
    get_page_content,
    update_page_content,
    create_monthly_index_link,
    get_monthly_index_path
)

__all__ = [
    # MinIO operations
    'download_from_minio',
    'read_content_from_minio',
    'get_minio_client',
    'list_objects_in_minio',
    # Wiki upload operations
    'upload_to_wiki',
    # Wiki page operations
    'get_page_by_path',
    'get_page_content',
    'update_page_content',
    'create_monthly_index_link',
    'get_monthly_index_path'
]

