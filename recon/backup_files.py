import time
import json
import os
from googlesearch import search

def find_backup_files(target_domain):
    """
    Perform Google Dork queries to find backup files.
    Save the results in a structured format (JSON) inside `outputs/target_domain/backup_files.json`.
    """
    # Define Google Dork queries with the target domain
    queries = [
        f'site:{target_domain} intitle:"index of" "backup"',
        f'site:{target_domain} intitle:"index of" "old"',
        f'site:{target_domain} filetype:bak inurl:"backup"',
        f'site:{target_domain} filetype:zip inurl:"backup"',
        f'site:{target_domain} filetype:sql inurl:"backup"',
        f'site:{target_domain} inurl:"backup" intext:"backup"',
        f'site:{target_domain} inurl:"old" intext:"old"'
    ]

    # Limit the number of results per query
    num_results = 20

    # Delay time (in seconds) between queries
    delay_time = 3

    # Create the output directory for the target domain
    output_dir = f"outputs/{target_domain}"
    os.makedirs(output_dir, exist_ok=True)

    # Output file path
    output_file = f"{output_dir}/backup_files.json"

    print(f"Running {len(queries)} queries for target: {target_domain} with a {delay_time}-second delay between each query...")

    # Perform the search and save results
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
        # Add delay between queries
        time.sleep(delay_time)

    # Save results to a JSON file
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    print(f"Results saved to {output_file}")
    return output_file