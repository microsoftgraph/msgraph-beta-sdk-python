from enum import Enum

class SubmissionResultCategory(Enum):
    NotJunk = "notJunk",
    Spam = "spam",
    Phishing = "phishing",
    Malware = "malware",
    AllowedByPolicy = "allowedByPolicy",
    BlockedByPolicy = "blockedByPolicy",
    Spoof = "spoof",
    Unknown = "unknown",
    NoResultAvailable = "noResultAvailable",
    UnknownFutureValue = "unknownFutureValue",

