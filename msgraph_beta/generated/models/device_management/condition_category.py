from enum import Enum

class ConditionCategory(str, Enum):
    ProvisionFailures = "provisionFailures",
    ImageUploadFailures = "imageUploadFailures",
    AzureNetworkConnectionCheckFailures = "azureNetworkConnectionCheckFailures",
    CloudPcInGracePeriod = "cloudPcInGracePeriod",
    FrontlineInsufficientLicenses = "frontlineInsufficientLicenses",
    CloudPcConnectionErrors = "cloudPcConnectionErrors",
    CloudPcHostHealthCheckFailures = "cloudPcHostHealthCheckFailures",
    CloudPcZoneOutage = "cloudPcZoneOutage",
    UnknownFutureValue = "unknownFutureValue",

