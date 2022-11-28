from enum import Enum

class AndroidForWorkVpnConnectionType(Enum):
    # Cisco AnyConnect.
    CiscoAnyConnect = "ciscoAnyConnect",
    # Pulse Secure.
    PulseSecure = "pulseSecure",
    # F5 Edge Client.
    F5EdgeClient = "f5EdgeClient",
    # Dell SonicWALL Mobile Connection.
    DellSonicWallMobileConnect = "dellSonicWallMobileConnect",
    # Check Point Capsule VPN.
    CheckPointCapsuleVpn = "checkPointCapsuleVpn",
    # Citrix
    Citrix = "citrix",

