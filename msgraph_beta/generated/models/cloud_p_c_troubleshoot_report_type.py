from enum import Enum

class CloudPCTroubleshootReportType(str, Enum):
    TroubleshootDetailsReport = "troubleshootDetailsReport",
    TroubleshootTrendCountReport = "troubleshootTrendCountReport",
    TroubleshootRegionalReport = "troubleshootRegionalReport",
    UnknownFutureValue = "unknownFutureValue",
    TroubleshootIssueCountReport = "troubleshootIssueCountReport",

