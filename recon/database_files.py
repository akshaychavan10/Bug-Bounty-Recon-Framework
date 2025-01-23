import time
import json
import os
from googlesearch import search

def find_database_files(target_domain):
    """
    Perform Google Dork queries to find database-related files.
    Save the results in a structured format (JSON) inside `outputs/target_domain/database_files.json`.
    """
    # Define Google Dork queries with the target domain
    queries = [
        f'site:{target_domain} intitle:"index of" "db_config.php"',
        f'site:{target_domain} intitle:"index of" "database.yml"',
        f'site:{target_domain} intitle:"index of" "db_connection.ini"',
        f'site:{target_domain} intitle:"index of" "database.json"',
        f'site:{target_domain} intitle:"index of" "db_backup.sql"',
        f'site:{target_domain} intitle:"index of" "mysql.cnf"',
        f'site:{target_domain} intitle:"index of" "pg_hba.conf"',
        f'site:{target_domain} intitle:"index of" "mariadb.conf"',
        f'site:{target_domain} intitle:"index of" "sqlite.db"',
        f'site:{target_domain} intitle:"index of" "sqlbackup.bak"',
        f'site:{target_domain} intitle:"index of" "db_schema.sql"',
        f'site:{target_domain} intitle:"index of" "oracle.conf"',
        f'site:{target_domain} intitle:"index of" "db_settings.php"',
        f'site:{target_domain} intitle:"index of" "connection.php"',
        f'site:{target_domain} intitle:"index of" "database_credentials.txt"'
    ]

    # Limit the number of results per query
    num_results = 20

    # Delay time (in seconds) between queries
    delay_time = 3

    # Create the output directory for the target domain
    output_dir = f"outputs/{target_domain}"
    os.makedirs(output_dir, exist_ok=True)

    # Output file path
    output_file = f"{output_dir}/database_files.json"

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