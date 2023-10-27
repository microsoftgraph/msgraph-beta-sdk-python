from enum import Enum

class DriveItemSourceApplication(str, Enum):
    Teams = "teams",
    Yammer = "yammer",
    SharePoint = "sharePoint",
    OneDrive = "oneDrive",
    Stream = "stream",
    PowerPoint = "powerPoint",
    Office = "office",
    UnknownFutureValue = "unknownFutureValue",

