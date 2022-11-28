from enum import Enum

class KioskModeManagedHomeScreenPinComplexity(Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # Numeric values only.
    Simple = "simple",
    # Alphanumerical value.
    Complex = "complex",

