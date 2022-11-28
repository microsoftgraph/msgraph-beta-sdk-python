from enum import Enum

class ResourceConnectionState(Enum):
    Connected = "connected",
    NotAuthorized = "notAuthorized",
    NotFound = "notFound",
    UnknownFutureValue = "unknownFutureValue",

