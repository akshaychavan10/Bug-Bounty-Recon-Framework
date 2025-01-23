import time
import json
import os
from googlesearch import search

def find_install_setup_files(target_domain):
    """
    Perform Google Dork queries to find installation or setup files.
    Save the results in a structured format (JSON) inside `outputs/target_domain/install_setup_files.json`.
    """
    queries = [
        f'site:{target_domain} inurl:"install.php"',
        f'site:{target_domain} inurl:"setup.php"',
        f'site:{target_domain} inurl:"install/index.php"',
        f'site:{target_domain} inurl:"setup/config.php"',
        f'site:{target_domain} intext:"Installation Wizard"'
    ]

    num_results = 20
    delay_time = 3
    output_dir = f"outputs/{target_domain}"
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{output_dir}/install_setup_files.json"

    print(f"Running {len(queries)} queries for target: {target_domain} with a {delay_time}-second delay between each query...")

    results = []
    for query in queries:
        query_results = {"query": query, "results": []}
        print(f"Searching for: {query}")
        try:
            for result in search(query, num_results=num_results):
                print(result)
                query_results["results"].append(result)
        except Exception as e:
            print(f"Error with query '{query}': {e}")
        results.append(query_results)
        time.sleep(delay_time)

    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    print(f"Results saved to {output_file}")
    return output_file