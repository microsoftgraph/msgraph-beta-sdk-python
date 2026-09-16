from enum import Enum

class CloudPcVmPerformanceMetricsTimeRange(str, Enum):
    Last2Hours = "last2Hours",
    Last4Hours = "last4Hours",
    Last12Hours = "last12Hours",
    Last24Hours = "last24Hours",
    Last48Hours = "last48Hours",
    Last4Days = "last4Days",
    Last7Days = "last7Days",
    Last14Days = "last14Days",
    Last28Days = "last28Days",
    UnknownFutureValue = "unknownFutureValue",

