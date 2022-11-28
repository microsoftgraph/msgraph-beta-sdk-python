from enum import Enum

class AppleUserInitiatedEnrollmentType(Enum):
    # Unknown enrollment type
    Unknown = "unknown",
    # Device enrollment type
    Device = "device",
    # User enrollment type
    User = "user",

