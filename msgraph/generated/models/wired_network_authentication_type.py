from enum import Enum

class WiredNetworkAuthenticationType(str, Enum):
    # None
    None_ = "none",
    # User Authentication
    User = "user",
    # Machine Authentication
    Machine = "machine",
    # Machine or User Authentication
    MachineOrUser = "machineOrUser",
    # Guest Authentication
    Guest = "guest",
    # Sentinel member for cases where the client cannot handle the new enum values.
    UnknownFutureValue = "unknownFutureValue",

