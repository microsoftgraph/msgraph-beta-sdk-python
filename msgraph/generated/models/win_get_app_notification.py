from enum import Enum

class WinGetAppNotification(Enum):
    # Show all notifications.
    ShowAll = "showAll",
    # Only show restart notification and suppress other notifications.
    ShowReboot = "showReboot",
    # Hide all notifications.
    HideAll = "hideAll",
    # Unknown future value, reserved for future usage as expandable enum.
    UnknownFutureValue = "unknownFutureValue",

