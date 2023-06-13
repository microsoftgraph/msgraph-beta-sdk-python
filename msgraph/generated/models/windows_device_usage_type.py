from enum import Enum

class WindowsDeviceUsageType(str, Enum):
    # Single User Device Type
    SingleUser = "singleUser",
    # Shared Device Type
    Shared = "shared",

