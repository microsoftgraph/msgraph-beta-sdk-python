from enum import Enum

class WindowsInformationProtectionPinCharacterRequirements(str, Enum):
    # Not allow
    NotAllow = "notAllow",
    # Require atleast one
    RequireAtLeastOne = "requireAtLeastOne",
    # Allow any number
    Allow = "allow",

