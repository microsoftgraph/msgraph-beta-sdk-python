from enum import Enum

class DeploymentStateValue(Enum):
    Scheduled = "scheduled",
    Offering = "offering",
    Paused = "paused",
    Faulted = "faulted",
    Archived = "archived",
    UnknownFutureValue = "unknownFutureValue",

