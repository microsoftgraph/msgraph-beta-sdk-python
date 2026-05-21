from enum import Enum

class CloudPcExternalPartnerActionType(str, Enum):
    ConfigureAgent = "configureAgent",
    DeployAgent = "deployAgent",
    UnknownFutureValue = "unknownFutureValue",

