from enum import Enum

class WindowsQualityUpdateClassification(Enum):
    # All update type
    All = "all",
    # Security only update type
    Security = "security",
    # Non security only update type
    NonSecurity = "nonSecurity",

