from enum import Enum

class DeviceEventLevel(Enum):
    # Indicates that the device event level is none.
    None_escaped = "none",
    # Indicates that the device event level is verbose.
    Verbose = "verbose",
    # Indicates that the device event level is information.
    Information = "information",
    # Indicates that the device event level is warning.
    Warning = "warning",
    # Indicates that the device event level is error.
    Error = "error",
    # Indicates that the device event level is critical.
    Critical = "critical",
    # Placeholder value for future expansion.
    UnknownFutureValue = "unknownFutureValue",
