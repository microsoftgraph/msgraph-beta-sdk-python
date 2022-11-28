from enum import Enum

class SignInAccessType(Enum):
    None_escaped = "none",
    B2bCollaboration = "b2bCollaboration",
    B2bDirectConnect = "b2bDirectConnect",
    MicrosoftSupport = "microsoftSupport",
    ServiceProvider = "serviceProvider",
    UnknownFutureValue = "unknownFutureValue",

