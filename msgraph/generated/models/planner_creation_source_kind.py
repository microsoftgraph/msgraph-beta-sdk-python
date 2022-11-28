from enum import Enum

class PlannerCreationSourceKind(Enum):
    None_escaped = "none",
    External = "external",
    Publication = "publication",
    UnknownFutureValue = "unknownFutureValue",

