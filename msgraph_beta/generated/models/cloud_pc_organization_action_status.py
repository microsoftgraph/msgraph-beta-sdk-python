from enum import Enum

class CloudPcOrganizationActionStatus(str, Enum):
    InProgress = "inProgress",
    Succeeded = "succeeded",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

