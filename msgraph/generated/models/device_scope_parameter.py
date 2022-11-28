from enum import Enum

class DeviceScopeParameter(Enum):
    # Device Scope parameter is not set
    None_escaped = "none",
    # use Scope Tag as parameter for the device scope configuration.
    ScopeTag = "scopeTag",
    # Placeholder value for future expansion.
    UnknownFutureValue = "unknownFutureValue",

