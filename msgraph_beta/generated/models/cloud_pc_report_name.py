from enum import Enum

class CloudPcReportName(str, Enum):
    RemoteConnectionHistoricalReports = "remoteConnectionHistoricalReports",
    DailyAggregatedRemoteConnectionReports = "dailyAggregatedRemoteConnectionReports",
    TotalAggregatedRemoteConnectionReports = "totalAggregatedRemoteConnectionReports",
    SharedUseLicenseUsageReport = "sharedUseLicenseUsageReport",
    SharedUseLicenseUsageRealTimeReport = "sharedUseLicenseUsageRealTimeReport",
    UnknownFutureValue = "unknownFutureValue",
    NoLicenseAvailableConnectivityFailureReport = "noLicenseAvailableConnectivityFailureReport",
    FrontlineLicenseUsageReport = "frontlineLicenseUsageReport",
    FrontlineLicenseUsageRealTimeReport = "frontlineLicenseUsageRealTimeReport",
    RemoteConnectionQualityReports = "remoteConnectionQualityReports",
    InaccessibleCloudPcReports = "inaccessibleCloudPcReports",
    RawRemoteConnectionReports = "rawRemoteConnectionReports",
    CloudPcUsageCategoryReports = "cloudPcUsageCategoryReports",
    CrossRegionDisasterRecoveryReport = "crossRegionDisasterRecoveryReport",
    PerformanceTrendReport = "performanceTrendReport",
    InaccessibleCloudPcTrendReport = "inaccessibleCloudPcTrendReport",

