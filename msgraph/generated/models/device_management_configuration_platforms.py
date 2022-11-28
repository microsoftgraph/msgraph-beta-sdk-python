from enum import Enum

class DeviceManagementConfigurationPlatforms(Enum):
    # None.
    None_escaped = "none",
    # Android.
    Android = "android",
    # iOS.
    IOS = "iOS",
    # MacOS.
    MacOS = "macOS",
    # Windows 10 X.
    Windows10X = "windows10X",
    # Windows 10.
    Windows10 = "windows10",
    # Linux.
    Linux = "linux",
    # Sentinel member for cases where the client cannot handle the new enum values.
    UnknownFutureValue = "unknownFutureValue",

