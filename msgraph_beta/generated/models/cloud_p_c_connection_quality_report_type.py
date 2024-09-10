from enum import Enum

class CloudPCConnectionQualityReportType(str, Enum):
    RemoteConnectionQualityReport = "remoteConnectionQualityReport",
    RegionalConnectionQualityTrendReport = "regionalConnectionQualityTrendReport",
    RegionalConnectionQualityInsightsReport = "regionalConnectionQualityInsightsReport",
    UnknownFutureValue = "unknownFutureValue",

