from enum import Enum

class CloudPcRemoteActionName(str, Enum):
    Unknown = "unknown",
    Restart = "restart",
    Rename = "rename",
    Resize = "resize",
    Restore = "restore",
    Reprovision = "reprovision",
    ChangeUserAccountType = "changeUserAccountType",
    Troubleshoot = "troubleshoot",
    PlaceUnderReview = "placeUnderReview",
    UnknownFutureValue = "unknownFutureValue",
    CreateSnapshot = "createSnapshot",
    PowerOn = "powerOn",
    PowerOff = "powerOff",
    MoveRegion = "moveRegion",

