from enum import Enum

class PlannerContainerType(str, Enum):
    Group = "group",
    UnknownFutureValue = "unknownFutureValue",
    Roster = "roster",
    Project = "project",
    DriveItem = "driveItem",
    User = "user",

