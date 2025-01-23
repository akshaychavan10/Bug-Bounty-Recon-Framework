import requests

def check_censys(domain):
    """
    Check Censys for domain information.
    """
    try:
        # Example API call (replace with actual Censys API key)
        response = requests.get(f"https://search.censys.io/api/v2/hosts/{domain}")
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print(f"Error checking Censys: {e}")
        return None