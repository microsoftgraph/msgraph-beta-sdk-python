from enum import Enum

class CloudPcOrganizationActionType(str, Enum):
    Activate = "activate",
    Deactivate = "deactivate",
    UnknownFutureValue = "unknownFutureValue",

