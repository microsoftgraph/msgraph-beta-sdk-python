from enum import Enum

class ReplyRestriction(Enum):
    Everyone = "everyone",
    AuthorAndModerators = "authorAndModerators",
    UnknownFutureValue = "unknownFutureValue",

