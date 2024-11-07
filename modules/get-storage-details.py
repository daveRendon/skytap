import requests
from requests.auth import HTTPBasicAuth

# Your Skytap "Login name" from the Skytap Portal and API token
login_name = 'your_login_name'
API_token = 'your_API_token'

base_url = 'https://cloud.skytap.com'
auth_sky = (login_name, API_token)
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Replace with your specific environment (configuration) ID
ENVIRONMENT_ID = '159726802'

# Skytap API endpoint to get the environment details
url = f'{base_url}/v2/configurations/{ENVIRONMENT_ID}'

def get_environment(environment_id):
    """
    Retrieve the details of the specified environment.
    """
    response = requests.get(url, headers=headers, auth=auth_sky)
    response.raise_for_status()
    return response.json()

def get_vms_in_environment(environment):
    """
    Retrieve VMs (LPARs) in the specified environment.
    """
    return environment.get('vms', [])

def get_disks_for_vm(vm_data):
    """
    Retrieve disks associated with the specified VM.
    """
    return vm_data.get('hardware', {}).get('disks', [])

def get_multi_attach_storage(environment):
    """
    Retrieve multi-attach storage configuration from the environment.
    """
    return environment.get('multi_attach_storage_groups', [])

def main():
    try:
        # Retrieve environment details
        environment = get_environment(ENVIRONMENT_ID)
        print(f"Environment ID: {environment['id']}")
        print(f"Environment Name: {environment['name']}")
        
        # Retrieve VMs (LPARs) in the environment
        vms = get_vms_in_environment(environment)
        if not vms:
            print("No VMs found in the environment.")
            return

        for vm in vms:
            print(f"\nVM ID: {vm['id']}")
            print(f"VM Name: {vm['name']}")
            
            # Retrieve disks for each VM
            disks = get_disks_for_vm(vm)
            if disks:
                for disk in disks:
                    print(f"  Disk ID: {disk['id']}, Size: {disk['size']} GB, Type: {disk['type']}")
            else:
                print("  No disks found for this VM.")
            
            # Display network interface details
            for interface in vm.get('interfaces', []):
                print(f"  Interface ID: {interface['id']}, IP: {interface['ip']}, Hostname: {interface['hostname']}")

        # Retrieve and print multi-attach storage configurations in the specified format
        multi_attach_storage = get_multi_attach_storage(environment)
        if multi_attach_storage:
            print("\nMulti-Attach Storage:")
            for storage in multi_attach_storage:
                print(f"  Storage Group ID: {storage['id']}, Name: {storage['name']}, Configuration ID: {storage['configuration_id']}")
                for allocation in storage.get('storage_allocations', []):
                    print(f"    Allocation ID: {allocation['id']}, Size: {allocation['size']} MB")
                    for attachment in allocation.get('disk_attachments', []):
                        # Check for 'vm_key' and other fields to avoid missing key errors
                        bus_type = attachment.get('bus_type', 'N/A')
                        bus_id = attachment.get('bus_id', 'N/A')
                        lun = attachment.get('lun', 'N/A')
                        vm_key = attachment.get('vm_key', 'N/A')
                        print(f"      Bus Type: {bus_type}, Bus ID: {bus_id}, LUN: {lun}, VM Key: {vm_key}")
        else:
            print("No multi-attach storage configurations found.")
            
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    main()
