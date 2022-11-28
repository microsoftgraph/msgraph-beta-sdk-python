from enum import Enum

class NetworkType(Enum):
    Intranet = "intranet",
    Extranet = "extranet",
    NamedNetwork = "namedNetwork",
    Trusted = "trusted",
    TrustedNamedLocation = "trustedNamedLocation",
    UnknownFutureValue = "unknownFutureValue",

