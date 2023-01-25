from enum import Enum

class PlannerCreationSourceKind(Enum):
    None_ = "none",
    External = "external",
    Publication = "publication",
    UnknownFutureValue = "unknownFutureValue",

