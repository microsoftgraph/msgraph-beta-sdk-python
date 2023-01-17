from enum import Enum

class BookingStaffMembershipStatus(Enum):
    Active = "active",
    PendingAcceptance = "pendingAcceptance",
    RejectedByStaff = "rejectedByStaff",
    UnknownFutureValue = "unknownFutureValue",

