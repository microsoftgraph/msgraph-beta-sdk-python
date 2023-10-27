from enum import Enum

class CloudPcAuditActivityResult(str, Enum):
    Success = "success",
    ClientError = "clientError",
    Failure = "failure",
    Timeout = "timeout",
    Other = "other",

