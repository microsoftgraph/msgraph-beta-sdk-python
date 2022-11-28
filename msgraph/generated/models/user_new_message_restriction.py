from enum import Enum

class UserNewMessageRestriction(Enum):
    Everyone = "everyone",
    EveryoneExceptGuests = "everyoneExceptGuests",
    Moderators = "moderators",
    UnknownFutureValue = "unknownFutureValue",

