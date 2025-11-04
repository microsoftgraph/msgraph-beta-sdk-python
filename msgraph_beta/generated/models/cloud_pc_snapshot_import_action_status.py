from enum import Enum

class CloudPcSnapshotImportActionStatus(str, Enum):
    Pending = "pending",
    InProgress = "inProgress",
    Succeeded = "succeeded",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

