from enum import Enum

class CloudPcFlexAvailabilityStatus(str, Enum):
    NotApplicable = "notApplicable",
    Available = "available",
    NotAvailable = "notAvailable",
    UnknownFutureValue = "unknownFutureValue",

