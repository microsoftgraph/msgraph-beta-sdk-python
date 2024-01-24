from enum import Enum

class ThreatType(str, Enum):
    Unknown = "unknown",
    Spam = "spam",
    Malware = "malware",
    Phishing = "phishing",
    None_ = "none",
    UnknownFutureValue = "unknownFutureValue",

