import requests

def detect_cms(url):
    """
    Detect the CMS used by a website.
    """
    try:
        response = requests.get(url)
        if "wp-content" in response.text:
            return "WordPress"
        elif "Joomla" in response.text:
            return "Joomla"
        elif "Drupal" in response.text:
            return "Drupal"
        return "Unknown"
    except Exception as e:
        print(f"Error detecting CMS: {e}")
        return None