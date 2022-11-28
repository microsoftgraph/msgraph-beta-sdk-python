from enum import Enum

class WindowsAutopilotEnrollmentType(Enum):
    Unknown = "unknown",
    AzureADJoinedWithAutopilotProfile = "azureADJoinedWithAutopilotProfile",
    OfflineDomainJoined = "offlineDomainJoined",
    AzureADJoinedUsingDeviceAuthWithAutopilotProfile = "azureADJoinedUsingDeviceAuthWithAutopilotProfile",
    AzureADJoinedUsingDeviceAuthWithoutAutopilotProfile = "azureADJoinedUsingDeviceAuthWithoutAutopilotProfile",
    AzureADJoinedWithOfflineAutopilotProfile = "azureADJoinedWithOfflineAutopilotProfile",
    AzureADJoinedWithWhiteGlove = "azureADJoinedWithWhiteGlove",
    OfflineDomainJoinedWithWhiteGlove = "offlineDomainJoinedWithWhiteGlove",
    OfflineDomainJoinedWithOfflineAutopilotProfile = "offlineDomainJoinedWithOfflineAutopilotProfile",

