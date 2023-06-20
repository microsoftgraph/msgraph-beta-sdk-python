from enum import Enum

class CloudPcDeviceImageStatusDetails(str, Enum):
    InternalServerError = "internalServerError",
    SourceImageNotFound = "sourceImageNotFound",
    OsVersionNotSupported = "osVersionNotSupported",
    SourceImageInvalid = "sourceImageInvalid",
    SourceImageNotGeneralized = "sourceImageNotGeneralized",
    UnknownFutureValue = "unknownFutureValue",

