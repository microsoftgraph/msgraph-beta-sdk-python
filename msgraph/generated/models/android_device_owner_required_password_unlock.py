from enum import Enum

class AndroidDeviceOwnerRequiredPasswordUnlock(Enum):
    # Timeout period before strong authentication is required is set to the device's default.
    DeviceDefault = "deviceDefault",
    # Timeout period before strong authentication is required is set to 24 hours.
    Daily = "daily",
    # Unknown future value (reserved, not used right now)
    UnkownFutureValue = "unkownFutureValue",

