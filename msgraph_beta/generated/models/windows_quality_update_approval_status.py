from enum import Enum

class WindowsQualityUpdateApprovalStatus(str, Enum):
    # unknown status for corresponding catalog item
    Unknown = "unknown",
    # approved for corresponding catalog item
    Approved = "approved",
    # suspended for corresponding catalog item
    Suspended = "suspended",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

