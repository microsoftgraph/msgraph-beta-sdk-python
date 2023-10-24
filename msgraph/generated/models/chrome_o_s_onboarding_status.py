from enum import Enum

class chromeOSOnboardingStatus(str, Enum):
    # Unknown
    Unknown = "unknown",
    # In progress
    Inprogress = "inprogress",
    # Onboarded
    Onboarded = "onboarded",
    # Failed
    Failed = "failed",
    # Offboarding
    Offboarding = "offboarding",
    # UnknownFutureValue
    UnknownFutureValue = "unknownFutureValue",

