from enum import Enum

class ChromeOSOnboardingStatus(Enum):
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

