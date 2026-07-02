'''A Complete Example — End to End'''
import requests

# 1. Build the request
URL = "https://api.github.com/users/Ankitabanerji/repos"
headers = {"Accept": "application/json"}

# 2. Send it — this does the entire HTTP cycle
response = requests.get(URL, headers=headers)

# 3. Inspect the response
print(response.status_code)    # 200
print(response.headers)  # application/json; charset=utf-8
print(response.json()[0])        # First repo name

# NOTES: What happens under the hood:
# - requests.get(...) opens a TCP connection to api.github.com:443
# - Performs a TLS handshake (because HTTPS)
# - Sends the HTTP GET request
# - Reads the HTTP response from the server
# - Returns a Response object with .status_code, .headers, .json() etc.