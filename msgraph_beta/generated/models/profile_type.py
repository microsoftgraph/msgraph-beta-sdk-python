from enum import Enum

class ProfileType(str, Enum):
    # Settings catalog profile type
    SettingsCatalog = "settingsCatalog",
    # Administrative Templates Profile Type
    AdministrativeTemplates = "administrativeTemplates",
    # Imported Administrative Templates Profile Type
    ImportedADMXTemplates = "importedADMXTemplates",
    # OEM Device related App Config Profile Type
    OemAppConfig = "oemAppConfig",
    # Hardware Configuration Profile Type
    HardwareConfig = "hardwareConfig",
    # DCV1 Endpoint Protection Profile Type
    DcV1EndpointProtection = "dcV1EndpointProtection",
    # DCV1 Device Restrictions Profile Type
    DcV1DeviceRestrictions = "dcV1DeviceRestrictions",

