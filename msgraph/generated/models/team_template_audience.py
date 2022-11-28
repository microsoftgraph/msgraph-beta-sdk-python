from enum import Enum

class TeamTemplateAudience(Enum):
    Organization = "organization",
    User = "user",
    Public = "public",
    UnknownFutureValue = "unknownFutureValue",

