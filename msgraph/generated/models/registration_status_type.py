from enum import Enum

class RegistrationStatusType(Enum):
    Registered = "registered",
    Enabled = "enabled",
    Capable = "capable",
    MfaRegistered = "mfaRegistered",
    UnknownFutureValue = "unknownFutureValue",

