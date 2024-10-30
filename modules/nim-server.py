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

# Create a new environment with a NIM Server
def create_nim_server():
    environment_data = {
        "name": "New Environment with NIM Server",
        "description": "This environment contains a NIM Server.",
        "template_id": "2505083"
    }
    create_env_url = f"{base_url}configurations.json"
    response = requests.post(create_env_url, headers=headers,auth=auth_sky, data=json.dumps(environment_data))
    if response.status_code == 200 or response.status_code == 201:
        print("Successfully created the environment with a NIM Server.")
        print("Environment Details:", response.json())
    else:
        print("Failed to create the environment. Status Code:", response.status_code)
        print("Error:", response.text)


create_nim_server()