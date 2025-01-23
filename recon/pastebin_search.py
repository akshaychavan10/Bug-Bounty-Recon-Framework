import requests

def search_pastebin(domain):
    """
    Search Pastebin for entries related to the domain.
    """
    try:
        # Example API call (replace with actual Pastebin API or scraping logic)
        response = requests.get(f"https://pastebin.com/search?q={domain}")
        if domain in response.text:
            return True
        return False
    except Exception as e:
        print(f"Error searching Pastebin: {e}")
        return False