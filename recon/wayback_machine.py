import requests

def search_wayback_machine(domain):
    """
    Search the Wayback Machine for historical data.
    """
    try:
        response = requests.get(f"http://archive.org/wayback/available?url={domain}")
        data = response.json()
        if data['archived_snapshots']:
            return data['archived_snapshots']['closest']['url']
        return None
    except Exception as e:
        print(f"Error searching Wayback Machine: {e}")
        return None