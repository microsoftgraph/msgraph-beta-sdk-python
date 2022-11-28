from enum import Enum

class AzureADDeviceRegistrationErrorReason(Enum):
    InvalidGlobalDeviceId = "invalidGlobalDeviceId",
    InvalidAzureADDeviceId = "invalidAzureADDeviceId",
    MissingTrustType = "missingTrustType",
    InvalidAzureADJoin = "invalidAzureADJoin",
    UnknownFutureValue = "unknownFutureValue",

