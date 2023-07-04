from enum import Enum

class Win32LobAppDeliveryOptimizationPriority(str, Enum):
    # Not configured or background normal delivery optimization priority.
    NotConfigured = "notConfigured",
    # Foreground delivery optimization priority.
    Foreground = "foreground",

