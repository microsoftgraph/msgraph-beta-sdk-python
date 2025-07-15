from enum import Enum

class TlsCertificateStatus(str, Enum):
    CsrGenerated = "csrGenerated",
    Enrolling = "enrolling",
    Active = "active",
    UnknownFutureValue = "unknownFutureValue",
    Expiring = "expiring",
    Expired = "expired",

