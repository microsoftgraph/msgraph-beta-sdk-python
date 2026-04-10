from enum import Enum

class CloudPCUserSettingsPersistenceProfileStatus(str, Enum):
    Connected = "connected",
    NotConnected = "notConnected",
    Deleting = "deleting",
    UnknownFutureValue = "unknownFutureValue",

