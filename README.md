## Jira Cloud CSV Extractor

This script is designed for Jira Cloud administrative use. It provides functionality to retrieve and save important information in CSV format (using pagination to save all data at once).

##### Usage

    Ensure you have the required dependencies installed. You can install them using the following command:

    bash

    `pip install requests`

Update the configuration in the `config.py` file with your Jira Cloud credentials and base URL.

Run the script from the command line with the desired function name as an argument. For example:

bash

    python script_name.py get_filters

    Available functions:
        get_filters: Retrieves Jira filters and saves them to a CSV file.
        get_fields: Retrieves Jira fields and saves them to a CSV file.
        get_resolutions: Retrieves Jira resolutions and saves them to a CSV file.
        get_global_permissions: Retrieves Jira global permissions and saves them to a CSV file.

**Note:** Ensure that you have proper permission to access the specified Jira Cloud instance.

##### Dependencies
    Requests: This script utilizes the requests library to make HTTP requests to the Jira Cloud REST API.
