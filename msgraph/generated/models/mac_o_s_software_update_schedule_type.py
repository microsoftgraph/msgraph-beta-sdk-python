from enum import Enum

class MacOSSoftwareUpdateScheduleType(Enum):
    # Always update.
    AlwaysUpdate = "alwaysUpdate",
    # Update during time windows.
    UpdateDuringTimeWindows = "updateDuringTimeWindows",
    # Update outside of time windows.
    UpdateOutsideOfTimeWindows = "updateOutsideOfTimeWindows",

