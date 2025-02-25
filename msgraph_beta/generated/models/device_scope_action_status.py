from enum import Enum

class DeviceScopeActionStatus(str, Enum):
    # Indicates the device scope action failed to trigger.
    Failed = "failed",
    # Indicates the device scope action was successfully triggered.
    Succeeded = "succeeded",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

