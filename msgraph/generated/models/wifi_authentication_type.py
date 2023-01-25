from enum import Enum

class WifiAuthenticationType(Enum):
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

