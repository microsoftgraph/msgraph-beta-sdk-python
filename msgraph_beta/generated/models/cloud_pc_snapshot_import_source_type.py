from enum import Enum

class CloudPcSnapshotImportSourceType(str, Enum):
    AzureStorageAccount = "azureStorageAccount",
    SasUrl = "sasUrl",
    UnknownFutureValue = "unknownFutureValue",

