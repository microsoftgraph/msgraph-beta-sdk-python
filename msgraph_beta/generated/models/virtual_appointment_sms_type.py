from enum import Enum

class VirtualAppointmentSmsType(str, Enum):
    Confirmation = "confirmation",
    Reschedule = "reschedule",
    Cancellation = "cancellation",
    UnknownFutureValue = "unknownFutureValue",

