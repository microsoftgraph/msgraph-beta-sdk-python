from enum import Enum

class PlannerPlanAccessLevel(Enum):
    ReadAccess = "readAccess",
    ReadWriteAccess = "readWriteAccess",
    FullAccess = "fullAccess",
    UnknownFutureValue = "unknownFutureValue",

