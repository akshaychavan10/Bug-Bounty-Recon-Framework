import subprocess
import xml.etree.ElementTree as ET

def run_nmap(domain):
    """
    Run an Nmap scan on the specified domain and return the XML output.
    """
    command = f"nmap -oX - {domain}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Nmap scan failed: {result.stderr}")
    return result.stdout

def parse_nmap_output(xml_output):
    """
    Parse the Nmap XML output and extract IP addresses and open ports.
    """
    root = ET.fromstring(xml_output)
    results = []
    for host in root.findall('host'):
        ip = host.find('address').get('addr')
        ports = []
        for port in host.findall('ports/port'):
            port_id = port.get('portid')
            service = port.find('service').get('name', 'unknown')
            ports.append(f"{port_id}/{service}")
        results.append((ip, ', '.join(ports)))
    return results