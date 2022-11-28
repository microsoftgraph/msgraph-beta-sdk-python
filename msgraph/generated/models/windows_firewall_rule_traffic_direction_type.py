from enum import Enum

class WindowsFirewallRuleTrafficDirectionType(Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # The rule applies to outbound traffic.
    Out = "out",
    # The rule applies to inbound traffic.
    In_escaped = "in",

