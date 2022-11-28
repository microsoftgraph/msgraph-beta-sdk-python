from enum import Enum

class QualityUpdateClassification(Enum):
    All = "all",
    Security = "security",
    NonSecurity = "nonSecurity",
    UnknownFutureValue = "unknownFutureValue",

