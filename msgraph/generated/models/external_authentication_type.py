from enum import Enum

class ExternalAuthenticationType(Enum):
    Passthru = "passthru",
    AadPreAuthentication = "aadPreAuthentication",

