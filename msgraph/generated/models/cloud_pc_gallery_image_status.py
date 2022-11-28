from enum import Enum

class CloudPcGalleryImageStatus(Enum):
    Supported = "supported",
    SupportedWithWarning = "supportedWithWarning",
    NotSupported = "notSupported",
    UnknownFutureValue = "unknownFutureValue",

