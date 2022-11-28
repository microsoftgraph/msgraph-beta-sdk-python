from enum import Enum

class UserExperienceAnalyticsOperatingSystemRestartCategory(Enum):
    # Unknown
    Unknown = "unknown",
    # Restart with update
    RestartWithUpdate = "restartWithUpdate",
    # Restart without update
    RestartWithoutUpdate = "restartWithoutUpdate",
    # Blue screen restart
    BlueScreen = "blueScreen",
    # Shutdown with update
    ShutdownWithUpdate = "shutdownWithUpdate",
    # Shutdown without update
    ShutdownWithoutUpdate = "shutdownWithoutUpdate",
    # Long power button press
    LongPowerButtonPress = "longPowerButtonPress",
    # Boot error
    BootError = "bootError",
    # Update
    Update = "update",

