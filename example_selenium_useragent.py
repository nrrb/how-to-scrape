from selenium import webdriver
from bs4 import BeautifulSoup
import json

url = "https://httpbin.io/user-agent"  # Service that shows our User-Agent
driver = webdriver.Chrome()  # Start up a Chrome browser
driver.get(url)  # Load the URL
html = driver.page_source  # Get the rendered page source
driver.quit()  # Close the browser

# Parse the HTML and extract the User-Agent from the JSON response
soup = BeautifulSoup(html)
print(json.loads(soup.text)['user-agent'])
# This will show something like 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36...'
# Much more like a real browser!