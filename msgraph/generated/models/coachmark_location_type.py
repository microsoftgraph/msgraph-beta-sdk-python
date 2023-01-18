from enum import Enum

class CoachmarkLocationType(Enum):
    Unknown = "unknown",
    FromEmail = "fromEmail",
    Subject = "subject",
    ExternalTag = "externalTag",
    DisplayName = "displayName",
    MessageBody = "messageBody",
    UnknownFutureValue = "unknownFutureValue",

