# Screenshot Gallery

This folder contains evidence from the lab environment, specifically Wazuh dashboard views, Security Configuration Assessment (SCA) results, and baseline compliance scans. These screenshots demonstrate the initial (unhardened) security posture of each endpoint before remediation and configuration changes.

> **Note:** Only initial baseline scans are included at this time. Additional screenshots (Wazuh agents, alerts, rule matches, and hardened system results) will be added as the lab progresses.
>
> **Note:** Only one Kali screenshot is included, as both Kali VMs are configured identically.

---

## Purpose of These Screenshots

Each screenshot is intended to validate that:

- Wazuh is successfully receiving data from deployed agents  
- SCA policies are running correctly across all endpoints  
- CIS compliance scans have been executed as a baseline  
- Systems are in their natural, un-hardened state prior to remediation  

These results form the “before” portion of the lab’s hardening and compliance cycle, supporting future comparisons and showing measurable improvement.

---

## Endpoint Coverage

My current environment uses a single-node Wazuh SIEM hosted on Ubuntu, with agents deployed on:

- **Windows 11 workstation**
- **Kali Linux workstation**
- **Ubuntu/Kali-based Linux VM (Wazuh manager host)**
- Additional endpoints will be added as the lab expands

The SCA content used here evaluates systems against **CIS Benchmarks**, commonly referenced in:

- DoD/IC environments  
- STIG / hardening workflows  
- RMF step 4 (“Assess”)  
- Enterprise security baselines  

---

## Windows 11 — Baseline CIS Compliance Scan

**Benchmark:** CIS Microsoft Windows 11 Enterprise v3.0.0  
**Checks:** 482  
**Pass:** 124  
**Fail:** 349  
**Not Applicable:** 9  
**Score:** **26%**

This scan shows the initial state of a fresh Windows 11 installation.  
The high number of failures is expected and serves as a clear starting point for:

- Hardening
- Policy enforcement
- Verification via SCA rescans
- Wazuh rule tuning

### Screenshot — Windows 11 CIS Benchmark (Initial Scan)

<img width="1280" height="648" alt="Windows 11 Initial CIS Scan" src="https://github.com/user-attachments/assets/59da21a9-e1ee-4cd0-8960-bb2a74b3c22d" />

---

## Kali Linux — Baseline CIS Distribution Independent Benchmark

**Benchmark:** CIS Distribution Independent Linux Benchmark v2.0.0  
**Checks:** 190  
**Pass:** 83  
**Fail:** 99  
**Not Applicable:** 8  
**Score:** **45%**

Kali Linux is intentionally configured with looser, penetration-testing-oriented defaults.  
Many CIS controls fail by design, making it a useful “worst-case baseline” for demonstrating:

- Hardening effectiveness  
- Policy enforcement measures  
- How Wazuh interprets Linux baseline compliance  

### Screenshot — Kali Linux CIS Benchmark (Initial Scan)

<img width="1280" height="648" alt="Kali Initial CIS Scan" src="https://github.com/user-attachments/assets/ab8041ac-a817-47d4-bff1-6e845898f3e1" />

---

## Next Additions (Planned)

Additional screenshots will be added to support:

- Wazuh agent inventory view  
- SCA policy details and rule descriptions  
- Windows hardening (before/after)  
- OSCAP scan results  
- Custom Wazuh rule triggers  
- Alert correlation views  

These artifacts will serve as proof of lab maturity and progressive compliance improvement.
