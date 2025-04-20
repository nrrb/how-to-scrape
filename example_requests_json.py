import requests

# This URL searches for authors with the name "thich nhat hanh" in the Open Library API
search_url = 'https://openlibrary.org/search/authors.json?q=thich%20nhat%20hanh'
r = requests.get(search_url)  # Make the HTTP request to the API
if r.status_code==200:  # If the request was successful
  results = r.json()  # Parse the JSON response directly into a Python dictionary
  for result in results['docs']:  # Loop through each author result
    # Print a neatly formatted summary of each author and their work count
    print(f"Key: {result['key']} Author: {result['name']} ({result['work_count']} works on record)")

# Now we'll use the first result (which has the most works) to find their books
author_record = results['docs'][0]  # Grab the first author record (most works)
# Construct a new URL to get up to 1000 works by this author
works_url = f"https://openlibrary.org/authors/{author_record['key']}/works.json?limit=1000"
r = requests.get(works_url)  # Make another HTTP request for the works
if r.status_code==200:  # If this request was also successful
  results = r.json()  # Parse this JSON response
  works = results['entries']  # Get the list of works
  print(f"Found {len(works)} works for {author_record['name']}.")
  print("Here are the first 10 titles:")
  # Loop through the first 10 works and print their titles
  for work in works[:10]:
    print(work['title'])