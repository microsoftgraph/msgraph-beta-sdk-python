from enum import Enum

class ReportAction(str, Enum):
    Unknown = "unknown",
    Junk = "junk",
    NotJunk = "notJunk",
    Phish = "phish",
    UnknownFutureValue = "unknownFutureValue",

