from enum import Enum

class AnswerState(Enum):
    Published = "published",
    Draft = "draft",
    Excluded = "excluded",
    UnknownFutureValue = "unknownFutureValue",

