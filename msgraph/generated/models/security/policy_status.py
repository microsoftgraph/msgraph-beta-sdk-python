from enum import Enum

class PolicyStatus(Enum):
    Pending = "pending",
    Error = "error",
    Success = "success",
    UnknownFutureValue = "unknownFutureValue",

