import requests
from urllib.robotparser import RobotFileParser

def is_allowed(url, user_agent="MyScraperBot"):
    # Create a robot parser object
    rp = RobotFileParser()
    
    # Construct the URL to the site's robots.txt file
    # This splits the URL and rebuilds just the domain part + /robots.txt
    robots_url = url.split('/')[0] + '//' + url.split('/')[2] + '/robots.txt'
    
    # Set the URL and read the robots.txt file
    rp.set_url(robots_url)
    rp.read()
    
    # Check if our user agent is allowed to access this URL
    return rp.can_fetch(user_agent, url)

url = "https://example.com/interesting-data"
if is_allowed(url):
    # We're allowed to scrape this URL, so proceed
    r = requests.get(url)
else:
    # We're not allowed, so be respectful and don't scrape
    print("This URL is disallowed by robots.txt")
