from enum import Enum

class AlertStatusType(Enum):
    Active = "active",
    Resolved = "resolved",
    UnknownFutureValue = "unknownFutureValue",

