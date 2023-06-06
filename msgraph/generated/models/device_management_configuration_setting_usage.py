from enum import Enum

class DeviceManagementConfigurationSettingUsage(str, Enum):
    # Default. No setting type specified.
    None_ = "none",
    # Configuration setting type.
    Configuration = "configuration",
    # Compliance setting type.
    Compliance = "compliance",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

