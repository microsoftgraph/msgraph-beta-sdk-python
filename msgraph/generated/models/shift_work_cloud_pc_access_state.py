from enum import Enum

class ShiftWorkCloudPcAccessState(str, Enum):
    Unassigned = "unassigned",
    NoLicensesAvailable = "noLicensesAvailable",
    ActivationFailed = "activationFailed",
    Active = "active",
    Activating = "activating",
    UnknownFutureValue = "unknownFutureValue",
    StandbyMode = "standbyMode",

