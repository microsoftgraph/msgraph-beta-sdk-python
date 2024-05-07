from enum import Enum

class ProtocolType(str, Enum):
    None_ = "none",
    OAuth2 = "oAuth2",
    Ropc = "ropc",
    WsFederation = "wsFederation",
    Saml20 = "saml20",
    DeviceCode = "deviceCode",
    UnknownFutureValue = "unknownFutureValue",
    AuthenticationTransfer = "authenticationTransfer",
    NativeAuth = "nativeAuth",

