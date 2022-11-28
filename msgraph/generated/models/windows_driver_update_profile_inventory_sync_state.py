from enum import Enum

class WindowsDriverUpdateProfileInventorySyncState(Enum):
    # Pending sync.
    Pending = "pending",
    # Successful sync.
    Success = "success",
    # Failed sync.
    Failure = "failure",

