from enum import Enum

class CloudPcReportName(str, Enum):
    RemoteConnectionHistoricalReports = "remoteConnectionHistoricalReports",
    DailyAggregatedRemoteConnectionReports = "dailyAggregatedRemoteConnectionReports",
    TotalAggregatedRemoteConnectionReports = "totalAggregatedRemoteConnectionReports",
    SharedUseLicenseUsageReport = "sharedUseLicenseUsageReport",
    SharedUseLicenseUsageRealTimeReport = "sharedUseLicenseUsageRealTimeReport",
    UnknownFutureValue = "unknownFutureValue",
    NoLicenseAvailableConnectivityFailureReport = "noLicenseAvailableConnectivityFailureReport",
    RemoteConnectionQualityReports = "remoteConnectionQualityReports",
    InaccessibleCloudPcReports = "inaccessibleCloudPcReports",

