import requests
import time

# List of URLs we want to scrape
urls = ["https://example.com/page1", "https://example.com/page2", "..."]

for url in urls:
    # Request the URL
    r = requests.get(url)
    
    # Process the response (placeholder function)
    # In a real scraper, you'd extract and store data here
    process_response(r)
    
    # Wait between requests to avoid hammering the server
    # Being a good digital citizen means not overloading websites
    time.sleep(1)  # 1 second delay between requests