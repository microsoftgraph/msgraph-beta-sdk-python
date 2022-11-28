from enum import Enum

class AndroidManagedStoreAccountAppSyncStatus(Enum):
    Success = "success",
    CredentialsNotValid = "credentialsNotValid",
    AndroidForWorkApiError = "androidForWorkApiError",
    ManagementServiceError = "managementServiceError",
    UnknownError = "unknownError",
    None_escaped = "none",

