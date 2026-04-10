from enum import Enum

class FullServiceBackupDisableMode(str, Enum):
    None_ = "none",
    EnableAll = "enableAll",
    DisableAll = "disableAll",
    UnknownFutureValue = "unknownFutureValue",

