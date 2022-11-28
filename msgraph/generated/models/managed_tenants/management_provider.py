from enum import Enum

class ManagementProvider(Enum):
    Microsoft = "microsoft",
    Community = "community",
    IndirectProvider = "indirectProvider",
    Self = "self",
    UnknownFutureValue = "unknownFutureValue",

