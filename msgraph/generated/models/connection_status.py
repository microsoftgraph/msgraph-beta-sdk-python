from enum import Enum

class ConnectionStatus(str, Enum):
    Unknown = "unknown",
    Attempted = "attempted",
    Succeeded = "succeeded",
    Blocked = "blocked",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

