from enum import Enum

class WindowsAutopilotDeploymentState(Enum):
    Unknown = "unknown",
    Success = "success",
    InProgress = "inProgress",
    Failure = "failure",
    SuccessWithTimeout = "successWithTimeout",
    NotAttempted = "notAttempted",
    Disabled = "disabled",

