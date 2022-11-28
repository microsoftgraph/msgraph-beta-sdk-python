from enum import Enum

class DeviceManagementConfigurationSettingVisibility(Enum):
    # Not visible
    None_escaped = "none",
    # Visible to setting catalog UX
    SettingsCatalog = "settingsCatalog",
    # Visible to template
    Template = "template",

