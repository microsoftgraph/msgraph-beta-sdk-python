from enum import Enum

class AndroidForWorkDefaultAppPermissionPolicyType(Enum):
    # Device default value, no intent.
    DeviceDefault = "deviceDefault",
    # Prompt.
    Prompt = "prompt",
    # Auto grant.
    AutoGrant = "autoGrant",
    # Auto deny.
    AutoDeny = "autoDeny",

