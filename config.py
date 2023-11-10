# This script is created by Ana Vitória Selista for Jira administrative use

from requests.auth import HTTPBasicAuth

# The base URL of your instance
base_url = "https://{YOUR-INSTANCE-NAME}.atlassian.net/"

# Set the authentication credentials using HTTP Basic Authentication
credentials = HTTPBasicAuth("{YOUR-EMAIL}", "{API-TOKEN}")