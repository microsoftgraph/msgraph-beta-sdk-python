from enum import Enum

class CloudPcDeviceImageStatusDetails(Enum):
    InternalServerError = "internalServerError",
    SourceImageNotFound = "sourceImageNotFound",
    OsVersionNotSupported = "osVersionNotSupported",
    SourceImageInvalid = "sourceImageInvalid",
    SourceImageNotGeneralized = "sourceImageNotGeneralized",
    UnknownFutureValue = "unknownFutureValue",

