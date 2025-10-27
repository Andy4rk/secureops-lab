# scripts/rmf_mapper.py

import yaml

def load_controls(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def display_mapping(data):
    for control, info in data.items():
        print(f"{control}: {info['name']}")
        print(f"  Component: {info['component']}")
        print(f"  Notes: {info['notes']}\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python rmf_mapper.py <controls.yaml>")
    else:
        data = load_controls(sys.argv[1])
        display_mapping(data)
