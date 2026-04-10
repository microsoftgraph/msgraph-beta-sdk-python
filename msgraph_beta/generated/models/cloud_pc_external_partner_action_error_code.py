from enum import Enum

class CloudPcExternalPartnerActionErrorCode(str, Enum):
    None_ = "none",
    ExecuteActionFailed = "executeActionFailed",
    ExecuteActionTimeout = "executeActionTimeout",
    DeviceNotFound = "deviceNotFound",
    DeviceNotAvailable = "deviceNotAvailable",
    CheckDiskSpaceFailed = "checkDiskSpaceFailed",
    CheckNetworkConnectionFailed = "checkNetworkConnectionFailed",
    AgentNotFound = "agentNotFound",
    InvalidAgentFormat = "invalidAgentFormat",
    InvalidAgentChecksum = "invalidAgentChecksum",
    UnknownFutureValue = "unknownFutureValue",

