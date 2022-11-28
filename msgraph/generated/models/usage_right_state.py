from enum import Enum

class UsageRightState(Enum):
    Active = "active",
    Inactive = "inactive",
    Warning = "warning",
    Suspended = "suspended",
    UnknownFutureValue = "unknownFutureValue",

