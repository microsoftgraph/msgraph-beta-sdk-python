from enum import Enum

class RuleSeverityType(Enum):
    Unknown = "unknown",
    Informational = "informational",
    Warning = "warning",
    Critical = "critical",
    UnknownFutureValue = "unknownFutureValue",

