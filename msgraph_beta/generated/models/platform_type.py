from enum import Enum

class PlatformType(str, Enum):
    # None Platform Type
    None_ = "none",
    # Android Platform Type
    Android = "android",
    # Android Enterprise Platform Type
    AndroidEnterprise = "androidEnterprise",
    # iOS Platform Type
    IOS = "iOS",
    # MacOS Platform Type
    MacOS = "macOS",
    # Windows 10X Platform Type
    Windows10X = "windows10X",
    # Windows 10 Platform Type
    Windows10 = "windows10",

