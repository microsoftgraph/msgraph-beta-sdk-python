from enum import Enum

class ActionState(Enum):
    None_escaped = "none",
    Pending = "pending",
    Canceled = "canceled",
    Active = "active",
    Done = "done",
    Failed = "failed",
    NotSupported = "notSupported",

