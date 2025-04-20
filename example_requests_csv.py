import requests
import csv

# This URL points to weather data for Chicago's O'Hare Airport for 2025
# NOAA provides this data in a nicely structured CSV format - perfect for scraping!
url = 'https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2025/72530094846.csv'

r = requests.get(url)  # Make the HTTP request for the CSV data
if r.status_code==200:  # Check if we got a successful response
  content = r.content.decode('utf-8')  # Convert the raw bytes to a UTF-8 string
  csv_reader = csv.DictReader(content.splitlines())  # Parse the CSV text into a dict reader
  data = list(csv_reader)  # Convert the reader to a list of dictionaries, one per row
  first_day = data[0]  # Grab just the first day's data (Jan 1, 2025)
  # Print the results in a nice readable format
  print(f"The low temperature on {first_day['DATE']} was {first_day['MIN']} F at {first_day['NAME']}.")
# The low temperature on 2025-01-01 was   27.0 F at CHICAGO OHARE INTERNATIONAL AIRPORT, IL US.