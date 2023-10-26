from enum import Enum

class DeviceManagementConfigurationWindowsSkus(str, Enum):
    Unknown = "unknown",
    WindowsHome = "windowsHome",
    WindowsProfessional = "windowsProfessional",
    WindowsEnterprise = "windowsEnterprise",
    WindowsEducation = "windowsEducation",
    WindowsMobile = "windowsMobile",
    WindowsMobileEnterprise = "windowsMobileEnterprise",
    WindowsTeamSurface = "windowsTeamSurface",
    Iot = "iot",
    IotEnterprise = "iotEnterprise",
    HoloLens = "holoLens",
    HoloLensEnterprise = "holoLensEnterprise",
    HolographicForBusiness = "holographicForBusiness",
    WindowsMultiSession = "windowsMultiSession",
    SurfaceHub = "surfaceHub",

