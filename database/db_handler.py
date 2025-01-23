import sqlite3

def setup_database():
    """
    Initialize the SQLite database and create the necessary tables if they don't exist.
    """
    conn = sqlite3.connect('database/recon_data.db')
    cursor = conn.cursor()
    
    # Create a table to store targets
    cursor.execute('''CREATE TABLE IF NOT EXISTS targets
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       target_name TEXT UNIQUE)''')
    
    # Create a table to store recon results for each target
    cursor.execute('''CREATE TABLE IF NOT EXISTS recon_results
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       target_id INTEGER,
                       ip TEXT,
                       ports TEXT,
                       FOREIGN KEY(target_id) REFERENCES targets(id))''')
    
    conn.commit()
    conn.close()

def save_target(target_name):
    """
    Save a new target to the database.
    """
    conn = sqlite3.connect('database/recon_data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO targets (target_name) VALUES (?)', (target_name,))
    conn.commit()
    conn.close()

def get_target_id(target_name):
    """
    Get the target ID for a given target name.
    """
    conn = sqlite3.connect('database/recon_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM targets WHERE target_name = ?', (target_name,))
    target_id = cursor.fetchone()
    conn.close()
    return target_id[0] if target_id else None

def save_recon_data(target_id, ip, ports):
    """
    Save reconnaissance data for a specific target.
    """
    conn = sqlite3.connect('database/recon_data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO recon_results (target_id, ip, ports) VALUES (?, ?, ?)',
                   (target_id, ip, ports))
    conn.commit()
    conn.close()

def get_previous_targets():
    """
    Fetch a list of previously scanned targets.
    """
    conn = sqlite3.connect('database/recon_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT target_name FROM targets')
    targets = cursor.fetchall()
    conn.close()
    return [target[0] for target in targets]