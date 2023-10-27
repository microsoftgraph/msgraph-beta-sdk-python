from enum import Enum

class UpdateCategory(str, Enum):
    Feature = "feature",
    Quality = "quality",
    UnknownFutureValue = "unknownFutureValue",
    Driver = "driver",

