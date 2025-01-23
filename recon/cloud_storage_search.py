import requests

def search_cloud_storage(domain):
    """
    Search for exposed cloud storage buckets.
    """
    try:
        # Example: Check for S3 buckets
        response = requests.get(f"http://{domain}.s3.amazonaws.com")
        if response.status_code == 200:
            return True
        return False
    except Exception as e:
        print(f"Error searching cloud storage: {e}")
        return False