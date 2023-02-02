from enum import Enum

class ActionAfterRetentionPeriod(Enum):
    None_ = "none",
    Delete = "delete",
    StartDispositionReview = "startDispositionReview",
    Relabel = "relabel",
    UnknownFutureValue = "unknownFutureValue",

