from enum import Enum

class CloudPcReportName(Enum):
    RemoteConnectionHistoricalReports = "remoteConnectionHistoricalReports",
    DailyAggregatedRemoteConnectionReports = "dailyAggregatedRemoteConnectionReports",
    TotalAggregatedRemoteConnectionReports = "totalAggregatedRemoteConnectionReports",
    UnknownFutureValue = "unknownFutureValue",

