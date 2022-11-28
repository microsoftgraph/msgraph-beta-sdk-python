from enum import Enum

class DeviceManagementConfigurationSettingUsage(Enum):
    # No setting type specified
    None_escaped = "none",
    # Configuration setting
    Configuration = "configuration",
    # Compliance setting
    Compliance = "compliance",

