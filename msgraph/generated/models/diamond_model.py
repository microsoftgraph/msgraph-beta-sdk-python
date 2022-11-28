from enum import Enum

class DiamondModel(Enum):
    Unknown = "unknown",
    Adversary = "adversary",
    Capability = "capability",
    Infrastructure = "infrastructure",
    Victim = "victim",
    UnknownFutureValue = "unknownFutureValue",

