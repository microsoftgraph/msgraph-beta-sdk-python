from enum import Enum

class MultiFactorAuthConfiguration(Enum):
    NotRequired = "notRequired",
    Required = "required",
    UnknownFutureValue = "unknownFutureValue",

