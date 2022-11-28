from enum import Enum

class DeviceManagementAutopilotPolicyComplianceStatus(Enum):
    Unknown = "unknown",
    Compliant = "compliant",
    Installed = "installed",
    NotCompliant = "notCompliant",
    NotInstalled = "notInstalled",
    Error = "error",

