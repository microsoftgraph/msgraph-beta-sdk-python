from enum import Enum

class EducationSynchronizationStatus(Enum):
    Paused = "paused",
    InProgress = "inProgress",
    Success = "success",
    Error = "error",
    ValidationError = "validationError",
    Quarantined = "quarantined",
    UnknownFutureValue = "unknownFutureValue",
    Extracting = "extracting",
    Validating = "validating",

