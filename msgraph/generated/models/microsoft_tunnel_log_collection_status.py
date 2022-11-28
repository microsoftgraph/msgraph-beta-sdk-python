from enum import Enum

class MicrosoftTunnelLogCollectionStatus(Enum):
    # Indicates that the log collection is in progress
    Pending = "pending",
    # Indicates that the log collection is completed
    Completed = "completed",
    # Indicates that the log collection has failed
    Failed = "failed",
    # Placeholder value for future expansion enums
    UnknownFutureValue = "unknownFutureValue",

