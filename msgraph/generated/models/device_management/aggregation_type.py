from enum import Enum

class AggregationType(Enum):
    Count = "count",
    Percentage = "percentage",
    AffectedCloudPcCount = "affectedCloudPcCount",
    AffectedCloudPcPercentage = "affectedCloudPcPercentage",
    UnknownFutureValue = "unknownFutureValue",

