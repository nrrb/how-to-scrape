import requests

url = "https://www.google.com/"
r = requests.get(url)  # This is where we actually make the HTTP request to fetch the URL
if r.status_code==200:  # HTTP 200 means our request was successful
  html = r.content  # The raw HTML content of the page is stored in r.content
  print(f"Retrieved {url}")  # Just confirming we got the page successfully
else:
  # If we didn't get a 200, something went wrong - maybe the site is down or blocked us
  print(f"Couldn't get {url}, HTTP status code was {r.status_code}")