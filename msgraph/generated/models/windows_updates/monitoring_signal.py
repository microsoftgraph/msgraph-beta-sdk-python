from enum import Enum

class MonitoringSignal(str, Enum):
    Rollback = "rollback",
    UnknownFutureValue = "unknownFutureValue",

