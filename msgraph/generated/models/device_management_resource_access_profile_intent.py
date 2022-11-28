from enum import Enum

class DeviceManagementResourceAccessProfileIntent(Enum):
    # Apply the profile.
    Apply = "apply",
    # Remove the profile from devices that have installed the profile.
    Remove = "remove",

