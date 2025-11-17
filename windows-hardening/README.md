# Windows 11 Hardening

This directory documents how the Windows 11 endpoint in the lab is hardened and how those changes are validated through SCA / OSCAP and Wazuh.

## System Overview

- **OS:** Windows 11
- **Role:** Blue-team workstation / hardening target
- **Monitoring:** Wazuh agent installed and reporting to the Ubuntu-based Wazuh manager

## Hardening Focus Areas

The current hardening work is focused on:

1. **Account and Password Policies**
   - Minimum password length
   - Password complexity
   - Maximum password age
   - Account lockout threshold and duration

2. **Interactive Logon and Session Controls**
   - Interactive logon messages (where applicable)
   - Idle timeout / screen lock behavior

3. **Audit Policy**
   - Logon / logoff events
   - Account management
   - Policy changes and privilege use

4. **Baseline vs Hardened State**
   - Capturing the “before” configuration where possible
   - Documenting the final, hardened settings

## Validation

Hardening changes are validated using:

- **Wazuh SCA checks** against Windows security baselines
- **OSCAP / benchmark scans** where supported
- **Windows Event Logs**, forwarded to Wazuh, for:
  - Successful and failed logons
  - Lockout events
  - Policy changes

Relevant screenshots (initial scan results, policy checks, etc.) are stored in:

- `../docs/screenshots/`

## Planned Documentation

Planned files in this directory:

- `baseline-settings.md` – summary of the initial Windows configuration
- `hardened-settings.md` – final settings after hardening, with notes
- `policy-changes.md` – specific Local Security Policy / Group Policy changes

As the hardening process is refined, these files will be updated to show:

- Exact settings that were changed
- Why the setting was chosen
- How the change is detected by Wazuh / SCA
