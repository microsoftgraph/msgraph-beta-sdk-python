from enum import Enum

class ChangeItemState(str, Enum):
    Available = "available",
    ComingSoon = "comingSoon",
    UnknownFutureValue = "unknownFutureValue",

