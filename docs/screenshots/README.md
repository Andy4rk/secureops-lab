## Screenshot Gallery

This folder contains evidence from the lab environment: Wazuh dashboards, compliance scans, and hardening results.

> Note: Only initial scan screenshots are checked in at this time. Additional views (agents, alerts, updated hardening state) will be added as they are captured.

# Each screenshot is intended to show:

- That Wazuh is successfully running and collecting scan results
- That baseline configuration checks have been performed
- A starting point for future hardening and remediation work


# My environment uses a single-node Wazuh SIEM hosted on Ubuntu, with agents deployed on:
- Windows 11 workstation
- Kali Linux workstation
- Ubuntu/Kali-based Linux VM
- Additional endpoints as the lab grows

This README focuses on the Security Configuration Assessment (SCA) capability within Wazuh, which evaluates systems against CIS Benchmarks — commonly used in enterprise security programs, DoD/STIG environments, and regulated infrastructures.


These scans serve as the baseline state before hardening the systems.
The initial scans are intentionally insecure — this demonstrates the real-world reality of un-hardened operating systems and sets up the opportunity for before/after improvement.

⸻

Windows 11 — Baseline CIS Compliance Scan

Policy: CIS Microsoft Windows 11 Enterprise Benchmark v3.0.0
Checks: 482
Pass: 124
Fail: 349
Not Applicable: 9
Score: 26%

This baseline scan reflects an un-hardened Windows 11 installation.
The high number of failed checks (349) is expected and provides a perfect starting point for improvement.

Screenshot — Windows 11 CIS Benchmark (Initial Scan)



<img width="1280" height="648" alt="Screenshot 2025-11-15 at 1 12 45 AM" src="https://github.com/user-attachments/assets/59da21a9-e1ee-4cd0-8960-bb2a74b3c22d" />




Kali Linux — Baseline CIS Distribution Independent Benchmark

Policy: CIS Distribution Independent Linux Benchmark v2.0.0
Checks: 190
Pass: 83
Fail: 99
Not Applicable: 8
Score: 45%

Kali Linux is intentionally permissive due to its penetration testing nature. Many CIS controls are expected to fail by design.
This makes Kali an excellent “worst-case scenario” for demonstrating hardening improvements.

Screenshot — Kali Linux CIS Benchmark (Initial Scan)

<img width="1280" height="648" alt="Screenshot 2025-11-15 at 1 11 04 AM" src="https://github.com/user-attachments/assets/ab8041ac-a817-47d4-bff1-6e845898f3e1" />
