import requests
from bs4 import BeautifulSoup

url = "https://www.uniqlo.com/us/en/feature/sale/men?storeId=125789&inventoryCondition=1"
r = requests.get(url) # It never finishes this request
if r.status_code==200:
  soup = BeautifulSoup(r.content)
  print(f"Retrieved {url}")
else:
  print(f"Couldn't get {url}, HTTP status code was {r.status_code}")