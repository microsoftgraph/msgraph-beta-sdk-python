from enum import Enum

class CloudPcManagementService(str, Enum):
    Windows365 = "windows365",
    DevBox = "devBox",
    UnknownFutureValue = "unknownFutureValue",
    RpaBox = "rpaBox",

