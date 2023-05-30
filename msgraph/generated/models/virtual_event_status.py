from enum import Enum

class VirtualEventStatus(Enum):
    Draft = "draft",
    Published = "published",
    Canceled = "canceled",
    UnknownFutureValue = "unknownFutureValue",

