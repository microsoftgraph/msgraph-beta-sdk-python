from enum import Enum

class TimeCardState(Enum):
    ClockedIn = "clockedIn",
    OnBreak = "onBreak",
    ClockedOut = "clockedOut",
    UnknownFutureValue = "unknownFutureValue",

