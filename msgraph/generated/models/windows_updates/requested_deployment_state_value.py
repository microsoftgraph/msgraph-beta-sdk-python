from enum import Enum

class RequestedDeploymentStateValue(Enum):
    None_escaped = "none",
    Paused = "paused",
    Archived = "archived",
    UnknownFutureValue = "unknownFutureValue",

