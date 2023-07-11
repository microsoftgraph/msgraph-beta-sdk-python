from enum import Enum

class IdentityUserFlowAttributeDataType(str, Enum):
    String = "string",
    Boolean = "boolean",
    Int64 = "int64",
    StringCollection = "stringCollection",
    DateTime = "dateTime",
    UnknownFutureValue = "unknownFutureValue",

