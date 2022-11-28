from enum import Enum

class AndroidDeviceOwnerEnrollmentTokenType(Enum):
    # Default token type.
    Default = "default",
    # Token type for Azure AD shared dedicated device enrollment. It applies to CorporateOwnedDedicatedDevice enrollment mode only.
    CorporateOwnedDedicatedDeviceWithAzureADSharedMode = "corporateOwnedDedicatedDeviceWithAzureADSharedMode",

