from enum import Enum

class AuthenticationMethodFeature(Enum):
    SsprRegistered = "ssprRegistered",
    SsprEnabled = "ssprEnabled",
    SsprCapable = "ssprCapable",
    PasswordlessCapable = "passwordlessCapable",
    MfaCapable = "mfaCapable",

