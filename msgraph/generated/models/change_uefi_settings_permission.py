from enum import Enum

class ChangeUefiSettingsPermission(Enum):
    # Device default value, no intent.
    NotConfiguredOnly = "notConfiguredOnly",
    # Prevent change of UEFI setting permission
    None_escaped = "none",

