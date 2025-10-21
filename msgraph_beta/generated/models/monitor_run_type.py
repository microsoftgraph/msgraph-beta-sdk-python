from enum import Enum

class MonitorRunType(str, Enum):
    Monitor = "monitor",
    Apply = "apply",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

