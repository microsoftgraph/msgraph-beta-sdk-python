from enum import Enum

class DeviceRiskScore(Enum):
    None_ = "none",
    Informational = "informational",
    Low = "low",
    Medium = "medium",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

