from enum import Enum

class FilteringPolicyAction(str, Enum):
    Block = "block",
    Allow = "allow",
    UnknownFutureValue = "unknownFutureValue",

