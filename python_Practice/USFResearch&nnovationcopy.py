import requests

url = "https://8qbz5f6jov-dsn.algolia.net/1/indexes/technologies/query"

headers = {
    "Content-Type": "application/json",
    "x-algolia-application-id": "8QBZ5F6JOV",
    "x-algolia-api-key": "b78d623731ba38769c5b0701ca58ba7c"
}

page = 0

while True:
    payload = {
        "params": f"query=&hitsPerPage=50&page={page}"
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    hits = data.get("hits", [])
    if not hits:
        break

    print(f"\nPage {page} → {len(hits)} records\n")

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
