from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.uniqlo.com/us/en/feature/sale/men?storeId=125789&inventoryCondition=1"
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(5) # wait 5 seconds for the page to load
soup = BeautifulSoup(driver.page_source)
driver.quit()