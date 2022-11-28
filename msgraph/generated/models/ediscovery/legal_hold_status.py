from enum import Enum

class LegalHoldStatus(Enum):
    Pending = "Pending",
    Error = "Error",
    Success = "Success",
    UnknownFutureValue = "UnknownFutureValue",

