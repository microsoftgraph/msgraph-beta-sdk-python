from enum import Enum

class ZebraFotaScheduleMode(str, Enum):
    # Instructs the device to install the update as soon as it is received.
    InstallNow = "installNow",
    # Schedule an update to be installed at a specified date and time.
    Scheduled = "scheduled",
    # Unknown future enum value.
    UnknownFutureValue = "unknownFutureValue",

