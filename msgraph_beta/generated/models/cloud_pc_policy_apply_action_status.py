from enum import Enum

class CloudPcPolicyApplyActionStatus(str, Enum):
    Processing = "processing",
    Succeeded = "succeeded",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

