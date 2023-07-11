from enum import Enum

class ColumnTypes(str, Enum):
    Note = "note",
    Text = "text",
    Choice = "choice",
    Multichoice = "multichoice",
    Number = "number",
    Currency = "currency",
    DateTime = "dateTime",
    Lookup = "lookup",
    Boolean = "boolean",
    User = "user",
    Url = "url",
    Calculated = "calculated",
    Location = "location",
    Geolocation = "geolocation",
    Term = "term",
    Multiterm = "multiterm",
    Thumbnail = "thumbnail",
    ApprovalStatus = "approvalStatus",
    UnknownFutureValue = "unknownFutureValue",

