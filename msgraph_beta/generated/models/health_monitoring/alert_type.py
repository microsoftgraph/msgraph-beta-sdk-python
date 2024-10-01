from enum import Enum

class AlertType(str, Enum):
    Unknown = "unknown",
    MfaSignInFailure = "mfaSignInFailure",
    ManagedDeviceSignInFailure = "managedDeviceSignInFailure",
    CompliantDeviceSignInFailure = "compliantDeviceSignInFailure",
    UnknownFutureValue = "unknownFutureValue",

