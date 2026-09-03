import requests
import json

url = "https://8qbz5f6jov-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.10.5)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.30.2)%3B%20JS%20Helper%20(3.5.5)&x-algolia-api-key=b78d623731ba38769c5b0701ca58ba7c&x-algolia-application-id=8QBZ5F6JOV"

page = 0
hits_per_page = 50
while True:

  payload = json.dumps({
    "requests": [
      {
        "indexName": "technologies",
        "params": f"hitsPerPage={hits_per_page}&page={page}"
      }
    ]
  })

  headers = {
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  data = response.json()
  hits = data.get("results", [])[0].get("hits", [])
  if not hits:
        break

  for row in hits:
    title = row.get("title", "").strip()
    url_link = row.get("Url", "").strip()

    inventors = row.get("inventors", [])
    inventors_text = ", ".join(inventors) if inventors else "N/A"

    print("Title     :", title)
    print("URL       :", url_link)
    print("Inventors :", inventors_text)
    print()

  page += 1
