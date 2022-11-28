from enum import Enum

class RestoreTimeRange(Enum):
    Before = "before",
    After = "after",
    BeforeOrAfter = "beforeOrAfter",
    UnknownFutureValue = "unknownFutureValue",

