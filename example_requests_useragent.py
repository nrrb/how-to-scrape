import requests

url = "https://httpbin.io/user-agent"
r = requests.get(url)  # Make a request to a service that returns our User-Agent
print(r.json()['user-agent'])  # Extract and print the User-Agent from the JSON response
# This will show something like 'python-requests/2.31.0'
# Sites can easily detect this isn't a real browser!