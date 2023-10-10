from enum import Enum

class FrontlineCloudPcAccessState(str, Enum):
    Unassigned = "unassigned",
    NoLicensesAvailable = "noLicensesAvailable",
    ActivationFailed = "activationFailed",
    Active = "active",
    Activating = "activating",
    StandbyMode = "standbyMode",
    UnknownFutureValue = "unknownFutureValue",

