from enum import Enum

class WiFiSecurityType(Enum):
    # Open (No Authentication).
    Open = "open",
    # WPA-Personal.
    WpaPersonal = "wpaPersonal",
    # WPA-Enterprise. Must use IOSEnterpriseWifiConfiguration type to configure enterprise options.
    WpaEnterprise = "wpaEnterprise",
    # WEP Encryption.
    Wep = "wep",
    # WPA2-Personal.
    Wpa2Personal = "wpa2Personal",
    # WPA2-Enterprise. Must use WindowsWifiEnterpriseEAPConfiguration type to configure enterprise options.
    Wpa2Enterprise = "wpa2Enterprise",

