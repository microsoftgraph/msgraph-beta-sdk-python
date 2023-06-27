from enum import Enum

class RegistryHive(str, Enum):
    Unknown = "unknown",
    CurrentConfig = "currentConfig",
    CurrentUser = "currentUser",
    LocalMachineSam = "localMachineSam",
    LocalMachineSecurity = "localMachineSecurity",
    LocalMachineSoftware = "localMachineSoftware",
    LocalMachineSystem = "localMachineSystem",
    UsersDefault = "usersDefault",
    UnknownFutureValue = "unknownFutureValue",

