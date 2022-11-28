from enum import Enum

class ProtocolType(Enum):
    None_escaped = "none",
    OAuth2 = "oAuth2",
    Ropc = "ropc",
    WsFederation = "wsFederation",
    Saml20 = "saml20",
    DeviceCode = "deviceCode",
    UnknownFutureValue = "unknownFutureValue",

