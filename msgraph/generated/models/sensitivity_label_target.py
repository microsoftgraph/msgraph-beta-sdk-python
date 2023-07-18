from enum import Enum

class SensitivityLabelTarget(str, Enum):
    Email = "email",
    Site = "site",
    UnifiedGroup = "unifiedGroup",
    UnknownFutureValue = "unknownFutureValue",
    Teamwork = "teamwork",

