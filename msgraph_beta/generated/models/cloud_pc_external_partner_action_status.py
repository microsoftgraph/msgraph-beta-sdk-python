from enum import Enum

class CloudPcExternalPartnerActionStatus(str, Enum):
    Created = "created",
    Pending = "pending",
    Canceled = "canceled",
    Running = "running",
    Succeeded = "succeeded",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

