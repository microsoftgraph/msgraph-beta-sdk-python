from enum import Enum

class AospWifiSecurityType(Enum):
    # No security type.
    None_escaped = "none",
    # WPA-Pre-shared-key
    Wpa = "wpa",
    # WEP-Pre-shared-key
    Wep = "wep",

