from enum import Enum

class MicrosoftStoreForBusinessPortalSelectionOptions(str, Enum):
    # This option is not available for the account
    None_ = "none",
    # Intune Company Portal only.
    CompanyPortal = "companyPortal",
    # MSFB Private store only.
    PrivateStore = "privateStore",

