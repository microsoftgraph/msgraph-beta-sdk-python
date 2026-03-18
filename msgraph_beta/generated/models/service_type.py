from enum import Enum

class ServiceType(str, Enum):
    Unknown = "unknown",
    Sharepoint = "sharepoint",
    Exchange = "exchange",
    OneDriveForBusiness = "oneDriveForBusiness",
    UnknownFutureValue = "unknownFutureValue",

