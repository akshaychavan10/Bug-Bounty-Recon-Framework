import requests

def find_wordpress(domain):
    """
    Check if a domain is running WordPress.
    """
    try:
        response = requests.get(f"http://{domain}/wp-login.php")
        if "wp-login.php" in response.url:
            return True
        return False
    except Exception as e:
        print(f"Error finding WordPress: {e}")
        return False