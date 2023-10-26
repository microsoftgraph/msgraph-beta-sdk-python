from enum import Enum

class frontlineCloudPcAccessState(str, Enum):
    Unassigned = "unassigned",
    NoLicensesAvailable = "noLicensesAvailable",
    ActivationFailed = "activationFailed",
    Active = "active",
    Activating = "activating",
    StandbyMode = "standbyMode",
    UnknownFutureValue = "unknownFutureValue",

