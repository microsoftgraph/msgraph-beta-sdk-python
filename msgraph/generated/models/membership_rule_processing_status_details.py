from enum import Enum

class MembershipRuleProcessingStatusDetails(Enum):
    NotStarted = "NotStarted",
    Running = "Running",
    Failed = "Failed",
    Succeeded = "Succeeded",
    UnsupportedFutureValue = "UnsupportedFutureValue",

