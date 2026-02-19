from enum import Enum

class CloudPcSourceImageCategory(str, Enum):
    ManagedImage = "managedImage",
    AzureComputeGallery = "azureComputeGallery",
    UnknownFutureValue = "unknownFutureValue",

