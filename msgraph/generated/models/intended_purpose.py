from enum import Enum

class IntendedPurpose(Enum):
    # Unassigned
    Unassigned = "unassigned",
    # SmimeEncryption
    SmimeEncryption = "smimeEncryption",
    # SmimeSigning
    SmimeSigning = "smimeSigning",
    # VPN
    Vpn = "vpn",
    # Wifi
    Wifi = "wifi",

