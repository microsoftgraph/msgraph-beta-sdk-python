from enum import Enum

class TiAction(Enum):
    Unknown = "unknown",
    Allow = "allow",
    Block = "block",
    Alert = "alert",
    UnknownFutureValue = "unknownFutureValue",

