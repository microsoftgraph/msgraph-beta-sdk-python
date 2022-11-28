from enum import Enum

class RoleAssignmentScopeType(Enum):
    # Allow assignments to the specified ResourceScopes.
    ResourceScope = "resourceScope",
    # Allow assignments to all Intune devices.
    AllDevices = "allDevices",
    # Allow assignments to all Intune licensed users.
    AllLicensedUsers = "allLicensedUsers",
    # Allow assignments to all Intune devices and licensed users.
    AllDevicesAndLicensedUsers = "allDevicesAndLicensedUsers",

