from enum import Enum

class EnrollmentNotificationTemplateType(str, Enum):
    # Email Notification
    Email = "email",
    # Push Notification
    Push = "push",
    # Unknown Type
    UnknownFutureValue = "unknownFutureValue",

