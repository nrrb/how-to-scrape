import requests

search_url = 'https://openlibrary.org/search/authors.json?q=thich%20nhat%20hanh'
r = requests.get(search_url)
if r.status_code==200:
  results = r.json()
  for result in results['docs']:
    print(f"Key: {result['key']} Author: {result['name']} ({result['work_count']} works on record)")
# Key: OL2623681A Author: Thích Nhất Hạnh (681 works on record)
# Key: OL12771438A Author: Thich Nhat Hanh (28 works on record)
# Key: OL14127406A Author: Lilian Cheung Thich Nhat Hanh (1 works on record)
# Key: OL10831290A Author: Thomas Merton ; Thich Nhat Hanh (1 works on record)
# Key: OL10829635A Author: Brush Dance and Thich Nhat Hanh (1 works on record)
# Key: OL12195067A Author: Nicholas Kirsten-Honshin Thich Nhat Hanh (1 works on record)
# Key: OL12857628A Author: Nhất Hạnh Thích (20 works on record)
# Key: OL14080878A Author: Nhá̂t Hạnh Thích (2 works on record)
# Key: OL13496000A Author: HANH Thich Nhat - (1 works on record)
# Key: OL13904327A Author: Nhat Hanh Thich (1 works on record)
# Key: OL13978476A Author: Hanh Thich Nhat (1 works on record)
#
# The first result OL2623681A has the highest number of works so it's likely it's that one
author_record = results['docs'][0]
works_url = f"https://openlibrary.org/authors/{author_record['key']}/works.json?limit=1000"
r = requests.get(works_url)
if r.status_code==200:
  results = r.json()
  works = results['entries']
  print(f"Found {len(works)} works for {author_record['name']}.")
  print("Here are the first 10 titles:")
  for work in works[:10]:
    print(work['title'])