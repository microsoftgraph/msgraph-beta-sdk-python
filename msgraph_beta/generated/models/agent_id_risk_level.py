from enum import Enum

class AgentIdRiskLevel(str, Enum):
    None_ = "none",
    Low = "low",
    Medium = "medium",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

