from enum import Enum

class AppManagementLevel(Enum):
    # Unspecified
    Unspecified = "unspecified",
    # Unmanaged
    Unmanaged = "unmanaged",
    # MDM
    Mdm = "mdm",
    # Android Enterprise
    AndroidEnterprise = "androidEnterprise",
    # Android Enterprise dedicated devices with Azure AD Shared mode
    AndroidEnterpriseDedicatedDevicesWithAzureAdSharedMode = "androidEnterpriseDedicatedDevicesWithAzureAdSharedMode",
    # Android Open Source Project (AOSP) devices
    AndroidOpenSourceProjectUserAssociated = "androidOpenSourceProjectUserAssociated",
    # Android Open Source Project (AOSP) userless devices
    AndroidOpenSourceProjectUserless = "androidOpenSourceProjectUserless",
    # Place holder for evolvable enum
    UnknownFutureValue = "unknownFutureValue",

