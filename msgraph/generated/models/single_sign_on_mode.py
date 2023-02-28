from enum import Enum

class SingleSignOnMode(Enum):
    None_ = "none",
    OnPremisesKerberos = "onPremisesKerberos",
    Saml = "saml",
    PingHeaderBased = "pingHeaderBased",
    AadHeaderBased = "aadHeaderBased",
    OAuthToken = "oAuthToken",
    UnknownFutureValue = "unknownFutureValue",

