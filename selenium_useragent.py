from selenium import webdriver
from bs4 import BeautifulSoup
import json

url = "https://httpbin.io/user-agent"
driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source
driver.quit()
soup = BeautifulSoup(html)
print(json.loads(soup.text)['user-agent'])
# Something like 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'