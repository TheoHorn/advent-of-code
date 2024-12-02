import requests
from requests_oauthlib import OAuth1Session

def get_webpage_content(url, client_key, client_secret, resource_owner_key, resource_owner_secret):
    if not url.startswith('https://'):
        return "Error: URL must start with 'https://'"
    
    oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)
    
    response = oauth.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: Unable to fetch the webpage. Status code: {response.status_code}"

# Example usage
url = 'https://adventofcode.com/2024/day/2/input'
client_key = 'your_client_key'
client_secret = 'your_client_secret'
resource_owner_key = 'your_resource_owner_key'
resource_owner_secret = 'your_resource_owner_secret'

content = get_webpage_content(url, client_key, client_secret, resource_owner_key, resource_owner_secret)
print(content)