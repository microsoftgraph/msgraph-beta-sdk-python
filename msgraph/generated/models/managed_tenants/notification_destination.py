from enum import Enum

class NotificationDestination(Enum):
    None_ = "none",
    Api = "api",
    Email = "email",
    Sms = "sms",
    UnknownFutureValue = "unknownFutureValue",

