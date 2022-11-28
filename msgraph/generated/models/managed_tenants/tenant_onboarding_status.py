from enum import Enum

class TenantOnboardingStatus(Enum):
    Ineligible = "ineligible",
    InProcess = "inProcess",
    Active = "active",
    Inactive = "inactive",
    UnknownFutureValue = "unknownFutureValue",

