from enum import Enum

class CloudPcPartnerAgentInstallStatus(Enum):
    Installed = "installed",
    InstallFailed = "installFailed",
    Installing = "installing",
    Uninstalling = "uninstalling",
    UninstallFailed = "uninstallFailed",
    Licensed = "licensed",
    UnknownFutureValue = "unknownFutureValue",

