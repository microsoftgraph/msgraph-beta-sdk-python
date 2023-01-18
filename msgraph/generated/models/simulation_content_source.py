from enum import Enum

class SimulationContentSource(Enum):
    Unknown = "unknown",
    Global_escaped = "global",
    Tenant = "tenant",
    UnknownFutureValue = "unknownFutureValue",

