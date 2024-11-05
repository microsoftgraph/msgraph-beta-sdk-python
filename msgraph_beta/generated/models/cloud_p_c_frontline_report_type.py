from enum import Enum

class CloudPCFrontlineReportType(str, Enum):
    NoLicenseAvailableConnectivityFailureReport = "noLicenseAvailableConnectivityFailureReport",
    LicenseUsageReport = "licenseUsageReport",
    LicenseUsageRealTimeReport = "licenseUsageRealTimeReport",
    LicenseHourlyUsageReport = "licenseHourlyUsageReport",
    ConnectedUserRealtimeReport = "connectedUserRealtimeReport",
    UnknownFutureValue = "unknownFutureValue",

