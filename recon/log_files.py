import time
import json
import os
from googlesearch import search

def find_log_files(target_domain):
    """
    Perform Google Dork queries to find log files.
    Save the results in a structured format (JSON) inside `outputs/target_domain/log_files.json`.
    """
    # Define Google Dork queries with the target domain
    queries = [
        f'site:{target_domain} inurl:"/logs/"',
        f'site:{target_domain} inurl:"/log/"',
        f'site:{target_domain} inurl:"/access.log"',
        f'site:{target_domain} inurl:"/error.log"',
        f'site:{target_domain} inurl:"/debug.log"',
        f'site:{target_domain} inurl:"/server.log"',
        f'site:{target_domain} filetype:log inurl:"log"',
        f'site:{target_domain} filetype:log inurl:"logs"',
        f'site:{target_domain} inurl:"access_log"',
        f'site:{target_domain} inurl:"error_log"',
        f'site:{target_domain} inurl:"debug_log"',
        f'site:{target_domain} inurl:"ftp.log"',
        f'site:{target_domain} inurl:"auth.log"',
        f'site:{target_domain} inurl:"syslog"',
        f'site:{target_domain} intitle:"index of" "logs"',
        f'site:{target_domain} intitle:"index of" "log"',
        f'site:{target_domain} intitle:"index of" "access.log"',
        f'site:{target_domain} intitle:"index of" "error.log"',
        f'site:{target_domain} inurl:"/var/log/"',
        f'site:{target_domain} inurl:"/var/logs/"',
        f'site:{target_domain} inurl:"/var/log/apache2/"',
        f'site:{target_domain} inurl:"/var/log/nginx/"',
        f'site:{target_domain} inurl:"/var/log/mysql/"',
        f'site:{target_domain} inurl:"backup.log"',
        f'site:{target_domain} inurl:"backup_log"',
        f'site:{target_domain} inurl:"log.bak"',
        f'site:{target_domain} inurl:"log.zip"',
        f'site:{target_domain} inurl:"log.tar.gz"',
        f'site:{target_domain} inurl:"config" intext:"log_path"',
        f'site:{target_domain} inurl:"config" intext:"log_dir"',
        f'site:{target_domain} inurl:"config" intext:"logfile"',
        f'site:{target_domain} intext:"[error]" filetype:log',
        f'site:{target_domain} intext:"[warn]" filetype:log',
        f'site:{target_domain} intext:"[debug]" filetype:log',
        f'site:{target_domain} intext:"[info]" filetype:log'
    ]

    # Limit the number of results per query
    num_results = 20

    # Delay time (in seconds) between queries
    delay_time = 3

    # Create the output directory for the target domain
    output_dir = f"outputs/{target_domain}"
    os.makedirs(output_dir, exist_ok=True)

    # Output file path
    output_file = f"{output_dir}/log_files.json"

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