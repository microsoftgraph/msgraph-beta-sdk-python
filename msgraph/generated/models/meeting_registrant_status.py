from enum import Enum

class MeetingRegistrantStatus(Enum):
    Registered = "registered",
    Canceled = "canceled",
    Processing = "processing",
    UnknownFutureValue = "unknownFutureValue",

