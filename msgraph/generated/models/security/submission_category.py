from enum import Enum

class SubmissionCategory(Enum):
    NotJunk = "notJunk",
    Spam = "spam",
    Phishing = "phishing",
    Malware = "malware",
    UnknownFutureValue = "unknownFutureValue",

