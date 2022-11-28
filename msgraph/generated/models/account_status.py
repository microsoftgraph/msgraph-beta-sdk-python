from enum import Enum

class AccountStatus(Enum):
    Unknown = "unknown",
    Staged = "staged",
    Active = "active",
    Suspended = "suspended",
    Deleted = "deleted",
    UnknownFutureValue = "unknownFutureValue",

