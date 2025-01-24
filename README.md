# Bug Bounty Reconnaissance Automation Framework

## Overview
The **Bug Bounty Recon Framework** is a Python-based reconnaissance tool designed to automate and streamline the information-gathering phase of bug bounty programs. It integrates multiple reconnaissance techniques and tools to identify vulnerabilities, misconfigurations, and sensitive information across target domains. The framework is modular, extensible, and suitable for both beginners and experienced security researchers.

---

## Features
The framework supports the following reconnaissance tasks:

1. **Subdomain Enumeration**:
   - Identify subdomains using `crt.sh` and other techniques.

2. **File Discovery**:
   - Locate sensitive files such as:
     - Apache configuration files
     - Database files
     - Backup files
     - Log files
     - `robots.txt`
     - `htaccess` files
     - Publicly exposed documents

3. **Technology Detection**:
   - Detect content management systems (CMS) and frameworks.
   - Identify WordPress installations.

4. **Vulnerability Discovery**:
   - Search for open redirects.
   - Detect Apache Struts RCE vulnerabilities.
   - Identify backdoors and misconfigurations.

5. **Third-Party Exposure**:
   - Check for third-party service exposures.
   - Search for sensitive data on Pastebin and GitHub.

6. **Port Scanning**:
   - Perform Nmap scans to identify open ports and services.

7. **Web Application Reconnaissance**:
   - Enumerate login pages.
   - Check for directory listing vulnerabilities.
   - Analyze security headers.

8. **Cloud and S3 Bucket Discovery**:
   - Identify exposed AWS S3 buckets.
   - Search for Bitbucket pipelines and Atlassian products (Jira, Confluence).

9. **Historical Data Analysis**:
   - Query the Wayback Machine for historical snapshots of the target.

10. **Whois Lookup**:
    - Retrieve domain registration details.

---

## Getting Started

### Prerequisites
- Python 3.8 or later
- Pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/akshaychavan10/Bug-Bounty-Recon-Framework.git
   cd Bug-Bounty-Recon-Framework
   ```

2. Set up a virtual environment (recommended):
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the target domains in `config.json`:
   ```json
   {
       "targets": ["example.com", "anotherdomain.com"]
   }
   ```

---

## Usage

### Command-Line Interface (CLI)
Run the framework from the command line:
```bash
python3 main.py
```

### Web Application
The framework includes a Flask-based web interface for interactive use:
```bash
python3 web_app.py
```
- Access the web interface at `http://127.0.0.1:5000`.
- Add targets, run reconnaissance tasks, and view results in a user-friendly format.

### Output
All results are saved in the `output` directory, organized by target domain. Reports are generated in JSON format for further analysis.

---

## Directory Structure

```
Bug-Bounty-Recon-Framework/
│
├── database/                  # Database scripts for storing results
│   └── db_handler.py
│
├── outputs/                   # Reconnaissance results for each target
│   └── target_domain/
│       ├── subdomain_crt.json
│       ├── log_files.json
│       ├── s3_buckets.json
│       └── bitbucket_atlassian.json
│
├── recon/                     # Reconnaissance scripts
│   ├── subdomain_enumeration.py
│   ├── log_files.py
│   ├── s3_buckets.py
│   ├── bitbucket_atlassian.py
│   └── ... (other scripts)
│
├── templates/                 # Flask HTML templates
│   ├── index.html
│   └── target_details.html
│
├── utils/                     # Utility scripts
│   └── buttons.py
│
├── config.json                # Configuration file for target domains
├── main.py                    # Main CLI script
├── web_app.py                 # Flask web application
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---
## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---
## Contact
For questions or feedback, please contact:
- [GitHub](https://github.com/akshaychavan10) 
- [LinkedIn](https://www.linkedin.com/in/akshaychavan07/) 

---

This framework is designed to simplify and accelerate the reconnaissance process for bug bounty hunters. Happy hunting! 🐛🔍

---
