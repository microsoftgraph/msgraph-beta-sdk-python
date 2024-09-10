from enum import Enum

class PlatformType(str, Enum):
    # None
    None_ = "none",
    # Android
    Android = "android",
    # iOS
    IOS = "iOS",
    # MacOS
    MacOS = "macOS",
    # Windows 10X Platform Type
    Windows10X = "windows10X",
    # Windows 10
    Windows10 = "windows10",
    # Linux
    Linux = "linux",
    # UnknownFutureValue
    UnknownFutureValue = "unknownFutureValue",
    # AndroidEnterprise
    AndroidEnterprise = "androidEnterprise",
    # Android Open Source Project
    Aosp = "aosp",

