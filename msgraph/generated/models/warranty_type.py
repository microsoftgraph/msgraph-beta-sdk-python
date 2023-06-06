from enum import Enum

class WarrantyType(str, Enum):
    # Unknown warranty type
    Unknown = "unknown",
    # Manufacturer warranty
    Manufacturer = "manufacturer",
    # Contractual warranty
    Contractual = "contractual",
    # Unknown future value
    UnknownFutureValue = "unknownFutureValue",

