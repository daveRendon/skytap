import requests
from requests.auth import HTTPBasicAuth
import json

# Your Skytap "Login name" from the Skytap Portal and API token
login_name='your-login-name'
API_token='your-api-token'

base_url = 'https://cloud.skytap.com/'
auth_sky = (login_name,API_token)
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Replace with your specific environment (configuration) ID
environment_id = 'your-environment-id'

# Skytap API endpoint to get the environment details
url = f'https://cloud.skytap.com/v2/configurations/{environment_id}'

response = requests.get(url, headers=headers,auth=auth_sky)

# Check if the request was successful
if response.status_code == 200:
    environment_data = response.json()
    print('Environment Details:')
    # Pretty print the entire environment data for debugging
    # print(json.dumps(environment_data, indent=2))  
    
    # Extract the VMs (LPARs) from the environment data
    vms = environment_data.get('vms', [])
    
    # Initialize markdown table
    markdown_table = "| VM ID            | Name               | Status     | OS                  | vCPUs | Memory (GB) |\n"
    markdown_table += "|------------------|--------------------|------------|---------------------|-------|-------------|\n"
    
    for vm in vms:
        vm_id = vm.get('id', 'N/A')
        name = vm.get('name', 'N/A')
        status = vm.get('runstate', 'N/A')
        
        hardware = vm.get('hardware', {})
        settings = hardware.get('settings', {})
        
        os = hardware.get('guestOS', 'N/A')
        vcpus = settings.get('cpus', {}).get('current', 'N/A')
        memory_mb = settings.get('ram', {}).get('current', 'N/A')
        
        # Convert memory from MB to GB
        memory_gb = memory_mb / 1024 if memory_mb != 'N/A' else 'N/A'
        
        # Append row to markdown table
        markdown_table += f"| {vm_id:<16} | {name:<18} | {status:<10} | {os:<19} | {vcpus:<5} | {memory_gb:<11} |\n"
    
    # Print the markdown table
    print(markdown_table)
else:
    print('Failed to retrieve environment details')
    print('Status Code:', response.status_code)
    print('Response:', response.text)