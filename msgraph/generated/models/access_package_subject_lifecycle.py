from enum import Enum

class AccessPackageSubjectLifecycle(Enum):
    NotDefined = "notDefined",
    NotGoverned = "notGoverned",
    Governed = "governed",
    UnknownFutureValue = "unknownFutureValue",

