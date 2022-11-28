from enum import Enum

class CloudPcConnectivityEventType(Enum):
    Unknown = "unknown",
    UserConnection = "userConnection",
    UserTroubleshooting = "userTroubleshooting",
    DeviceHealthCheck = "deviceHealthCheck",
    UnknownFutureValue = "unknownFutureValue",

