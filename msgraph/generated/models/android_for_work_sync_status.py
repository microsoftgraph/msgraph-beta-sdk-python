from enum import Enum

class AndroidForWorkSyncStatus(Enum):
    Success = "success",
    CredentialsNotValid = "credentialsNotValid",
    AndroidForWorkApiError = "androidForWorkApiError",
    ManagementServiceError = "managementServiceError",
    UnknownError = "unknownError",
    None_escaped = "none",

