from enum import Enum

class ManagementTemplateDeploymentStatus(Enum):
    Unknown = "unknown",
    InProgress = "inProgress",
    Completed = "completed",
    Failed = "failed",
    Ineligible = "ineligible",
    UnknownFutureValue = "unknownFutureValue",

