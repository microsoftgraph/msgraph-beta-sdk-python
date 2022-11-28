from enum import Enum

class CloudPcSupportedRegionStatus(Enum):
    Available = "available",
    Restricted = "restricted",
    Unavailable = "unavailable",
    UnknownFutureValue = "unknownFutureValue",

