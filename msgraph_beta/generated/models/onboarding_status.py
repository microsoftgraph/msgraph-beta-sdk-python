from enum import Enum

class OnboardingStatus(str, Enum):
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
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

