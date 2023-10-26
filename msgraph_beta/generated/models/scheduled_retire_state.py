from enum import Enum

class ScheduledRetireState(str, Enum):
    # CancelRetire
    CancelRetire = "cancelRetire",
    # ConfirmRetire
    ConfirmRetire = "confirmRetire",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

