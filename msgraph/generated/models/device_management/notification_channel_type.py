from enum import Enum

class NotificationChannelType(Enum):
    Portal = "portal",
    Email = "email",
    PhoneCall = "phoneCall",
    Sms = "sms",
    UnknownFutureValue = "unknownFutureValue",

