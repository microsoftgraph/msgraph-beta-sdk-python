from enum import Enum

class CloudPcConnectivityStatus(Enum):
    Unknown = "unknown",
    Available = "available",
    AvailableWithWarning = "availableWithWarning",
    Unavailable = "unavailable",
    UnknownFutureValue = "unknownFutureValue",

