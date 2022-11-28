from enum import Enum

class DevicePlatformType(Enum):
    # Android.
    Android = "android",
    # AndroidForWork.
    AndroidForWork = "androidForWork",
    # iOS.
    IOS = "iOS",
    # MacOS.
    MacOS = "macOS",
    # WindowsPhone 8.1.
    WindowsPhone81 = "windowsPhone81",
    # Windows 8.1 and later
    Windows81AndLater = "windows81AndLater",
    # Windows 10 and later.
    Windows10AndLater = "windows10AndLater",
    # Android Work Profile.
    AndroidWorkProfile = "androidWorkProfile",
    # Unknown.
    Unknown = "unknown",
    # Android AOSP.
    AndroidAOSP = "androidAOSP",

