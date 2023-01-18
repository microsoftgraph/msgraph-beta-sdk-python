from enum import Enum

class SimulationContentStatus(Enum):
    Unknown = "unknown",
    Draft = "draft",
    Ready = "ready",
    Archive = "archive",
    Delete = "delete",
    UnknownFutureValue = "unknownFutureValue",

