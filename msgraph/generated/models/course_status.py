from enum import Enum

class CourseStatus(Enum):
    NotStarted = "notStarted",
    InProgress = "inProgress",
    Completed = "completed",
    UnknownFutureValue = "unknownFutureValue",

