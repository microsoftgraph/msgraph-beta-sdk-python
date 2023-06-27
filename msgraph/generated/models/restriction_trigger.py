from enum import Enum

class RestrictionTrigger(str, Enum):
    CopyPaste = "copyPaste",
    CopyToNetworkShare = "copyToNetworkShare",
    CopyToRemovableMedia = "copyToRemovableMedia",
    ScreenCapture = "screenCapture",
    Print = "print",
    CloudEgress = "cloudEgress",
    UnallowedApps = "unallowedApps",

