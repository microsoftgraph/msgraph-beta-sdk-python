from enum import Enum

class DeviceManagementScriptRunState(str, Enum):
    # Default value. Indicates that the script execution status is unknown for the device.
    Unknown = "unknown",
    # Indicates that the script ran successfully for the device.
    Success = "success",
    # Indicates that the script resulted in failure for the device.
    Fail = "fail",
    # Indicates that the discovery script was unable to complete on the device.
    ScriptError = "scriptError",
    # Indicates that the script has not yet started running on the device.
    Pending = "pending",
    # Indicates that the script is not applicable for this device.
    NotApplicable = "notApplicable",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

