from enum import Enum

class CloudPcStorageAccountAccessTier(str, Enum):
    Hot = "hot",
    Cool = "cool",
    Premium = "premium",
    Cold = "cold",
    UnknownFutureValue = "unknownFutureValue",

