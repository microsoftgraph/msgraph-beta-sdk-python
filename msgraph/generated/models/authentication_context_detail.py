from enum import Enum

class AuthenticationContextDetail(Enum):
    Required = "required",
    PreviouslySatisfied = "previouslySatisfied",
    NotApplicable = "notApplicable",
    UnknownFutureValue = "unknownFutureValue",

