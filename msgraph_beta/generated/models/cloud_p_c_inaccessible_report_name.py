from enum import Enum

class CloudPCInaccessibleReportName(str, Enum):
    InaccessibleCloudPcReports = "inaccessibleCloudPcReports",
    InaccessibleCloudPcTrendReport = "inaccessibleCloudPcTrendReport",
    UnknownFutureValue = "unknownFutureValue",

