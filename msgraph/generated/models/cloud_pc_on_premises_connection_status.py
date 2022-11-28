from enum import Enum

class CloudPcOnPremisesConnectionStatus(Enum):
    Pending = "pending",
    Running = "running",
    Passed = "passed",
    Failed = "failed",
    Warning = "warning",
    UnknownFutureValue = "unknownFutureValue",

