from enum import Enum

class DirectoryDefinitionDiscoverabilities(Enum):
    None_escaped = "None",
    AttributeNames = "AttributeNames",
    AttributeDataTypes = "AttributeDataTypes",
    AttributeReadOnly = "AttributeReadOnly",
    ReferenceAttributes = "ReferenceAttributes",
    UnknownFutureValue = "UnknownFutureValue",

