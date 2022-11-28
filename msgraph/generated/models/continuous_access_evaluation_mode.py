from enum import Enum

class ContinuousAccessEvaluationMode(Enum):
    StrictEnforcement = "strictEnforcement",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",

