from enum import Enum

class CloudPcResizeValidationCode(Enum):
    Success = "success",
    CloudPcNotFound = "cloudPcNotFound",
    OperationConflict = "operationConflict",
    OperationNotSupported = "operationNotSupported",
    TargetLicenseHasAssigned = "targetLicenseHasAssigned",
    InternalServerError = "internalServerError",
    UnknownFutureValue = "unknownFutureValue",

