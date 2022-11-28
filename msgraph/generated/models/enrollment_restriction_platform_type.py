from enum import Enum

class EnrollmentRestrictionPlatformType(Enum):
    # Applies to all platforms
    AllPlatforms = "allPlatforms",
    # iOS/iPadOS devices
    Ios = "ios",
    # Windows devices
    Windows = "windows",
    # Windows Phone devices
    WindowsPhone = "windowsPhone",
    # Android devices
    Android = "android",
    # Android for Work devices
    AndroidForWork = "androidForWork",
    # macOS devices
    Mac = "mac",

