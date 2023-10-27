from enum import Enum

class PstnUserBlockMode(str, Enum):
    Blocked = "blocked",
    Unblocked = "unblocked",
    UnknownFutureValue = "unknownFutureValue",

