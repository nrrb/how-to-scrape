import requests
import time

# List of URLs we want to scrape
urls = ["https://example.com/page1", "https://example.com/page2"]
contents = []

for url in urls:
    # Request the URL
    r = requests.get(url)

    # Store the content in an array for later processing    
    contents.append(r.content)
    
    # Wait between requests to avoid hammering the server
    # Being a good digital citizen means not overloading websites
    time.sleep(1)  # 1 second delay between requests