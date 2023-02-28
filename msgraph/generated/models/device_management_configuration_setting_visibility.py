from enum import Enum

class DeviceManagementConfigurationSettingVisibility(Enum):
    # Not visible
    None_ = "none",
    # Visible to setting catalog UX
    SettingsCatalog = "settingsCatalog",
    # Visible to template
    Template = "template",

