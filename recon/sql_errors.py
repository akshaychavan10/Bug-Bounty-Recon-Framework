import time
import json
import os
from googlesearch import search

def find_sql_errors(target_domain):
    """
    Perform Google Dork queries to find SQL error messages.
    Save the results in a structured format (JSON) inside `outputs/target_domain/sql_errors.json`.
    """
    # Define Google Dork queries with the target domain
    queries = [
        f'site:{target_domain} intext:"SQL syntax"',
        f'site:{target_domain} intext:"mysql_fetch_array"',
        f'site:{target_domain} intext:"mysql_fetch_assoc"',
        f'site:{target_domain} intext:"mysql_num_rows"',
        f'site:{target_domain} intext:"You have an error in your SQL syntax"',
        f'site:{target_domain} intext:"Warning: mysql_query()"',
        f'site:{target_domain} intext:"Uncaught mysqli_sql_exception"'
    ]

    # Limit the number of results per query
    num_results = 20

    # Delay time (in seconds) between queries
    delay_time = 3

    # Create the output directory for the target domain
    output_dir = f"outputs/{target_domain}"
    os.makedirs(output_dir, exist_ok=True)

    # Output file path
    output_file = f"{output_dir}/sql_errors.json"

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