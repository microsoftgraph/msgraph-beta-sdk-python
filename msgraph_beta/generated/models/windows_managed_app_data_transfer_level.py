from enum import Enum

class WindowsManagedAppDataTransferLevel(str, Enum):
    # All apps.
    AllApps = "allApps",
    # No apps.
    None_ = "none",

