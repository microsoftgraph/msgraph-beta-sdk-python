from enum import Enum

class CloudPcOnPremisesConnectionType(Enum):
    HybridAzureADJoin = "hybridAzureADJoin",
    AzureADJoin = "azureADJoin",
    UnknownFutureValue = "unknownFutureValue",

