from enum import Enum

class DetectionSeverity(str, Enum):
    Low = "low",
    Medium = "medium",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

