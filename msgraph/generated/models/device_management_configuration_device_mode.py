from enum import Enum

class DeviceManagementConfigurationDeviceMode(Enum):
    # No Device Mode specified
    None_escaped = "none",
    # Device must be in kiosk mode for this setting to apply
    Kiosk = "kiosk",

