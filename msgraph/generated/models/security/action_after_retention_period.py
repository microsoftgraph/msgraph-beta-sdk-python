from enum import Enum

class ActionAfterRetentionPeriod(Enum):
    None_escaped = "none",
    Delete = "delete",
    StartDispositionReview = "startDispositionReview",
    Relabel = "relabel",
    UnknownFutureValue = "unknownFutureValue",

