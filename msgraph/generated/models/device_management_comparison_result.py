from enum import Enum

class DeviceManagementComparisonResult(str, Enum):
    # Unknown setting comparison
    Unknown = "unknown",
    # The setting values are equal
    Equal = "equal",
    # The setting values are not equal
    NotEqual = "notEqual",
    # The setting is added
    Added = "added",
    # The setting is removed
    Removed = "removed",

