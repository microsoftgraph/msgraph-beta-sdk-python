from enum import Enum

class AndroidPermissionActionType(Enum):
    Prompt = "prompt",
    AutoGrant = "autoGrant",
    AutoDeny = "autoDeny",

