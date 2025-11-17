# secureops-lab

Home lab project to simulate security operations and compliance workflows for defense-style environments, using a virtualized network, Wazuh SIEM, and benchmark / STIG-aligned hardening.

---

## Lab Overview

This lab is built on a single Proxmox VE host and is designed to look and feel like a small enterprise network that needs to be monitored, hardened, and documented.

**Current endpoints:**

- **Proxmox VE** on a mini PC (Ryzen 9, 32 GB RAM)
- **Ubuntu Server** – Wazuh indexer / server / dashboard (single-node)
- **Windows 11** – blue-team endpoint and hardening target
- **Kali Linux** VMs – attacker / tooling box, used for generating activity and testing detections

The focus of this project is:

- Security monitoring with **Wazuh SIEM**
- Automated **SCA / OSCAP** checks
- **Windows hardening** based on benchmark findings
- Mapping the lab to **NIST SP 800-53** and the **RMF** lifecycle

---

## Project Goals

- Build a realistic, virtualized security lab that runs on a single host
- Collect logs and security events from all endpoints in **Wazuh**
- Run **SCA / OSCAP** scans and track compliance over time
- Implement Windows 11 hardening (password policy, lockout, audit policy, etc.)
- Map lab controls to **NIST 800-53 Rev. 5** and **RMF steps**
- Experiment with basic automation for parsing STIG content and control mappings

---

## Architecture

- **Hypervisor:** Proxmox VE on bare-metal mini PC  
- **Security Stack:** Wazuh indexer, server, and dashboard on Ubuntu Server  
- **Endpoints:**
  - Windows 11 – joined to Wazuh, hardened using local policy
  - Kali – used for reconnaissance / attack simulation
- **Compliance Tooling:**
  - Wazuh **SCA** policies and **OSCAP** content for benchmark checks
  - Custom scripts for mapping STIG and NIST controls

A network / VM topology diagram and screenshots live under:

- `docs/screenshots/` (Wazuh dashboards, scan results, hardening proof)
- `docs/RMF_Mapping.md` (how each component maps to controls and RMF steps)

---

## Key Capabilities

### 1. Security Monitoring (Wazuh SIEM)

- Wazuh manager and dashboard deployed on Ubuntu Server
- Agents installed on:
  - Windows 11 endpoint
  - Kali VM(s) (as needed)
- Centralized logging and alerting for:
  - Authentication events
  - System and security logs
  - File integrity / configuration changes (where enabled)

Planned documentation: `wazuh/README.md` with exported config snippets and custom rule examples.

---

### 2. Compliance Scanning (SCA / OSCAP)

- Wazuh **SCA** policies used to assess:
  - Windows 11 security baseline items
  - Linux host configuration where applicable
- **OSCAP** content used for benchmark / STIG-style checks on supported systems
- Scan results are captured in:
  - Wazuh dashboard views (screenshots in `docs/screenshots/`)
  - Future CSV / JSON exports for tracking deltas over time

---

### 3. Windows 11 Hardening

The Windows 11 VM is configured as the primary hardening target. Work includes:

- Account and password policies (length, complexity, lockout)
- Interactive logon and session controls
- Audit policies tied back to Wazuh log collection
- Additional settings driven by SCA / OSCAP findings

Planned documentation: `windows-hardening/` with:

- `baseline-settings.md` – initial state
- `hardened-settings.md` – final state and rationale
- Notes on how changes impact SCA / OSCAP scores

---

### 4. RMF & NIST 800-53 Mapping

The lab is tied back to governance / compliance using:

- `docs/RMF_Mapping.md` – mapping lab components to:
  - RMF phases (Categorize, Select, Implement, Assess, Authorize, Monitor)
  - NIST 800-53 Rev. 5 control families (e.g., AC, AU, CM, SI)
- `scripts/rmf_mapper.py` – helper script for working with control mappings
- `scripts/stig_parser.py` – experimental parser for STIG / benchmark data

This demonstrates not only technical configuration work, but also how it fits into a formal risk-management framework.

---

## Repository Layout

> This layout focuses on the parts of the lab that are implemented today, plus a small amount of experimental automation.

- **`docs/`**
  - `RMF_Mapping.md` – NIST 800-53 + RMF mapping for lab components
  - `screenshots/` – Wazuh dashboards, SCA / OSCAP results, hardening proof
- **`wazuh/`** *(to be populated)*  
  Wazuh configuration snippets, SCA policies, custom rules, and notes.
- **`windows-hardening/`** *(to be populated)*  
  Documentation of Windows 11 baseline vs hardened state, with links back to findings.
- **`scripts/`**
  - `rmf_mapper.py` – utility for working with control mappings
  - `stig_parser.py` – experimental STIG / benchmark parsing script
- **`infra/`**
  - `stig_remediation.yml` – early experimentation with STIG remediation automation
- **`LICENSE`** – Apache 2.0
- **`README.md`** – this file

---

## Roadmap

- [x] Deploy Proxmox and create core lab VMs
- [x] Deploy Wazuh indexer / server / dashboard on Ubuntu Server
- [x] Install Wazuh agents on Windows 11 and Kali
- [x] Run initial SCA / OSCAP scans and verify alerts in Wazuh
- [x] Begin RMF / NIST 800-53 control mapping (`docs/RMF_Mapping.md`)
- [ ] Document Wazuh configuration and custom rules under `wazuh/`
- [ ] Fully document Windows hardening steps under `windows-hardening/`
- [ ] Add more complete scan exports (JSON/CSV) for trend analysis
- [ ] Expand automation around STIG content using the scripts in `scripts/`

---

## License

This project is licensed under the **Apache 2.0** License – see `LICENSE` for details.
