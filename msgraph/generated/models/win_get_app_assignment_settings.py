from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_app_assignment_settings = lazy_import('msgraph.generated.models.mobile_app_assignment_settings')
win_get_app_install_time_settings = lazy_import('msgraph.generated.models.win_get_app_install_time_settings')
win_get_app_notification = lazy_import('msgraph.generated.models.win_get_app_notification')
win_get_app_restart_settings = lazy_import('msgraph.generated.models.win_get_app_restart_settings')

class WinGetAppAssignmentSettings(mobile_app_assignment_settings.MobileAppAssignmentSettings):
    def __init__(self,) -> None:
        """
        Instantiates a new WinGetAppAssignmentSettings and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.winGetAppAssignmentSettings"
        # The install time settings to apply for this app assignment.
        self._install_time_settings: Optional[win_get_app_install_time_settings.WinGetAppInstallTimeSettings] = None
        # Contains value for notification status.
        self._notifications: Optional[win_get_app_notification.WinGetAppNotification] = None
        # The reboot settings to apply for this app assignment.
        self._restart_settings: Optional[win_get_app_restart_settings.WinGetAppRestartSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WinGetAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WinGetAppAssignmentSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WinGetAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "install_time_settings": lambda n : setattr(self, 'install_time_settings', n.get_object_value(win_get_app_install_time_settings.WinGetAppInstallTimeSettings)),
            "notifications": lambda n : setattr(self, 'notifications', n.get_enum_value(win_get_app_notification.WinGetAppNotification)),
            "restart_settings": lambda n : setattr(self, 'restart_settings', n.get_object_value(win_get_app_restart_settings.WinGetAppRestartSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def install_time_settings(self,) -> Optional[win_get_app_install_time_settings.WinGetAppInstallTimeSettings]:
        """
        Gets the installTimeSettings property value. The install time settings to apply for this app assignment.
        Returns: Optional[win_get_app_install_time_settings.WinGetAppInstallTimeSettings]
        """
        return self._install_time_settings
    
    @install_time_settings.setter
    def install_time_settings(self,value: Optional[win_get_app_install_time_settings.WinGetAppInstallTimeSettings] = None) -> None:
        """
        Sets the installTimeSettings property value. The install time settings to apply for this app assignment.
        Args:
            value: Value to set for the installTimeSettings property.
        """
        self._install_time_settings = value
    
    @property
    def notifications(self,) -> Optional[win_get_app_notification.WinGetAppNotification]:
        """
        Gets the notifications property value. Contains value for notification status.
        Returns: Optional[win_get_app_notification.WinGetAppNotification]
        """
        return self._notifications
    
    @notifications.setter
    def notifications(self,value: Optional[win_get_app_notification.WinGetAppNotification] = None) -> None:
        """
        Sets the notifications property value. Contains value for notification status.
        Args:
            value: Value to set for the notifications property.
        """
        self._notifications = value
    
    @property
    def restart_settings(self,) -> Optional[win_get_app_restart_settings.WinGetAppRestartSettings]:
        """
        Gets the restartSettings property value. The reboot settings to apply for this app assignment.
        Returns: Optional[win_get_app_restart_settings.WinGetAppRestartSettings]
        """
        return self._restart_settings
    
    @restart_settings.setter
    def restart_settings(self,value: Optional[win_get_app_restart_settings.WinGetAppRestartSettings] = None) -> None:
        """
        Sets the restartSettings property value. The reboot settings to apply for this app assignment.
        Args:
            value: Value to set for the restartSettings property.
        """
        self._restart_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("installTimeSettings", self.install_time_settings)
        writer.write_enum_value("notifications", self.notifications)
        writer.write_object_value("restartSettings", self.restart_settings)
    

