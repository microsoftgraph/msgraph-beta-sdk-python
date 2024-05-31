from enum import Enum

class ThreatSeverity(str, Enum):
    Informational = "informational",
    Low = "low",
    Medium = "medium",
    High = "high",
    Critical = "critical",
    UnknownFutureValue = "unknownFutureValue",

