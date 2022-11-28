from enum import Enum

class DeviceManagementConfigurationAzureAdTrustType(Enum):
    # No AAD Trust Type specified
    None_escaped = "none",
    # AAD Joined Trust Type
    AzureAdJoined = "azureAdJoined",
    # AddWorkAccount
    AddWorkAccount = "addWorkAccount",
    # MDM only
    MdmOnly = "mdmOnly",

