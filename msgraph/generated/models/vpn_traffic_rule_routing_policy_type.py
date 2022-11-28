from enum import Enum

class VpnTrafficRuleRoutingPolicyType(Enum):
    # No routing policy specified.
    None_escaped = "none",
    # Network traffic for the specified app will be routed through the VPN.
    SplitTunnel = "splitTunnel",
    # All network traffic will be routed through the VPN.
    ForceTunnel = "forceTunnel",

