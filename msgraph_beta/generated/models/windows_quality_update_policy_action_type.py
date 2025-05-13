from enum import Enum

class WindowsQualityUpdatePolicyActionType(str, Enum):
    # Enum value to represent the approval actions for quality update
    Approve = "approve",
    # Enum value to represent the pause actions for quality update
    Suspend = "suspend",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

