from enum import Enum

class SingleSignOnMode(Enum):
    None_escaped = "none",
    OnPremisesKerberos = "onPremisesKerberos",
    Saml = "saml",
    PingHeaderBased = "pingHeaderBased",
    AadHeaderBased = "aadHeaderBased",
    OAuthToken = "oAuthToken",
    UnknownFutureValue = "unknownFutureValue",

