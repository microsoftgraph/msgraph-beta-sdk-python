from enum import Enum

class GranularRestoreItems(str, Enum):
    Email = "email",
    Note = "note",
    Contact = "contact",
    Task = "task",
    Calendar = "calendar",
    UnknownFutureValue = "unknownFutureValue",

