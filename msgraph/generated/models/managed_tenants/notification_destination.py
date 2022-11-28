from enum import Enum

class NotificationDestination(Enum):
    None_escaped = "none",
    Api = "api",
    Email = "email",
    Sms = "sms",
    UnknownFutureValue = "unknownFutureValue",

