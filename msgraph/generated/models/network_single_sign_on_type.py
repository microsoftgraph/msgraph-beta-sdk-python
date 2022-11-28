from enum import Enum

class NetworkSingleSignOnType(Enum):
    # Disabled
    Disabled = "disabled",
    # Pre-Logon
    Prelogon = "prelogon",
    # Post-Logon
    Postlogon = "postlogon",

