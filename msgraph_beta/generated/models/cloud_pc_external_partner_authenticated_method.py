from enum import Enum

class CloudPcExternalPartnerAuthenticatedMethod(str, Enum):
    GDAP = "gDAP",
    DAP = "dAP",
    AppOnly = "appOnly",
    NormalUser = "normalUser",
    GuestUser = "guestUser",
    UnknownFutureValue = "unknownFutureValue",

