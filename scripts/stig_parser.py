# scripts/stig_parser.py

import xml.etree.ElementTree as ET

def parse_stig_report(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    findings = []

    for rule in root.findall(".//rule-result"):
        result = rule.find("result").text
        title = rule.find("rule").get("id")
        if result != "pass":
            findings.append((title, result))

    print(f"Total findings: {len(findings)}")
    for title, result in findings:
        print(f"{title}: {result}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python stig_parser.py <report.xml>")
    else:
        parse_stig_report(sys.argv[1])
