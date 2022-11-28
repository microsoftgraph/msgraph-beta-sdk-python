from enum import Enum

class SubmissionContentType(Enum):
    Email = "email",
    Url = "url",
    File = "file",
    App = "app",
    UnknownFutureValue = "unknownFutureValue",

