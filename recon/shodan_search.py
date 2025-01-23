import shodan

def search_shodan(domain, api_key):
    """
    Search Shodan for domain information.
    """
    try:
        api = shodan.Shodan(api_key)
        results = api.search(domain)
        return results
    except Exception as e:
        print(f"Error searching Shodan: {e}")
        return None