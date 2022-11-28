from enum import Enum

class CloudPcDomainJoinType(Enum):
    AzureADJoin = "azureADJoin",
    HybridAzureADJoin = "hybridAzureADJoin",
    UnknownFutureValue = "unknownFutureValue",

