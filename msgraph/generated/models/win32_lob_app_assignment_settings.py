from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_app_assignment_settings, mobile_app_install_time_settings, win32_lob_app_delivery_optimization_priority, win32_lob_app_notification, win32_lob_app_restart_settings

from . import mobile_app_assignment_settings

@dataclass
class Win32LobAppAssignmentSettings(mobile_app_assignment_settings.MobileAppAssignmentSettings):
    odata_type = "#microsoft.graph.win32LobAppAssignmentSettings"
    # Contains value for delivery optimization priority.
    delivery_optimization_priority: Optional[win32_lob_app_delivery_optimization_priority.Win32LobAppDeliveryOptimizationPriority] = None
    # The install time settings to apply for this app assignment.
    install_time_settings: Optional[mobile_app_install_time_settings.MobileAppInstallTimeSettings] = None
    # Contains value for notification status.
    notifications: Optional[win32_lob_app_notification.Win32LobAppNotification] = None
    # The reboot settings to apply for this app assignment.
    restart_settings: Optional[win32_lob_app_restart_settings.Win32LobAppRestartSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppAssignmentSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_app_assignment_settings, mobile_app_install_time_settings, win32_lob_app_delivery_optimization_priority, win32_lob_app_notification, win32_lob_app_restart_settings

        from . import mobile_app_assignment_settings, mobile_app_install_time_settings, win32_lob_app_delivery_optimization_priority, win32_lob_app_notification, win32_lob_app_restart_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "deliveryOptimizationPriority": lambda n : setattr(self, 'delivery_optimization_priority', n.get_enum_value(win32_lob_app_delivery_optimization_priority.Win32LobAppDeliveryOptimizationPriority)),
            "installTimeSettings": lambda n : setattr(self, 'install_time_settings', n.get_object_value(mobile_app_install_time_settings.MobileAppInstallTimeSettings)),
            "notifications": lambda n : setattr(self, 'notifications', n.get_enum_value(win32_lob_app_notification.Win32LobAppNotification)),
            "restartSettings": lambda n : setattr(self, 'restart_settings', n.get_object_value(win32_lob_app_restart_settings.Win32LobAppRestartSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("deliveryOptimizationPriority", self.delivery_optimization_priority)
        writer.write_object_value("installTimeSettings", self.install_time_settings)
        writer.write_enum_value("notifications", self.notifications)
        writer.write_object_value("restartSettings", self.restart_settings)
    

