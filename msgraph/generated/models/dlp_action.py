from enum import Enum

class DlpAction(Enum):
    NotifyUser = "notifyUser",
    BlockAccess = "blockAccess",
    DeviceRestriction = "deviceRestriction",

