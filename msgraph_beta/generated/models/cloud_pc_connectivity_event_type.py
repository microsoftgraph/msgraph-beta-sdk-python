from enum import Enum

class CloudPcConnectivityEventType(str, Enum):
    Unknown = "unknown",
    UserConnection = "userConnection",
    UserTroubleshooting = "userTroubleshooting",
    DeviceHealthCheck = "deviceHealthCheck",
    UnknownFutureValue = "unknownFutureValue",

