from enum import Enum

class RequestHttpMethod(str, Enum):
    Post = "post",
    Patch = "patch",
    Put = "put",
    Get = "get",
    Delete = "delete",
    UnknownFutureValue = "unknownFutureValue",

