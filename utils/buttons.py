from .imports import (
    run_nmap, parse_nmap_output, check_directory_listing, search_pastebin,
    search_wayback_machine, find_wordpress, check_censys, search_github,
    search_shodan, check_security_headers, search_cloud_storage, detect_cms,
    find_configuration_files, find_database_files, find_wordpress_files,
    find_log_files, find_backup_files, find_login_pages, find_sql_errors,
    find_apache_config_files, find_robots_txt, search_domain_eye,
    find_publicly_exposed_documents, find_phpinfo, find_backdoors,
    find_install_setup_files, find_open_redirects, find_apache_struts_rce,
    find_third_party_exposure, find_htaccess_sensitive_files, enumerate_subdomains, enumerate_bitbucket_atlassian
)

def get_buttons(target_entry):
    buttons = [
        ("Nmap Scan", lambda: run_nmap(target_entry.get())),
        ("Check Directory Listing", lambda: check_directory_listing(target_entry.get())),
        ("Search Pastebin", lambda: search_pastebin(target_entry.get())),
        ("Search Wayback Machine", lambda: search_wayback_machine(target_entry.get())),
        ("Find WordPress", lambda: find_wordpress(target_entry.get())),
        ("Check Censys", lambda: check_censys(target_entry.get())),
        ("Search GitHub", lambda: search_github(target_entry.get())),
        ("Search Shodan", lambda: search_shodan(target_entry.get(), "YOUR_SHODAN_API_KEY")),
        ("Check Security Headers", lambda: check_security_headers(target_entry.get())),
        ("Search Cloud Storage", lambda: search_cloud_storage(target_entry.get())),
        ("Detect CMS", lambda: detect_cms(target_entry.get())),
        ("Find Configuration Files", lambda: find_configuration_files(target_entry.get())),
        ("Find Database Files", lambda: find_database_files(target_entry.get())),
        ("Find WordPress Files", lambda: find_wordpress_files(target_entry.get())),
        ("Find Log Files", lambda: find_log_files(target_entry.get())),
        ("Find Backup Files", lambda: find_backup_files(target_entry.get())),
        ("Find Login Pages", lambda: find_login_pages(target_entry.get())),
        ("Find SQL Errors", lambda: find_sql_errors(target_entry.get())),
        ("Find Apache Config", lambda: find_apache_config_files(target_entry.get())),
        ("Find Robots.txt", lambda: find_robots_txt(target_entry.get())),
        ("Search DomainEye", lambda: search_domain_eye(target_entry.get())),
        ("Publicly Exposed Documents", lambda: find_publicly_exposed_documents(target_entry.get())),
        # New buttons for your files
        ("Check PHPInfo", lambda: find_phpinfo(target_entry.get())),
        ("Find Backdoors", lambda: find_backdoors(target_entry.get())),
        ("Check Install/Setup Files", lambda: find_install_setup_files(target_entry.get())),
        ("Check Open Redirects", lambda: find_open_redirects(target_entry.get())),
        ("Apache Struts RCE", lambda: find_apache_struts_rce(target_entry.get())),
        ("Third-Party Exposure", lambda: find_third_party_exposure(target_entry.get())),
        ("Check .htaccess/Sensitive Files", lambda: find_htaccess_sensitive_files(target_entry.get())),
        ("Enumerate Subdomains", lambda: enumerate_subdomains(target_entry.get())),
        ("Search in Bitbucket and Atlassian", lambda: enumerate_bitbucket_atlassian(target_entry.get())),
    ]
    return buttons