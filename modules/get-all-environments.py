import requests
from requests.auth import HTTPBasicAuth

# Your Skytap login name and API token
login_name = 'your_login_name'  # Replace with actual Skytap login name
API_token = 'your_API_token'  # Replace with actual Skytap API token

# Base URL and authentication
base_url = 'https://cloud.skytap.com'
auth = HTTPBasicAuth(login_name, API_token)
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

def get_user_info():
    """
    Retrieves customer ID and account ID for the current user.
    """
    url = f"{base_url}/v2/users"
    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        user_info_list = response.json()
        if isinstance(user_info_list, list) and user_info_list:
            user_info = user_info_list[0]
            customer_id = user_info.get('customer_id')
            account_id = user_info.get('account_id')
            
            print(f"Customer ID: {customer_id}")
            print(f"Account ID: {account_id}")
            
            return customer_id, account_id
        else:
            print("No user information available.")
            return None, None
    else:
        print(f"Failed to retrieve user information. Status code: {response.status_code}")
        return None, None

def get_all_environments():
    """
    Retrieves all environments in the account.
    """
    url = f"{base_url}/v2/configurations"
    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve environments. Status code: {response.status_code}")
        return []

def get_vms_in_environment(environment_id):
    """
    Retrieves all VMs in a specific environment.
    """
    url = f"{base_url}/v2/configurations/{environment_id}/vms"
    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve VMs for Environment ID {environment_id}. Status code: {response.status_code}")
        return []

def summarize_environments(environments):
    """
    Provides a summary of each environment in a Markdown table format with aligned columns
    and displays totals for VM counts, RAM, and storage.
    """
    summary = []
    # Initialize totals
    total_power_vm_count = 0
    total_x86_vm_count = 0
    total_power_ram = 0
    total_x86_ram = 0
    total_storage_tb = 0

    # Prepare the Markdown table headers
    headers = [
        "Environment ID", "Environment Name", "Power VM Count",
        "x86 VM Count", "Power RAM (GB)", "x86 RAM (GB)", "Total Storage (TB)"
    ]
    
    # Calculate the maximum width for each column
    column_widths = {header: len(header) for header in headers}
    
    for env in environments:
        environment_id = str(env['id'])
        environment_name = env.get('name', 'Unnamed Environment')

        # Retrieve VM details for this environment
        vms = get_vms_in_environment(environment_id)

        power_vm_count = 0
        x86_vm_count = 0
        power_ram_total = 0
        x86_ram_total = 0
        storage_total_tb = 0

        for vm in vms:
            architecture = vm['hardware'].get('architecture', 'unknown')
            ram_gb = vm['hardware'].get('ram', 0) / 1024  # Convert MB to GB
            storage_gb = vm['hardware'].get('storage', 0) / 1024  # Convert MB to GB

            # Accumulate totals based on architecture type
            if architecture == 'power':
                power_vm_count += 1
                power_ram_total += ram_gb
            elif architecture == 'x86':
                x86_vm_count += 1
                x86_ram_total += ram_gb

            # Add to total storage in TB
            storage_total_tb += storage_gb / 1024  # Convert GB to TB

        # Update grand totals
        total_power_vm_count += power_vm_count
        total_x86_vm_count += x86_vm_count
        total_power_ram += power_ram_total
        total_x86_ram += x86_ram_total
        total_storage_tb += storage_total_tb

        # Record each row of data
        row_data = {
            "Environment ID": environment_id,
            "Environment Name": environment_name,
            "Power VM Count": str(power_vm_count),
            "x86 VM Count": str(x86_vm_count),
            "Power RAM (GB)": f"{power_ram_total:.2f}",
            "x86 RAM (GB)": f"{x86_ram_total:.2f}",
            "Total Storage (TB)": f"{storage_total_tb:.2f}"
        }

        # Update maximum width for each column based on the current row
        for key, value in row_data.items():
            column_widths[key] = max(column_widths[key], len(value))
        
        # Add row data to summary
        summary.append(row_data)

    # Print the Markdown table
    def format_row(row):
        return " | ".join(f"{row[header]:<{column_widths[header]}}" for header in headers)
    
    # Print table header and separator
    header_row = format_row({header: header for header in headers})
    separator_row = " | ".join("-" * column_widths[header] for header in headers)
    print(header_row)
    print(separator_row)
    
    # Print each data row
    for row in summary:
        print(format_row(row))

    # Print totals row
    total_row = {
        "Environment ID": "Total",
        "Environment Name": "",
        "Power VM Count": str(total_power_vm_count),
        "x86 VM Count": str(total_x86_vm_count),
        "Power RAM (GB)": f"{total_power_ram:.2f}",
        "x86 RAM (GB)": f"{total_x86_ram:.2f}",
        "Total Storage (TB)": f"{total_storage_tb:.2f}"
    }
    print(separator_row)
    print(format_row(total_row))

# Main Execution Flow
# Step 1: Retrieve customer ID and account ID
customer_id, account_id = get_user_info()

# Step 2: Retrieve all environments
environments = get_all_environments()

# Step 3: Summarize each environment's VM details and display the markdown table with totals
if environments:
    summarize_environments(environments)
else:
    print("No environments found or retrieved.")
