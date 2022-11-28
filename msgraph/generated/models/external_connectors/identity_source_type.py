from enum import Enum

class IdentitySourceType(Enum):
    AzureActiveDirectory = "azureActiveDirectory",
    External = "external",
    UnknownFutureValue = "unknownFutureValue",

