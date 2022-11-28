from enum import Enum

class EvidenceRemediationStatus(Enum):
    None_escaped = "none",
    Remediated = "remediated",
    Prevented = "prevented",
    Blocked = "blocked",
    NotFound = "notFound",
    Active = "active",
    PendingApproval = "pendingApproval",
    Declined = "declined",
    NotRemediated = "notRemediated",
    Running = "running",
    UnknownFutureValue = "unknownFutureValue",

