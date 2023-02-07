from enum import Enum

class IncomingTokenType(Enum):
    None_ = "none",
    PrimaryRefreshToken = "primaryRefreshToken",
    Saml11 = "saml11",
    Saml20 = "saml20",
    UnknownFutureValue = "unknownFutureValue",
    RemoteDesktopToken = "remoteDesktopToken",

