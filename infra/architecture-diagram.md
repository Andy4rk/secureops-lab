mermaid


graph LR
  subgraph Proxmox Host
    U[Ubuntu Server<br/>Wazuh Manager + Single-Node]
    W[Windows 11 Endpoint]
    K1[Kali 1]
    K2[Kali 2]
  end

  U <-- Wazuh Agent --> U
  W <-- Wazuh Agent --> U
  K1 <-- Wazuh Agent --> U
  K2 <-- Wazuh Agent --> U

  Internet((Internet)) ---|apt/ms updates| U
  Internet ---|updates| W
