from enum import Enum

class ConfirmedBy(Enum):
    None_escaped = "none",
    User = "user",
    Manager = "manager",
    UnknownFutureValue = "unknownFutureValue",

