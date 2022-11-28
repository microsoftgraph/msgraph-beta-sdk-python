from enum import Enum

class OverrideOption(Enum):
    NotAllowed = "notAllowed",
    AllowFalsePositiveOverride = "allowFalsePositiveOverride",
    AllowWithJustification = "allowWithJustification",
    AllowWithoutJustification = "allowWithoutJustification",

