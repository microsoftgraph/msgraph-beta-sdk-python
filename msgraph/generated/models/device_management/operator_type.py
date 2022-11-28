from enum import Enum

class OperatorType(Enum):
    GreaterOrEqual = "greaterOrEqual",
    Equal = "equal",
    Greater = "greater",
    Less = "less",
    LessOrEqual = "lessOrEqual",
    NotEqual = "notEqual",
    UnknownFutureValue = "unknownFutureValue",

