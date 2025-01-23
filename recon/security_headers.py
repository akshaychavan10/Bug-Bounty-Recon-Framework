import requests

def check_security_headers(url):
    """
    Check for security headers on a given URL.
    """
    try:
        response = requests.get(url)
        headers = response.headers
        security_headers = {
            "Content-Security-Policy": headers.get("Content-Security-Policy"),
            "Strict-Transport-Security": headers.get("Strict-Transport-Security"),
            "X-Content-Type-Options": headers.get("X-Content-Type-Options"),
            "X-Frame-Options": headers.get("X-Frame-Options"),
            "X-XSS-Protection": headers.get("X-XSS-Protection"),
        }
        return security_headers
    except Exception as e:
        print(f"Error checking security headers: {e}")
        return None