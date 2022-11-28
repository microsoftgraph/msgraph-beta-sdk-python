from enum import Enum

class EventPropagationStatus(Enum):
    None_escaped = "none",
    InProcessing = "inProcessing",
    Failed = "failed",
    Success = "success",
    UnknownFutureValue = "unknownFutureValue",

