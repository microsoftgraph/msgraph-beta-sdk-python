from enum import Enum

class PolicyScope(Enum):
    None_escaped = "none",
    All = "all",
    Selected = "selected",
    UnknownFutureValue = "unknownFutureValue",

