from enum import Enum

class RetentionTrigger(Enum):
    DateLabeled = "dateLabeled",
    DateCreated = "dateCreated",
    DateModified = "dateModified",
    DateOfEvent = "dateOfEvent",
    UnknownFutureValue = "unknownFutureValue",

