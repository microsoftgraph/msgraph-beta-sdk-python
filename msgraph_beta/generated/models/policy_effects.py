from enum import Enum

class PolicyEffects(str, Enum):
    Compliant = "compliant",
    Deny = "deny",
    UnknownFutureValue = "unknownFutureValue",

