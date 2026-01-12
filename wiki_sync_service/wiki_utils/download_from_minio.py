import os
import tempfile
from dotenv import load_dotenv
from minio import Minio
from minio.error import S3Error
from urllib.parse import urlparse

# Load environment variables
load_dotenv()


def get_minio_client():
    """Creates and returns a MinIO client with credentials from environment variables.
    
    Returns:
        Minio: MinIO client instance or None if credentials are missing
    """
    minio_endpoint = os.getenv('MINIO_ENDPOINT', 'minio-api.smartsolar.io.vn')
    minio_port = os.getenv('MINIO_PORT', '9000')
    minio_access_key = os.getenv('MINIO_ACCESS_KEY')
    minio_secret_key = os.getenv('MINIO_SECRET_KEY')
    minio_secure = os.getenv('MINIO_SECURE', 'true').lower() == 'true'
    
    if not minio_access_key or not minio_secret_key:
        print("Error: MINIO_ACCESS_KEY or MINIO_SECRET_KEY not found in .env file.")
        return None
    
    # Parse endpoint to extract host and port
    # Logic: If using HTTPS (secure=True), don't add port (assumes reverse proxy)
    # If using HTTP (secure=False), add port if specified
    if minio_endpoint.startswith('http://') or minio_endpoint.startswith('https://'):
        parsed_endpoint = urlparse(minio_endpoint)
        endpoint_host = parsed_endpoint.hostname
        # If port is explicitly in URL, use it
        if parsed_endpoint.port:
            endpoint_port = parsed_endpoint.port
        # If using HTTPS and no port in URL, don't add port (reverse proxy)
        elif minio_secure:
            endpoint_port = None
        # If using HTTP and no port in URL, use default port
        else:
            endpoint_port = int(minio_port) if minio_port else None
    else:
        if ':' in minio_endpoint:
            endpoint_host, port_str = minio_endpoint.split(':', 1)
            endpoint_port = int(port_str)
        else:
            endpoint_host = minio_endpoint
            # If using HTTPS, don't add port (reverse proxy)
            if minio_secure:
                endpoint_port = None
            else:
                endpoint_port = int(minio_port) if minio_port else None
    
    # Build endpoint string
    if endpoint_port:
        endpoint = f"{endpoint_host}:{endpoint_port}"
    else:
        endpoint = endpoint_host
    
    try:
        print(f"Creating MinIO client with endpoint: {endpoint}")
        client = Minio(
            endpoint,
            access_key=minio_access_key,
            secret_key=minio_secret_key,
            secure=minio_secure
        )
        return client
    except Exception as e:
        print(f"Error creating MinIO client: {e}")
        return None


def download_from_minio(object_name, local_path=None, bucket_name=None):
    """Downloads a file from MinIO server.
    
    Args:
        object_name (str): Object name/path in MinIO bucket (e.g., 'summaries/daily_digest_2026-01-07.md')
        local_path (str, optional): Local path to save the file. If None, uses a temporary file.
        bucket_name (str, optional): Bucket name. If None, uses MINIO_BUCKET from .env
    
    Returns:
        str: Path to the downloaded file, or None if download failed
    """
    try:
        client = get_minio_client()
        if not client:
            return None
        
        minio_bucket = bucket_name or os.getenv('MINIO_BUCKET', 'dtung.vu')
        
        # Check if bucket exists
        if not client.bucket_exists(minio_bucket):
            print(f"Error: Bucket '{minio_bucket}' does not exist.")
            return None
        
        # Check if object exists
        try:
            client.stat_object(minio_bucket, object_name)
        except S3Error as e:
            if e.code == 'NoSuchKey':
                print(f"Error: Object '{object_name}' does not exist in bucket '{minio_bucket}'.")
                return None
            raise
        
        # Use temporary file if local_path not provided
        if local_path is None:
            # Extract filename from object_name
            filename = os.path.basename(object_name) or 'downloaded_file.md'
            temp_dir = tempfile.gettempdir()
            local_path = os.path.join(temp_dir, filename)
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(local_path) if os.path.dirname(local_path) else '.', exist_ok=True)
        
        # Download the file
        client.fget_object(minio_bucket, object_name, local_path)
        
        print(f"Successfully downloaded {object_name} from MinIO to {local_path}")
        return local_path
        
    except S3Error as e:
        print(f"MinIO S3Error: {e}")
        return None
    except Exception as e:
        print(f"Error downloading from MinIO: {e}")
        return None


def read_content_from_minio(object_name, bucket_name=None):
    """Downloads and reads the content of a file from MinIO server as a string.
    
    Args:
        object_name (str): Object name/path in MinIO bucket (e.g., 'summaries/daily_digest_2026-01-07.md')
        bucket_name (str, optional): Bucket name. If None, uses MINIO_BUCKET from .env
    
    Returns:
        str: Content of the file, or None if download/read failed
    """
    try:
        client = get_minio_client()
        if not client:
            return None
        
        minio_bucket = bucket_name or os.getenv('MINIO_BUCKET', 'dtung.vu')
        
        # Check if bucket exists
        if not client.bucket_exists(minio_bucket):
            print(f"Error: Bucket '{minio_bucket}' does not exist.")
            return None
        
        # Get object and read content
        response = client.get_object(minio_bucket, object_name)
        content = response.read().decode('utf-8')
        response.close()
        response.release_conn()
        
        print(f"Successfully read content from MinIO: {minio_bucket}/{object_name}")
        return content
        
    except S3Error as e:
        print(f"MinIO S3Error: {e}")
        return None
    except Exception as e:
        print(f"Error reading from MinIO: {e}")
        return None


def list_objects_in_minio(prefix="summaries/", bucket_name=None):
    """Lists all objects in MinIO bucket with a given prefix.
    
    Args:
        prefix (str): Prefix to filter objects (default: 'summaries/')
        bucket_name (str, optional): Bucket name. If None, uses MINIO_BUCKET from .env
    
    Returns:
        list: List of object names, or empty list if failed
    """
    try:
        client = get_minio_client()
        if not client:
            return []
        
        minio_bucket = bucket_name or os.getenv('MINIO_BUCKET', 'dtung.vu')
        
        # Check if bucket exists
        if not client.bucket_exists(minio_bucket):
            print(f"Error: Bucket '{minio_bucket}' does not exist.")
            return []
        
        # List objects
        objects = []
        for obj in client.list_objects(minio_bucket, prefix=prefix, recursive=True):
            objects.append(obj.object_name)
        
        return objects
        
    except S3Error as e:
        print(f"MinIO S3Error: {e}")
        return []
    except Exception as e:
        print(f"Error listing objects from MinIO: {e}")
        return []
