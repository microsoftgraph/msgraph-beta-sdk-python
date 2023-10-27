from enum import Enum

class shiftWorkCloudPcAccessState(str, Enum):
    Unassigned = "unassigned",
    NoLicensesAvailable = "noLicensesAvailable",
    ActivationFailed = "activationFailed",
    Active = "active",
    Activating = "activating",
    UnknownFutureValue = "unknownFutureValue",
    StandbyMode = "standbyMode",

