import os
import re
import json
import redis
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from datetime import datetime, UTC


# -----------------------------
# CONFIG
# -----------------------------
URL = "https://www.sc.com.my/investor-alert-list"

# Set to True if you want to ignore Redis duplicates (for testing)
DEBUG_IGNORE_REDIS = True

# Connect to Redis
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

# -----------------------------
# FETCH DATA
# -----------------------------
def fetch_all_data():
    try:
        html = requests.get(URL, timeout=30).text
    except Exception as e:
        print("Error fetching URL:", e)
        return []

    soup = BeautifulSoup(html, "lxml")
    script_text = None

    for script in soup.find_all("script"):
        if script.string and "$X.PMD" in script.string:
            script_text = script.string
            break

    if not script_text:
        print(" $X.PMD not found")
        return []

    match = re.search(r"\$X\.PMD\s*=\s*(\{.*?\});\s*\$X", script_text, re.S)
    if not match:
        print(" JSON block not found")
        return []

    data = json.loads(match.group(1))
    entities = []

    for parent in data.values():
        if not isinstance(parent, dict):
            continue
        for record in parent.values():
            if not isinstance(record, dict):
                continue
            name = record.get("name", "").strip()
            if not name:
                continue
            entity = {
                "name": name,
                "address": record.get("address", "").strip(),
                "website": record.get("website", "").strip(),
                "remark": record.get("remark", "").strip(),
                "date": record.get("date", "").strip(),
                "image_url": record.get("url", "").strip(),
            }
            entities.append(entity)

    return entities

# -----------------------------
# REDIS STORAGE
# -----------------------------
def save_to_redis(entity):
    name_key = entity["name"].lower()
    # Prevent duplicates
    if not DEBUG_IGNORE_REDIS:
        if not r.sadd("sc:visited:names", name_key):
            return False
    r.hset("sc:entities", name_key, json.dumps(entity, ensure_ascii=False))
    return True

# -----------------------------
# EXPORT XML
# -----------------------------
def save_xml(data, filename="outputfile/malaysia_sc_redis.xml"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    root = ET.Element("Investors")

    for item in data:
        investor_el = ET.SubElement(root, "Investor")
        ET.SubElement(investor_el, "name").text = item.get("name", "")

        def add_field(parent, tag, value, separators=r"[;•|]"):
            if not value:
                return
            if isinstance(value, str):
                values = [v.strip() for v in re.split(separators, value) if v.strip()]
            elif isinstance(value, list):
                values = value
            else:
                values = [str(value)]
            if len(values) > 1:
                parent_tag = ET.SubElement(parent, tag + "s")  # plural container
                for v in values:
                    ET.SubElement(parent_tag, tag).text = v
            else:
                ET.SubElement(parent, tag).text = values[0]

        add_field(investor_el, "address", item.get("address", ""), separators=r";")
        add_field(investor_el, "website", item.get("website", ""), separators=r"[\|\s+](?=[^\n])")
        add_field(investor_el, "remark", item.get("remark", ""), separators=r"[•·]")
        add_field(investor_el, "date", item.get("date", ""))
        add_field(investor_el, "image_url", item.get("image_url", ""))

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    print(f" XML saved: {filename}")

# -----------------------------
# EXPORT JSON
# -----------------------------
def save_json(data, filename="outputfile/malaysia_sc_redis.json"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f" JSON saved: {filename}")

# -----------------------------
# MAIN
# -----------------------------
def main():
    entities = fetch_all_data()
    if not entities:
        print("No entities found, exiting.")
        return

    print(f"Fetched entities: {len(entities)}")
    for e in entities[:5]:
        print(e)  # debug first 5

    saved = []
    for e in entities:
        if save_to_redis(e):
            saved.append(e)

    r.set("sc:last_run", datetime.now(UTC).isoformat())

    print(f"Total scraped: {len(entities)}")
    print(f"New saved: {len(saved)}")

    if saved:
        save_xml(saved, "outputfile/malaysia_sc_redis.xml")
        save_json(saved, "outputfile/malaysia_sc_redis.json")

# -----------------------------
if __name__ == "__main__":
    main()
