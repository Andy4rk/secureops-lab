# RMF Control Mapping for SecureOps Lab

This document maps lab components to NIST SP 800-53 Rev. 5 controls and RMF lifecycle steps. 
It demonstrates how each system, tool, and process in the SecureOps Lab supports cybersecurity compliance and operational assurance.

---

## RMF Lifecycle Phases

| Phase | Description |
|-------|-------------|
| **1. Categorize** | Define impact levels and system boundaries |
| **2. Select**     | Choose baseline controls (e.g., Low/Moderate/High) |
| **3. Implement**  | Configure technical and procedural safeguards |
| **4. Assess**     | Evaluate control effectiveness (e.g., STIG scans, OpenSCAP) |
| **5. Authorize**  | Document risk posture and obtain ATO |
| **6. Monitor**    | Continuously assess and respond to changes |

---

## Control Mapping Table

| Control ID | Control Name | Lab Component | Implementation Notes |
|------------|--------------|----------------|-----------------------|
| AC-2       | Account Management | Ubuntu Server | Enforce least privilege, audit user creation |
| SI-2       | Flaw Remediation | OpenSCAP, Ansible | Automate STIG patching and version tracking |
| SC-7       | Boundary Protection | pfSense VM | Simulate firewall rules and DMZ segmentation |
| AU-6       | Audit Review | ELK Stack | Centralized log aggregation and alerting |
| CA-7       | Continuous Monitoring | Grafana + Wazuh | Visualize compliance drift and threat activity |
| RA-5       | Vulnerability Scanning | OpenVAS, Nessus (external) | Scan internal assets and report CVSS scores |
| SA-11      | Developer Security Testing | GitHub Actions + Trivy | Scan containers and code during CI/CD |

---

## Notes
- This mapping will evolve as lab components are deployed and refined.
- Controls are selected based on a **Moderate baseline** for DoD systems.
- Additional mappings will be added for alignment with additional concepts.

---

## References
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [RMF Overview (NIST)](https://csrc.nist.gov/publications/detail/sp/800-37/rev-2/final)
- [DISA STIG Portal](https://public.cyber.mil/stigs/)
