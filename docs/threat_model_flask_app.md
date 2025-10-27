# Threat Model: Flask Web Application

This document outlines the threat model for a containerized Flask web application deployed in the SecureOps Lab. It identifies assets, potential threats, mitigations, and maps techniques to MITRE ATT&CK.

---

## System Overview

- **App Type:** Flask web application
- **Deployment:** Docker container via GitHub Actions
- **Exposure:** Accessible from internal lab network (simulated DMZ)
- **Purpose:** Demonstrate DevSecOps pipeline and security integration

---

## Assets

| Asset | Description |
|-------|-------------|
| Source Code | Python files, templates, configs |
| Container Image | Built via CI/CD pipeline |
| Secrets | API keys, DB credentials |
| Web Interface | Flask routes and endpoints |
| Logs | Application and access logs |

---

## Threats

| Threat | Description | MITRE Technique |
|--------|-------------|------------------|
| Code Injection | Malicious input via web forms | T1059 (Command and Scripting Interpreter) |
| Credential Exposure | Secrets hardcoded or leaked in logs | T1552 (Unsecured Credentials) |
| Container Escape | Attacker breaks out of container | T1611 (Escape to Host) |
| Supply Chain Attack | Compromised dependency in `requirements.txt` | T1195 (Supply Chain Compromise) |
| Insecure Deserialization | Exploiting unsafe object loading | T1505.002 (Web Shell) |
| Log Poisoning | Manipulating logs to hide activity | T1564.003 (Log Tampering) |

---

## Mitigations

| Threat | Mitigation |
|--------|------------|
| Code Injection | Input validation, use of Flask-WTF |
| Credential Exposure | Use `.env` files, GitHub secrets, avoid hardcoding |
| Container Escape | Use minimal base images, apply seccomp profiles |
| Supply Chain Attack | Pin dependencies, use `pip-audit` or `Safety` |
| Insecure Deserialization | Avoid `pickle`, use safe serializers |
| Log Poisoning | Centralized logging with Wazuh or ELK, integrity checks |

---

## References

- [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)
- [MITRE ATT&CK Navigator](https://attack.mitre.org/)
- [Flask Security Best Practices](https://flask.palletsprojects.com/en/latest/security/)
