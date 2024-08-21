from enum import Enum

class WorkplaceSensorEventType(str, Enum):
    BadgeIn = "badgeIn",
    BadgeOut = "badgeOut",
    UnknownFutureValue = "unknownFutureValue",

