from enum import Enum

class CloudPcExportJobStatus(Enum):
    NotStarted = "notStarted",
    InProgress = "inProgress",
    Completed = "completed",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

