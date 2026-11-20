from enum import Enum

class CloudPcFlexAccessState(str, Enum):
    Unassigned = "unassigned",
    ActivationFailed = "activationFailed",
    Active = "active",
    Activating = "activating",
    StandbyMode = "standbyMode",
    UnknownFutureValue = "unknownFutureValue",

