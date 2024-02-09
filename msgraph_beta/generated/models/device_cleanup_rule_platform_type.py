from enum import Enum

class DeviceCleanupRulePlatformType(str, Enum):
    # Default. Indicates that clean up rule is associated with all managed device platforms.
    All = "all",
    # Indicates that clean up rule is associated with Android open source project managed device platforms.
    AndroidAOSP = "androidAOSP",
    # Indicates that clean up rule is associated with Android device administrator managed device platforms.
    AndroidDeviceAdministrator = "androidDeviceAdministrator",
    # Indicates that clean up rule is associated with Android dedicated and fully managed and Corporate Owned Work Profile managed device platforms.
    AndroidDedicatedAndFullyManagedCorporateOwnedWorkProfile = "androidDedicatedAndFullyManagedCorporateOwnedWorkProfile",
    # Indicates that clean up rule is associated with ChromeOS managed device platforms.
    ChromeOS = "chromeOS",
    # Indicates that clean up rule is associated with Android personally owned work profile managed device platforms.
    AndroidPersonallyOwnedWorkProfile = "androidPersonallyOwnedWorkProfile",
    # Indicates that clean up rule is associated with IOS managed device platforms.
    Ios = "ios",
    # Indicates that clean up rule is associated with MacOS managed device platforms.
    MacOS = "macOS",
    # Indicates that clean up rule is associated with Windows managed device platforms.
    Windows = "windows",
    # Indicates that clean up rule is associated with Windows Holographic managed device platforms.
    WindowsHolographic = "windowsHolographic",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

