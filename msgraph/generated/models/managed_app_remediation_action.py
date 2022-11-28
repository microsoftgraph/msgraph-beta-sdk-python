from enum import Enum

class ManagedAppRemediationAction(Enum):
    # app and the corresponding company data to be blocked
    Block = "block",
    # app and the corresponding company data to be wiped
    Wipe = "wipe",
    # app and the corresponding user to be warned
    Warn = "warn",

