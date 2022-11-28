from enum import Enum

class ApprovalState(Enum):
    Pending = "pending",
    Approved = "approved",
    Denied = "denied",
    Aborted = "aborted",
    Canceled = "canceled",

