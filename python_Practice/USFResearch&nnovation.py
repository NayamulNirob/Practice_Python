import requests
import json
import xml.etree.ElementTree as ET

# -----------------------------
# CONFIG
# -----------------------------
URL = "https://8qbz5f6jov-dsn.algolia.net/1/indexes/technologies/query"

HEADERS = {
    "Content-Type": "application/json",
    "x-algolia-application-id": "8QBZ5F6JOV",
    "x-algolia-api-key": "b78d623731ba38769c5b0701ca58ba7c"
}

# -----------------------------
# FETCH DATA
# -----------------------------
def fetch_all_data():
    all_records = []
    page = 0

    while True:
        payload = {
            "params": f"query=&hitsPerPage=50&page={page}"
        }

        r = requests.post(URL, headers=HEADERS, json=payload, timeout=30)
        data = r.json()

        hits = data.get("hits", [])
        if not hits:
            break

        for row in hits:
            record = {
                "title": row.get("title", "").strip(),
                "url": row.get("Url", "").strip(),
                "inventors": row.get("inventors", []),
                "disclosureDate": row.get("disclosureDate", "")
            }
            all_records.append(record)

        page += 1

    return all_records


# -----------------------------
# SAVE JSON
# -----------------------------
def save_json(data, filename="outputfile/USFResearch&nnovation.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f" JSON saved: {filename}")


# -----------------------------
# SAVE XML
# -----------------------------
def save_xml(data, filename="outputfile/USFResearch&nnovation.xml"):
    root = ET.Element("technologies")

    for item in data:
        tech = ET.SubElement(root, "technology")

        ET.SubElement(tech, "title").text = item["title"]
        ET.SubElement(tech, "url").text = item["url"]
        ET.SubElement(tech, "disclosureDate").text = item["disclosureDate"]

        inventors_el = ET.SubElement(tech, "inventors")
        for inv in item["inventors"]:
            ET.SubElement(inventors_el, "inventor").text = inv

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

    print(f" XML saved: {filename}")


# -----------------------------
# RUN
# -----------------------------
def main():
    data = fetch_all_data()
    print(f"Total records: {len(data)}")

    save_json(data)
    save_xml(data)


if __name__ == "__main__":
    main()
