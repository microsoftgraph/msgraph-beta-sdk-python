from enum import Enum

class MicrosoftTunnelLogCollectionStatus(str, Enum):
    # Indicates that the log collection is in progress
    Pending = "pending",
    # Indicates that the log collection is completed
    Completed = "completed",
    # Indicates that the log collection has failed
    Failed = "failed",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

