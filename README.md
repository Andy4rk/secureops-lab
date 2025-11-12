# secureops-lab
Home lab project to simulate RMF-compliant cybersecurity operations for defense environments.

# Project Goals
- Simulate a secure enterprise network with virtualized systems
- Automate STIG assessments and framework compliance tracking
- Perform threat modeling and vulnerability analysis
- Integrate DevSecOps pipelines with security scanning
- Map lab components in accordance with NIST 800-53 controls and RMF phases

# Lab Architecture
- Proxmox VE hypervisor on Mini PC (Ryzen 9, 32GB RAM)
- VMs: Ubuntu1 (STIG scans), Ubuntu2 (Wazuh host), Kali (red team), Windows 11 (blue team), Flask app (CI/CD target)
- Containers: DevSecOps pipeline, dashboards, log aggregation

# Repo Structure
- 'docs/': RMF mappings, threat models, architecture diagrams
- 'infra/': Ansible playbooks, VM configs
- 'ci-cd/': GitHub Actions, Dockerfiles, Trivy scans
- 'scripts/': Python tools for automation and reporting
- 'dashboards/': Grafana, ELK, Wazuh configs

# Roadmap
- [X] Set up Proxmox and base VMs
- [X] Implement Wazuh Indexer, Server, and Dashboard
- [X] Configure agents on each endpoint for Wazuh SIEM
- [ ] Automate STIG scans with OpenSCAP
- [ ] Build threat models using OWASP Threat Dragon
- [ ] Integrate GitHub Actions + Trivy for DevSecOps
- [ ] Map controls to NIST 800-53 and RMF steps
- [ ] Create dashboards for compliance and threat visibility

# License
Apache 2.0
