from enum import Enum

class AuthenticationStrengthRequirements(Enum):
    None_escaped = "none",
    Mfa = "mfa",
    UnknownFutureValue = "unknownFutureValue",

