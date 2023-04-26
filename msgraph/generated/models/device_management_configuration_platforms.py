from enum import Enum

class DeviceManagementConfigurationPlatforms(Enum):
    # Default. No platform type specified.
    None_ = "none",
    # Settings for Android platform.
    Android = "android",
    # Settings for iOS platform.
    IOS = "iOS",
    # Settings for MacOS platform.
    MacOS = "macOS",
    # Windows 10 X.
    Windows10X = "windows10X",
    # Settings for Windows 10 platform.
    Windows10 = "windows10",
    # Settings for Linux platform.
    Linux = "linux",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

