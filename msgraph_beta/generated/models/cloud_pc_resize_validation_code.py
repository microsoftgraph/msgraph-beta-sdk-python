from enum import Enum

class CloudPcResizeValidationCode(str, Enum):
    Success = "success",
    CloudPcNotFound = "cloudPcNotFound",
    OperationConflict = "operationConflict",
    OperationNotSupported = "operationNotSupported",
    TargetLicenseHasAssigned = "targetLicenseHasAssigned",
    InternalServerError = "internalServerError",
    UnknownFutureValue = "unknownFutureValue",

