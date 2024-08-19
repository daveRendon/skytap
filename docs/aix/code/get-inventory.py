import requests
from requests.auth import HTTPBasicAuth
import json

# Your Skytap "Login name" from the Skytap Portal and API token
login_name='your-login-name-here'
API_token='your-api-token-here'

base_url = 'https://cloud.skytap.com/'
auth_sky = (login_name,API_token)
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Replace with your specific environment (configuration) ID
environment_id = 'your-environment-id-here'

# Skytap API endpoint to get the environment details
url = f'https://cloud.skytap.com/v2/configurations/{environment_id}'


response = requests.get(url, headers=headers,auth=auth_sky)

# Check if the request was successful
if response.status_code == 200:
    environment_data = response.json()
    print('Environment Details:')
    print(environment_data)
    
    # Extract the VMs (LPARs) from the environment data
    vms = environment_data.get('vms', [])
    
    print('\nLPAR Inventory:')
    for vm in vms:
        print(f"VM ID: {vm.get('id', 'N/A')}")
        print(f"Name: {vm.get('name', 'N/A')}")
        print(f"Status: {vm.get('runstate', 'N/A')}")
        print(f"OS: {vm.get('operating_system', 'N/A')}")
        print(f"CPUs: {vm.get('vcpus', 'N/A')}")
        print(f"Memory: {vm.get('memory', 'N/A')} MB")
        print('---')
else:
    print('Failed to retrieve environment details')
    print('Status Code:', response.status_code)
    print('Response:', response.text)