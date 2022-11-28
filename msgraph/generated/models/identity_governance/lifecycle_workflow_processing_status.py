from enum import Enum

class LifecycleWorkflowProcessingStatus(Enum):
    Queued = "queued",
    InProgress = "inProgress",
    Completed = "completed",
    CompletedWithErrors = "completedWithErrors",
    Canceled = "canceled",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

