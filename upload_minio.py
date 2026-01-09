import os
from dotenv import load_dotenv
from minio import Minio
from minio.error import S3Error
from urllib.parse import urlparse

# Load environment variables
load_dotenv()


def upload_to_minio(file_path, object_name):
    """Uploads a file to MinIO server.
    
    Args:
        file_path (str): Local path to the file to upload
        object_name (str): Object name/path in MinIO bucket (e.g., 'summaries/file.md')
    
    Returns:
        bool: True if upload was successful, False otherwise
    
    Environment variables required:
        MINIO_ACCESS_KEY: MinIO access key
        MINIO_SECRET_KEY: MinIO secret key
        MINIO_ENDPOINT: MinIO server endpoint (default: 'minio.smartsolar.io.vn')
        MINIO_BUCKET: MinIO bucket name (default: 'dtung.vu')
        MINIO_SECURE: Use HTTPS (default: 'true')
    """
    try:
        # Get credentials from environment variables
        minio_endpoint = os.getenv('MINIO_ENDPOINT', 'minio.smartsolar.io.vn')
        minio_access_key = os.getenv('MINIO_ACCESS_KEY')
        minio_secret_key = os.getenv('MINIO_SECRET_KEY')
        minio_bucket = os.getenv('MINIO_BUCKET', 'dtung.vu')
        minio_secure = os.getenv('MINIO_SECURE', 'true').lower() == 'true'
        
        if not minio_access_key or not minio_secret_key:
            print("Warning: MINIO_ACCESS_KEY or MINIO_SECRET_KEY not found in .env file. Skipping MinIO upload.")
            return False
        
        # Parse endpoint to remove protocol (if provided)
        if minio_endpoint.startswith('http://') or minio_endpoint.startswith('https://'):
            parsed_endpoint = urlparse(minio_endpoint)
            endpoint_host = parsed_endpoint.netloc
        else:
            endpoint_host = minio_endpoint
        
        # Initialize MinIO client
        client = Minio(
            endpoint_host,
            access_key=minio_access_key,
            secret_key=minio_secret_key,
            secure=minio_secure
        )
        
        # Ensure bucket exists
        found = client.bucket_exists(minio_bucket)
        if not found:
            client.make_bucket(minio_bucket)
            print(f"Created bucket: {minio_bucket}")
        
        # Upload the file
        client.fput_object(
            minio_bucket,
            object_name,
            file_path
        )
        
        print(f"Successfully uploaded {file_path} to MinIO: {minio_bucket}/{object_name}")
        return True
        
    except S3Error as e:
        print(f"MinIO S3Error: {e}")
        return False
    except Exception as e:
        print(f"Error uploading to MinIO: {e}")
        return False

