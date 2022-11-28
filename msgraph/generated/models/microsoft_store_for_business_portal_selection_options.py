from enum import Enum

class MicrosoftStoreForBusinessPortalSelectionOptions(Enum):
    # This option is not available for the account
    None_escaped = "none",
    # Intune Company Portal only.
    CompanyPortal = "companyPortal",
    # MSFB Private store only.
    PrivateStore = "privateStore",

