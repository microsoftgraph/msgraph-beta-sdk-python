from enum import Enum

class AdminConsentState(Enum):
    # Admin did not configure the item
    NotConfigured = "notConfigured",
    # Admin granted item
    Granted = "granted",
    # Admin deos not grant item
    NotGranted = "notGranted",

