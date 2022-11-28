from enum import Enum

class CloudPcAuditActivityResult(Enum):
    Success = "success",
    ClientError = "clientError",
    Failure = "failure",
    Timeout = "timeout",
    Other = "other",

