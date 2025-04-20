import requests
import pandas as pd

# Same Chicago weather data URL as before
url = 'https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2025/72530094846.csv'
r = requests.get(url)  # Make the HTTP request
if r.status_code==200:  # If successful
  # Convert the response to a CSV string and use pandas to parse it directly
  # This is a slick one-liner that replaces multiple steps from the previous example
  df = pd.read_csv(pd.io.common.StringIO(r.content.decode('utf-8')))
  
  # Here's where pandas shines - we can easily find the coldest day
  # idxmin() gives us the index of the minimum value in the 'MIN' column
  coldest_day = df.loc[df['MIN'].idxmin()]
  
  # Print out our finding in a readable format
  print(f"The coldest day of 2025 so far was {coldest_day['DATE']} with {coldest_day['MIN']}°F at {coldest_day['NAME']}.")
# The coldest day of 2025 so far was 2025-01-20 with -5.0°F at CHICAGO OHARE INTERNATIONAL AIRPORT, IL US.