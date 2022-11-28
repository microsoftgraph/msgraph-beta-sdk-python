from enum import Enum

class WorkloadActionStatus(Enum):
    ToAddress = "toAddress",
    Completed = "completed",
    Error = "error",
    TimeOut = "timeOut",
    InProgress = "inProgress",
    UnknownFutureValue = "unknownFutureValue",

