from enum import Enum

class MonitorStatus(str, Enum):
    Active = "active",
    Inactive = "inactive",
    InactivatedBySystem = "inactivatedBySystem",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

