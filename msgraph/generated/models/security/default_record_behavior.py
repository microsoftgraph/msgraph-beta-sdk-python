from enum import Enum

class DefaultRecordBehavior(Enum):
    StartLocked = "startLocked",
    StartUnlocked = "startUnlocked",
    UnknownFutureValue = "unknownFutureValue",

