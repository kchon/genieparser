expected_output = {
    "interfaces": {
        "Control0/0": {
            "ipv4": {"10.10.1.1": {"ip": "10.10.1.1"}},
            "check": "YES",
            "method": "CONFIG",
            "link_status": "up",
            "line_protocol": "up",
        },
        "GigabitEthernet0/0": {
            "ipv4": {"10.10.1.1": {"ip": "10.10.1.1"}},
            "check": "YES",
            "method": "CONFIG",
            "link_status": "up",
            "line_protocol": "up",
        },
        "GigabitEthernet0/1": {
            "ipv4": {"unnumbered": {"unnumbered_intf_ref": "unassigned"}},
            "check": "YES",
            "method": "unset admin",
            "link_status": "down",
            "line_protocol": "down",
        },
        "GigabitEthernet0/2": {
            "ipv4": {"10.10.1.1": {"ip": "10.10.1.1"}},
            "check": "YES",
            "method": "manual admin",
            "link_status": "down",
            "line_protocol": "down",
        },
        "GigabitEthernet0/3": {
            "ipv4": {"10.10.1.1": {"ip": "10.10.1.1"}},
            "check": "YES",
            "method": "DHCP admin",
            "link_status": "down",
            "line_protocol": "down",
        },
        "Management0/0": {
            "ipv4": {"10.10.1.1": {"ip": "10.10.1.1"}},
            "check": "YES",
            "method": "CONFIG",
            "link_status": "up",
        },
        "Vlan150": {
            "ipv4": {"10.10.1.1": {"ip": "10.10.1.1"}},
            "check": "YES",
            "method": "CONFIG",
            "link_status": "up",
            "line_protocol": "up",
        },
        "Vlan160": {
            "ipv4": {"10.10.1.1": {"ip": "10.10.1.1"}},
            "check": "YES",
            "method": "CONFIG",
            "link_status": "down",
            "line_protocol": "down",
        },
        "Vlan170": {
            "ipv4": {"unnumbered": {"unnumbered_intf_ref": "unassigned"}},
            "check": "YES",
            "method": "unset",
            "link_status": "up",
            "line_protocol": "up",
        },
    }
}
