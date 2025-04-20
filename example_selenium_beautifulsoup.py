from selenium import webdriver
from bs4 import BeautifulSoup
 
# A URL that probably uses JavaScript to load its content
url = "https://www.uniqlo.com/us/en/feature/sale/men?storeId=125789&inventoryCondition=1"

# Initialize a Chrome browser instance that Selenium will control
driver = webdriver.Chrome()

# Tell the browser to load our URL
driver.get(url)

# Wait 5 seconds for the page to fully load
# This gives JavaScript time to render the page content
driver.implicitly_wait(5)

# Get the fully rendered HTML (after JavaScript execution)
# and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source)

# Always close the browser when we're done to free up resources
driver.quit()

# Print the page title as a simple test
print(soup.title.text)
# Sale | Clothing & Accessories for Men | UNIQLO US
