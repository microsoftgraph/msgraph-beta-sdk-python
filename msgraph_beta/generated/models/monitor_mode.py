from enum import Enum

class MonitorMode(str, Enum):
    MonitorOnce = "monitorOnce",
    MonitorOnly = "monitorOnly",
    ApplyOnceAndMonitorContinuous = "applyOnceAndMonitorContinuous",
    ApplyOnce = "applyOnce",
    ApplyContinuous = "applyContinuous",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

