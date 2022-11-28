from enum import Enum

class RecommendationStatus(Enum):
    Active = "active",
    CompletedBySystem = "completedBySystem",
    CompletedByUser = "completedByUser",
    Dismissed = "dismissed",
    Postponed = "postponed",
    UnknownFutureValue = "unknownFutureValue",

