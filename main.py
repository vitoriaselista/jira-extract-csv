# This script is created by Ana Vitória Selista for Jira Cloud administrative use

import requests
import csv
import codecs
import json
from config import credentials, base_url

# Split the URL by "\\" to separate the parts.
instance_name = base_url.split("//")[1].split(".")[0]

def get(url, header=None, params=None):

    # Set default empty params if not provided
    if params is None:
        params = {'': ''}

    # Set default Content-Type header if not provided
    if header is None:
        header = {'Content-Type': 'application/json'}

    # Send a GET request with the specified URL, headers, authentication, and parameters
    return requests.get(
        url,
        headers=header,
        auth=credentials,
        params=params
    )

def save_to_csv(file_name, header, data):
    with open(file_name, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        csv_writer.writerows(data)
    print(f"Data saved to {file_name}")

def get_filters():
    url = base_url + "/rest/api/2/filter/search?expand=description,owner,jql,viewUrl,searchUrl,favourite,favouritedCount,sharePermissions,editPermissions,isWritable,subscriptions"
    max_results = 1000  # Set the total number of results you want
    results = []
    start_at = 0  # Initialize the starting point for pagination

    while len(results) < max_results:
        response = get(url, params={'maxResults': 100, 'startAt': start_at}).json()

        if 'values' not in response:
            print("No data found in 'results'.")
            return

        filters = response['values']

        if not filters:
            # No more results to retrieve
            break

        results.extend(filters)
        start_at += len(filters)

    # Define the CSV file name and open it for writing.
    csv_file_name = f"{instance_name}-filters.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header row to the CSV file.
        header = ['Name', 'Description', 'Owner', 'JQL', 'View URL', 'Search URL', 'Favourite', 'Favourited Count',
                  'Share Permissions', 'Edit Permissions', 'Is Writable', 'Subscriptions']
        csv_writer.writerow(header)

        # Iterate through the filters and write their data to the CSV file.
        for filter in results:
            name = filter.get('name', '')
            description = filter.get('description', '')
            owner = filter.get('owner', {}).get('displayName', '')
            jql = filter.get('jql', '')
            view_url = filter.get('viewUrl', '')
            search_url = filter.get('searchUrl', '')
            favourite = filter.get('favourite', False)
            favourited_count = filter.get('favouritedCount', 0)
            share_permissions = filter.get('sharePermissions', [])
            edit_permissions = filter.get('editPermissions', [])
            is_writable = filter.get('isWritable', False)
            subscriptions = filter.get('subscriptions', [])

            row = [name, description, owner, jql, view_url, search_url, favourite, favourited_count, share_permissions,
                   edit_permissions, is_writable, subscriptions]
            csv_writer.writerow(row)

    print(f"Data saved to {csv_file_name}")


def get_fields():
    url = base_url + "/rest/api/2/field/search"
    max_results = 1000  # Set the total number of results you want
    results = []
    start_at = 0  # Initialize the starting point for pagination

    while len(results) < max_results:
        response = get(url, params={'maxResults': 100, 'startAt': start_at}).json()

        if 'values' not in response:
            print("No data found in 'results'.")
            return

        fields = response['values']

        if not fields:
            # No more results to retrieve
            break

        results.extend(fields)
        start_at += len(fields)

    # Define the CSV file name and open it for writing with utf-8 encoding.
    csv_file_name = f"{instance_name}-fields.csv"
    with codecs.open(csv_file_name, mode='w', encoding='utf-8', errors='ignore') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header row to the CSV file.
        header = ["id", "name", "schema.type", "schema.items", "schema.system", "description"]
        csv_writer.writerow(header)

        # Iterate through the fields and write their data to the CSV file.
        for field in results:
            id = field.get('id', '')
            name = field.get('name', '')
            schema = field.get("schema", {})
            type_schema = schema.get("type", "")
            items_schema = schema.get("items", "")
            system_schema = schema.get("system", "")
            description = field.get('description', '')

            row = [id, name, type_schema, items_schema, system_schema, description]
            csv_writer.writerow(row)

    print(f"Data saved to {csv_file_name}")

def get_resolutions():
    url = base_url + "/rest/api/2/resolution"
    max_results = 1000  # Set the total number of results you want
    results = []
    start_at = 0  # Initialize the starting point for pagination

    while len(results) < max_results:
        response = get(url, params={'maxResults': 100, 'startAt': start_at}).json()

        if not response:
            print("No data found in 'results'.")
            return

        resolutions = response  # The JSON response is already a list of resolutions

        if not resolutions:
            # No more results to retrieve
            break

        results.extend(resolutions)
        start_at += len(resolutions)

    # Define the CSV file name and open it for writing with utf-8 encoding.
    csv_file_name = f"{instance_name}-resolutions.csv"
    with codecs.open(csv_file_name, mode='w', encoding='utf-8', errors='ignore') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header row to the CSV file.
        header = ["self", "id", "description", "name"]
        csv_writer.writerow(header)

        # Write the data from the JSON result to the CSV file.
        for resolution in results:
            self = resolution.get("self", ""),
            id = resolution.get("id", ""),
            description = resolution.get("description", ""),
            name = resolution.get("name", "")

            row = [self, name, id, description]
            csv_writer.writerow(row)

    print(f"Data saved to {csv_file_name}")

def get_global_permissions():
    url = base_url + "/rest/api/2/permissions"
    max_results = 1000  # Set the total number of results you want
    results = []
    start_at = 0  # Initialize the starting point for pagination

    while len(results) < max_results:
        response = get(url, params={'maxResults': 100, 'startAt': start_at}).json()

        if 'permissions' not in response:
            print("No data found in 'results'.")
            return

        permissions = response['permissions']

        if not permissions:
            # No more results to retrieve
            break

        results.extend(permissions)
        start_at += len(permissions)

    # Define the CSV file name and open it for writing.
    csv_file_name = f"{instance_name}-permissions.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header row to the CSV file.
        header = ['Key', 'Name', 'Type', 'Description']
        csv_writer.writerow(header)

        # Iterate through the permissions and write their data to the CSV file.
        for key, permission in permissions.items():
            key = permission.get('key', '')
            name = permission.get('name', '')
            type = permission.get('type', '')
            description = permission.get('description', '')

            row = [key, name, type, description]
            csv_writer.writerow(row)

    print(f"Data saved to {csv_file_name}")

def get_workflows():
    url = base_url + "/rest/api/3/workflow/search"
    max_results = 1000  # Set the total number of results you want
    results = []
    start_at = 0  # Initialize the starting point for pagination

    while len(results) < max_results:
        response = get(url, params={'maxResults': 100, 'startAt': start_at}).json()

        workflows = response['values']

        if not workflows:
            # No more results to retrieve
            break

        results.extend(workflows)
        start_at += len(workflows)

    # Define the CSV file name and open it for writing.
    csv_file_name = f"{instance_name}-workflows.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header row to the CSV file.
        header = ['Id', 'Name', 'Description', 'Created', 'Updated']
        csv_writer.writerow(header)

        # Iterate through the permissions and write their data to the CSV file.
        for workflow in results:
            entity_id = workflow.get('id', {}).get('entityId', '')
            name = workflow.get('id', {}).get('name', '')
            description = workflow.get('description', '')
            created = workflow.get('created', '')
            updated = workflow.get('updated', '')

            row = [entity_id, name, description, created, updated]
            csv_writer.writerow(row)

    print(f"Data saved to {csv_file_name}")

# Execute the functions from the command line
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a function name as an argument.")
    else:
        function_name = sys.argv[1]

        if function_name == "get_filters":
            get_filters()
        elif function_name == "get_fields":
            get_fields()
        elif function_name == "get_resolutions":
            get_resolutions()
        elif function_name == "get_global_permissions":
            get_global_permissions()
        elif function_name == "get_workflows":
            get_workflows()
        else:
            print(
                "Invalid function name. Available functions: get_filters, get_fields, get_resolutions, get_global_permissions")

