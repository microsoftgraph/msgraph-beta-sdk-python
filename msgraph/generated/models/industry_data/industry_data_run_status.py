from enum import Enum

class IndustryDataRunStatus(Enum):
    Running = "running",
    Failed = "failed",
    Completed = "completed",
    CompletedWithErrors = "completedWithErrors",
    CompletedWithWarnings = "completedWithWarnings",
    UnknownFutureValue = "unknownFutureValue",

