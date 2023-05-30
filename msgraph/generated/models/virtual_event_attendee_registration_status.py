from enum import Enum

class VirtualEventAttendeeRegistrationStatus(Enum):
    Registered = "registered",
    Canceled = "canceled",
    Waitlisted = "waitlisted",
    PendingApproval = "pendingApproval",
    RejectedByOrganizer = "rejectedByOrganizer",
    UnknownFutureValue = "unknownFutureValue",

