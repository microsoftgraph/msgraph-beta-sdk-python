from enum import Enum

class WorkflowExecutionType(Enum):
    Scheduled = "scheduled",
    OnDemand = "onDemand",
    UnknownFutureValue = "unknownFutureValue",

