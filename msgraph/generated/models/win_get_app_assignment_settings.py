from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_app_assignment_settings, win_get_app_install_time_settings, win_get_app_notification, win_get_app_restart_settings

from . import mobile_app_assignment_settings

@dataclass
class WinGetAppAssignmentSettings(mobile_app_assignment_settings.MobileAppAssignmentSettings):
    odata_type = "#microsoft.graph.winGetAppAssignmentSettings"
    # The install time settings to apply for this app assignment.
    install_time_settings: Optional[win_get_app_install_time_settings.WinGetAppInstallTimeSettings] = None
    # Contains value for notification status.
    notifications: Optional[win_get_app_notification.WinGetAppNotification] = None
    # The reboot settings to apply for this app assignment.
    restart_settings: Optional[win_get_app_restart_settings.WinGetAppRestartSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WinGetAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WinGetAppAssignmentSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WinGetAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_app_assignment_settings, win_get_app_install_time_settings, win_get_app_notification, win_get_app_restart_settings

        from . import mobile_app_assignment_settings, win_get_app_install_time_settings, win_get_app_notification, win_get_app_restart_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "installTimeSettings": lambda n : setattr(self, 'install_time_settings', n.get_object_value(win_get_app_install_time_settings.WinGetAppInstallTimeSettings)),
            "notifications": lambda n : setattr(self, 'notifications', n.get_enum_value(win_get_app_notification.WinGetAppNotification)),
            "restartSettings": lambda n : setattr(self, 'restart_settings', n.get_object_value(win_get_app_restart_settings.WinGetAppRestartSettings)),
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
        writer.write_object_value("installTimeSettings", self.install_time_settings)
        writer.write_enum_value("notifications", self.notifications)
        writer.write_object_value("restartSettings", self.restart_settings)
    

