import time
import json
import os
import socket
from googlesearch import search
from github import Github

def google_dork(target, query):
    """
    Perform a Google dork search for the given target and query.
    """
    results = []
    try:
        for url in search(query, num=10, stop=10, pause=2):  # Fetch top 10 results
            results.append(url)
    except Exception as e:
        print(f"Error performing Google dork search: {e}")
    return results

def check_port(target, port):
    """
    Check if a specific port is open on the target.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Set timeout to 2 seconds
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0  # Port is open if result is 0
    except Exception as e:
        print(f"Error checking port {port} on {target}: {e}")
        return False

def github_dork(target, query):
    """
    Perform a GitHub dork search for the given target and query.
    """
    results = []
    try:
        # Initialize GitHub API (requires a GitHub token for authentication)
        github_token = "YOUR_GITHUB_TOKEN"  # Replace with your GitHub token
        g = Github(github_token)
        query = f"{query} org:{target}"
        repos = g.search_code(query)
        for repo in repos:
            results.append({
                "repository": repo.repository.full_name,
                "file": repo.path,
                "url": repo.html_url
            })
    except Exception as e:
        print(f"Error performing GitHub dork search: {e}")
    return results

def enumerate_bitbucket_atlassian(target):
    """
    Main function to enumerate Bitbucket and Atlassian-related information.
    """
    print(f"Enumerating Bitbucket and Atlassian information for: {target}")

    # Google Dorks
    dorks = [
        f'site:{target} "atlassian"',
        f'site:{target} "bitbucket"',
        f'site:{target} "jira"',
        f'site:{target} "confluence"',
        f'intitle:"Bitbucket" site:{target}',
        f'intitle:"Atlassian Jira" site:{target}',
        f'intitle:"Atlassian Confluence" site:{target}',
        f'inurl:"jira" site:{target}',
        f'inurl:"bitbucket" site:{target}'
    ]

    # Limit the number of results per query
    num_results = 10

    # Delay time (in seconds) between queries
    delay_time = 2

    # Create the output directory for the target domain
    output_dir = f"outputs/{target}"
    os.makedirs(output_dir, exist_ok=True)

    # Output file path
    output_file = f"{output_dir}/bitbucket_atlassian.json"

    print(f"Running {len(dorks)} queries for target: {target} with a {delay_time}-second delay between each query...")

    # Perform Google dork searches
    google_results = []
    for dork in dorks:
        query_results = {"query": dork, "results": []}
        print(f"Searching for: {dork}")
        try:
            for result in search(dork, num_results=num_results):
                print(result)
                query_results["results"].append(result)
        except Exception as e:
            print(f"Error with query '{dork}': {e}")
        google_results.append(query_results)
        # Add delay between queries
        time.sleep(delay_time)

    # Port Scanning
    ports = [7990, 8080]
    port_results = {}
    for port in ports:
        print(f"Checking port {port} on {target}")
        if check_port(target, port):
            port_results[port] = "Open"
        else:
            port_results[port] = "Closed"

    # GitHub Dork
    github_query = 'bitbucket-pipelines.yml'
    print(f"Performing GitHub dork: {github_query} org:{target}")
    github_results = github_dork(target, github_query)

    # Save results to JSON
    output = {
        "google_dorks": google_results,
        "port_scan": port_results,
        "github_dork": github_results
    }

    # Save to file
    with open(output_file, "w") as f:
        json.dump(output, f, indent=4)
    print(f"Results saved to {output_file}")

