from enum import Enum

class DefenderSecurityCenterNotificationsFromAppType(Enum):
    # Not Configured
    NotConfigured = "notConfigured",
    # Block non-critical notifications
    BlockNoncriticalNotifications = "blockNoncriticalNotifications",
    # Block all notifications
    BlockAllNotifications = "blockAllNotifications",

