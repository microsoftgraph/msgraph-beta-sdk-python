from enum import Enum

class DeviceScopeActionStatus(str, Enum):
    # Indicates the device scope action failed to trigger.
    Failed = "failed",
    # Indicates the device scope action was successfully triggered.
    Succeeded = "succeeded",
    # Placeholder value for future expansion.
    UnknownFutureValue = "unknownFutureValue",

