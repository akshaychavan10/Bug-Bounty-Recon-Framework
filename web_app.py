from flask import Flask, render_template
import sqlite3
import json
import os

app = Flask(__name__)

# Database file path
DATABASE = 'database/recon_data.db'

def get_db_connection():
    """
    Establish a connection to the SQLite database.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn

@app.route('/')
def index():
    """
    Display the list of targets.
    """
    conn = get_db_connection()
    
    # Fetch all targets
    targets = conn.execute('SELECT * FROM targets').fetchall()
    
    conn.close()
    
    # Render the HTML template with the list of targets
    return render_template('index.html', targets=targets)

@app.route('/target/<target_name>')
def target_details(target_name):
    """
    Display detailed information for a specific target.
    Dynamically load all JSON files in the target's output directory.
    """
    conn = get_db_connection()
    
    # Fetch Nmap scan results for the target
    target = conn.execute('SELECT * FROM targets WHERE target_name = ?', (target_name,)).fetchone()
    if target:
        target_id = target['id']
        nmap_results = conn.execute('SELECT * FROM recon_results WHERE target_id = ?', (target_id,)).fetchall()
    else:
        nmap_results = []
    
    conn.close()

    # Load all JSON files in the target's output directory
    output_dir = f"outputs/{target_name}"
    results = {}
    if os.path.exists(output_dir):
        for filename in os.listdir(output_dir):
            if filename.endswith(".json"):
                with open(f"{output_dir}/{filename}", "r") as f:
                    try:
                        data = json.load(f)
                        results[filename.replace(".json", "")] = data
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON from {filename}")
                        results[filename.replace(".json", "")] = None

    # Debug: Print the results dictionary
    print("Results:", results)

    # Render the HTML template with the target details
    return render_template(
        'target_details.html',
        target_name=target_name,
        nmap_results=nmap_results,
        results=results
    )

if __name__ == '__main__':
    app.run(debug=True)