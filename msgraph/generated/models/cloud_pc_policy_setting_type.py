from enum import Enum

class CloudPcPolicySettingType(str, Enum):
    Region = "region",
    SingleSignOn = "singleSignOn",
    UnknownFutureValue = "unknownFutureValue",

