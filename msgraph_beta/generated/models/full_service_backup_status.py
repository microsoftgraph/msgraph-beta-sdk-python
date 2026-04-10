from enum import Enum

class FullServiceBackupStatus(str, Enum):
    Disabled = "disabled",
    Enabled = "enabled",
    UnknownFutureValue = "unknownFutureValue",

