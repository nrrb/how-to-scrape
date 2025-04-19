import requests

url = "https://httpbin.io/user-agent"
r = requests.get(url)
print(r.json()['user-agent'])
# Something like 'python-requests/2.31.0'