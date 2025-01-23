# recon/subdomain_enumeration.py
import requests
import json
import os

def query_crtsh(domain):
    """
    Query crt.sh for subdomains of the given domain.
    """
    url = f"https://crt.sh/?q={domain}&output=json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error querying crt.sh: {e}")
        return None

def save_subdomains_to_json(domain, subdomains, output_dir="outputs"):
    """
    Save subdomains to a JSON file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    domain_dir = os.path.join(output_dir, domain)
    if not os.path.exists(domain_dir):
        os.makedirs(domain_dir)

    output_file = os.path.join(domain_dir, "subdomain_crt.json")
    with open(output_file, "w") as f:
        json.dump(subdomains, f, indent=4)
    print(f"Subdomains saved to {output_file}")

def get_unique_subdomains(subdomains):
    """
    Extract unique subdomains from the crt.sh JSON response.
    """
    unique_subdomains = set()
    for entry in subdomains:
        name_value = entry.get("name_value", "")
        if name_value:
            # Split and clean subdomains (e.g., handle multiple subdomains in one entry)
            for subdomain in name_value.split("\n"):
                subdomain = subdomain.strip().lower()
                if subdomain:
                    unique_subdomains.add(subdomain)
    return sorted(unique_subdomains)

def enumerate_subdomains(domain):
    """
    Main function to enumerate subdomains and save results.
    """
    print(f"Enumerating subdomains for: {domain}")
    subdomains = query_crtsh(domain)
    if subdomains:
        unique_subdomains = get_unique_subdomains(subdomains)
        save_subdomains_to_json(domain, unique_subdomains)
        return unique_subdomains
    return []

