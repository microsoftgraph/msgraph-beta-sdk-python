from enum import Enum

class LifecycleTaskCategory(Enum):
    Joiner = "joiner",
    Leaver = "leaver",
    UnknownFutureValue = "unknownFutureValue",

