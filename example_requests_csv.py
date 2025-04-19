import requests
import csv

# This is the URL for the weather measurements at O'Hare Airport in Chicago for 2025
# You can find your own location's data here:
# https://www.ncei.noaa.gov/access/search/data-search/global-summary-of-the-day
url = 'https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2025/72530094846.csv'

r = requests.get(url)
if r.status_code==200:
  content = r.content.decode('utf-8')
  csv_reader = csv.DictReader(content.splitlines())
  data = list(csv_reader)
  first_day = data[0]
  print(f"The low temperature on {first_day['DATE']} was {first_day['MIN']} F at {first_day['NAME']}.")
# The low temperature on 2025-01-01 was   27.0 F at CHICAGO OHARE INTERNATIONAL AIRPORT, IL US.