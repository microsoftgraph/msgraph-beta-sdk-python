from enum import Enum

class SensitivityLabelAssignmentMethod(Enum):
    Standard = "standard",
    Privileged = "privileged",
    Auto = "auto",
    UnknownFutureValue = "unknownFutureValue",

