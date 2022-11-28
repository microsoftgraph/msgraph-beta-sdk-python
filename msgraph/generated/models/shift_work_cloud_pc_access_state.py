from enum import Enum

class ShiftWorkCloudPcAccessState(Enum):
    Unassigned = "unassigned",
    NoLicensesAvailable = "noLicensesAvailable",
    ActivationFailed = "activationFailed",
    Active = "active",
    Activating = "activating",
    Waitlisted = "waitlisted",
    UnknownFutureValue = "unknownFutureValue",

