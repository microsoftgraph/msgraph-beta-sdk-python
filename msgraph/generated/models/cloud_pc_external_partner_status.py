from enum import Enum

class CloudPcExternalPartnerStatus(Enum):
    NotAvailable = "notAvailable",
    Available = "available",
    Healthy = "healthy",
    Unhealthy = "unhealthy",
    UnknownFutureValue = "unknownFutureValue",

