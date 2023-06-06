from enum import Enum

class SimulationAutomationRunStatus(str, Enum):
    Unknown = "unknown",
    Running = "running",
    Succeeded = "succeeded",
    Failed = "failed",
    Skipped = "skipped",
    UnknownFutureValue = "unknownFutureValue",

