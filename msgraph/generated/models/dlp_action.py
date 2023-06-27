from enum import Enum

class DlpAction(str, Enum):
    NotifyUser = "notifyUser",
    BlockAccess = "blockAccess",
    DeviceRestriction = "deviceRestriction",

