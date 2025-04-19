import requests

url = "https://www.google.com/"
r = requests.get(url)
if r.status_code==200: # HTTP 200 means there was a successful response
  html = r.content
  print("Retrieved {url}")
else:
  print(f"Couldn't get {url}, HTTP status code was {r.status_code}")