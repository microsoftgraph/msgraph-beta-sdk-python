from enum import Enum

class DeviceAppManagementTaskPriority(Enum):
    # No priority set.
    None_ = "none",
    # High priority.
    High = "high",
    # Low priority.
    Low = "low",

