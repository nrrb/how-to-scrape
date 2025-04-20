import requests
from bs4 import BeautifulSoup

url = "https://lxml.de/"
r = requests.get(url)  # Make the HTTP request for the page
if r.status_code==200:  # If successful
  # Create a BeautifulSoup object from the HTML content
  # This parses the HTML into a navigable structure
  soup = BeautifulSoup(r.content)
  print(f"Retrieved {url}")
  
  # With BeautifulSoup, we can directly access elements like title
  title = soup.title.text  # Get just the text inside the <title> tag
  body = soup.body.text  # Get all text inside the <body> tag
  
  # We can also use CSS selectors to find specific elements
  # This finds the first h1 tag with class "title" and extracts its text
  headline = soup.select('h1.title')[0].text  # 'lxml - XML and HTML with Python'
else:
  print(f"Couldn't get {url}, HTTP status code was {r.status_code}")