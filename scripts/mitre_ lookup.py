# scripts/mitre_lookup.py

import json

def load_attack_data(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def lookup_technique(tech_id, data):
    for item in data["techniques"]:
        if item["id"] == tech_id:
            return item
    return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python mitre_lookup.py <technique_id> <data.json>")
    else:
        data = load_attack_data(sys.argv[2])
        result = lookup_technique(sys.argv[1], data)
        if result:
            print(f"{result['id']}: {result['name']}\n{result['description']}")
        else:
            print("Technique not found.")
