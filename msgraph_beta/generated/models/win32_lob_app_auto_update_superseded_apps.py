from enum import Enum

class Win32LobAppAutoUpdateSupersededApps(str, Enum):
    # Indicates that the auto-update superseded apps is not configured and the app will not auto-update the superseded apps.
    NotConfigured = "notConfigured",
    # Indicates that the auto-update superseded apps is enabled and the app will auto-update the superseded apps if the superseded apps are installed on the device.
    Enabled = "enabled",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

