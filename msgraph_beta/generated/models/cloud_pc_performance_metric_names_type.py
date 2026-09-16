from enum import Enum

class CloudPcPerformanceMetricNamesType(str, Enum):
    CpuUsageInPercentage = "cpuUsageInPercentage",
    AvailableMemoryInPercentage = "availableMemoryInPercentage",
    VmAvailability = "vmAvailability",
    NetworkInboundInBytes = "networkInboundInBytes",
    NetworkOutboundInBytes = "networkOutboundInBytes",
    InboundFlowsCount = "inboundFlowsCount",
    OutboundFlowsCount = "outboundFlowsCount",
    DiskReadInBytes = "diskReadInBytes",
    DiskWriteInBytes = "diskWriteInBytes",
    DiskReadOperationsPerSecond = "diskReadOperationsPerSecond",
    DiskWriteOperationsPerSecond = "diskWriteOperationsPerSecond",
    OsDiskLatencyInMs = "osDiskLatencyInMs",
    UnknownFutureValue = "unknownFutureValue",

