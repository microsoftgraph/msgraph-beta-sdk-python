from enum import Enum

class AndroidWiFiSecurityType(Enum):
    # Open (No Authentication).
    Open = "open",
    # WPA-Enterprise. Must use AndroidEnterpriseWifiConfiguration type to configure enterprise options.
    WpaEnterprise = "wpaEnterprise",
    # WPA2-Enterprise. Must use AndroidEnterpriseWifiConfiguration type to configure enterprise options.
    Wpa2Enterprise = "wpa2Enterprise",

