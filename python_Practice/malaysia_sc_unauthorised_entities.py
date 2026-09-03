import requests
import re
import json
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import os

url = "https://www.sc.com.my/investor-alert-list"

html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")

def fetch_all_data():
    script_text = None

    # Find script containing $X.PMD
    for script in soup.find_all("script"):
        if script.string and "$X.PMD" in script.string:
            script_text = script.string
            break

    if not script_text:
        print("$X.PMD not found")
        return []

    # Extract JSON using regex
    match = re.search(r"\$X\.PMD\s*=\s*(\{.*?\});\s*\$X", script_text, re.S)
    if not match:
        print("JSON block not found")
        return []

    json_text = match.group(1)

    # Load JSON
    data = json.loads(json_text)
    # print("JSON extracted successfully")
    # print("Total keys:", len(data))

    entities = []

    for parent_id, parent_value in data.items():
        if isinstance(parent_value, dict):
            for child_id, record in parent_value.items():
                if not isinstance(record, dict):
                    continue

                name = record.get("name", "").strip()
                address = record.get("address", "").strip()
                website = record.get("website", "").strip()
                remark = record.get("remark", "").strip()
                date = record.get("date", "").strip()
                image_url = record.get("url", "").strip()

                if name:
                    entities.append({
                        "name": name,
                        "address": address,
                        "website": website,
                        "remark": remark,
                        "date": date,
                        "image_url": image_url
                    })

    print(f"Extracted total entities: {len(entities)} entities")
    return entities

#------------------Save XML-----------------------------------
def save_xml(data, filename="outputfile/malaysia_sc_unauthorised_entities.xml"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    root = ET.Element("Investors")

    for item in data:
        investor_el = ET.SubElement(root, "Investor")
        ET.SubElement(investor_el, "name").text = item.get("name", "")

        # Helper function to split and save multiple values
        def add_field(parent, tag, value, separators=r"[;•|]"):
            if not value:
                return
            # Split by separators, remove extra spaces
            if isinstance(value, str):
                values = [v.strip() for v in re.split(separators, value) if v.strip()]
            elif isinstance(value, list):
                values = value
            else:
                values = [str(value)]

            if len(values) > 1:
                parent_tag = ET.SubElement(parent, tag + "s")  # e.g., addresses
                for v in values:
                    ET.SubElement(parent_tag, tag).text = v
            else:
                ET.SubElement(parent, tag).text = values[0]

        # Use appropriate separators for each field
        add_field(investor_el, "address", item.get("address", ""), separators=r";")
        add_field(investor_el, "website", item.get("website", ""), separators=r"[\|\s+]")
        add_field(investor_el, "remark", item.get("remark", ""), separators=r"[•]")

        add_field(investor_el, "date", item.get("date", ""))
        add_field(investor_el, "image_url", item.get("image_url", ""))

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    print(f"XML saved: {filename}")

# -----------------------------
# SAVE JSON
# -----------------------------
def save_json(data, filename="outputfile/malaysia_sc_unauthorised_entities.json"):
    import os
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"JSON saved: {filename}")
# -----------------------------

# -----------------------------
# RUN
# -----------------------------
def main():
    data = fetch_all_data()
    print(f"Total records: {len(data)}")

    if data:
        save_json(data)
        save_xml(data)

if __name__ == "__main__":
    main()
