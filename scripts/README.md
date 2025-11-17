# Scripts Directory

This directory contains helper tools and early-stage automation related to compliance analysis, STIG content parsing, and MITRE ATT&CK mapping. These scripts support the broader goals of the lab: improving system hardening, understanding benchmark requirements, and relating security findings to established frameworks.

The scripts in this folder are experimental but functional, and they demonstrate familiarity with common frameworks used in cybersecurity engineering, RMF workflows, and detection tuning.

---

## 📁 Included Scripts

### **1. rmf_mapper.py**
*A utility for working with NIST SP 800-53 Rev. 5 controls and mapping them to different components of the lab.*

**Purpose:**
- Helps visualize how lab elements (Wazuh, endpoints, hardening, SCA results) fit into the RMF process.
- Supports exploratory work around control interpretation, inheritance, and implementation evidence.

**Capabilities:**
- Load and display control families.
- Retrieve specific security controls.
- Used in conjunction with `docs/RMF_Mapping.md`.

**Relevance:**
This script demonstrates practical understanding of governance frameworks and helps keep the lab aligned with RMF-style documentation standards.

---

### **2. stig_parser.py**
*An early-stage parser for working with STIG or benchmark-like data sources and extracting relevant security configuration requirements.*

**Purpose:**
- Serve as the foundation for future STIG automation.
- Practice handling machine-readable compliance data.
- Output simplified or human-readable summaries for analysis.

**Capabilities:**
- Parse structured content (XML/JSON-like formats).
- Extract rule identifiers or descriptions.
- Useful for comparing STIG guidance to SCA/OSCAP findings.

**Relevance:**
Even in early form, this script supports your project's emphasis on configuration compliance, benchmark analysis, and eventual automation of remediation workflows.

---

### **3. mitre_lookup.py**
*A functional helper script for querying MITRE ATT&CK technique data.*

**Purpose:**
- Quickly look up technique names, descriptions, and metadata.
- Support mapping of detections or SCA findings to adversary behaviors.
- Reinforce awareness of ATT&CK as a threat-modeling framework.

**Capabilities:**
- Query MITRE ATT&CK technique identifiers.
- Return structured, readable output for fast analysis.
- Useful during detection engineering or alert enrichment.

**Relevance:**
MITRE ATT&CK alignment is increasingly expected in cybersecurity roles (defense contractors, SOCs, cyber engineering teams).  
This script shows that you understand how to leverage ATT&CK for analytical or defensive tasks.

---

## 🔧 Future Additions (Planned)

Potential future tools that may be added as the lab expands:

- Automated OSCAP / Wazuh SCA result exporter  
- Windows hardening validation parser  
- Log-to-technique mapping helper  
- YAML → RMF control documentation generator  
- STIG-to-Wazuh rule translator (long-term stretch goal)  

These scripts will evolve as the lab grows and as new compliance, detection, or automation tasks arise.

---

## 📘 Usage Notes

- These scripts are **standalone utilities** — they do not modify systems
