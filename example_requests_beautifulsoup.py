import requests
from bs4 import BeautifulSoup

url = "https://lxml.de/"
r = requests.get(url)
if r.status_code==200:
  soup = BeautifulSoup(r.content)
  print(f"(Retrieved {url}")
  title = soup.title.text # title is a direct, singular child of html
  body = soup.body.text # body is too
  headline = soup.select('h1.title')[0].text # 'lxml - XML and HTML with Python'
else:
  print(f"Couldn't get {url}, HTTP status code was {r.status_code}")