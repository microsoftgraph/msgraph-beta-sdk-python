from enum import Enum

class WindowsFirewallRuleNetworkProfileTypes(Enum):
    # No flags set.
    NotConfigured = "notConfigured",
    # The profile for networks that are connected to domains.
    Domain = "domain",
    # The profile for private networks.
    Private = "private",
    # The profile for public networks.
    Public = "public",

