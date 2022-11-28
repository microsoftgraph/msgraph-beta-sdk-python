from enum import Enum

class MigrationStatus(Enum):
    Ready = "ready",
    NeedsReview = "needsReview",
    AdditionalStepsRequired = "additionalStepsRequired",
    UnknownFutureValue = "unknownFutureValue",

