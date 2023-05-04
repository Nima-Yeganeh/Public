import requests
import json

# Make an HTTP GET request to the GitHub API
response = requests.get('https://api.github.com/repos/requests/requests')

# Parse the JSON response into a Python dictionary
data = json.loads(response.text)

# Print the repository name and description
print("Repository name:", data['name'])
print("Description:", data['description'])
