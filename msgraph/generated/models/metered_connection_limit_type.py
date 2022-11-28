from enum import Enum

class MeteredConnectionLimitType(Enum):
    # Unrestricted
    Unrestricted = "unrestricted",
    # Fixed
    Fixed = "fixed",
    # Variable
    Variable = "variable",

