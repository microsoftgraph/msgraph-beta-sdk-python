from enum import Enum

class HostReputationClassification(Enum):
    Unknown = "unknown",
    Neutral = "neutral",
    Suspicious = "suspicious",
    Malicious = "malicious",
    UnknownFutureValue = "unknownFutureValue",

