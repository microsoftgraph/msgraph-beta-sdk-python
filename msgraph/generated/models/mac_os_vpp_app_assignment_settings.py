from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_app_assignment_settings

from . import mobile_app_assignment_settings

class MacOsVppAppAssignmentSettings(mobile_app_assignment_settings.MobileAppAssignmentSettings):
    def __init__(self,) -> None:
        """
        Instantiates a new MacOsVppAppAssignmentSettings and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.macOsVppAppAssignmentSettings"
        # When TRUE, indicates that the app should not be automatically updated with the latest version from Apple app store. When FALSE, indicates that the app may be auto updated. By default, this property is set to null which internally is treated as FALSE.
        self._prevent_auto_app_update: Optional[bool] = None
        # When TRUE, indicates that the app should not be backed up to iCloud. When FALSE, indicates that the app may be backed up to iCloud. By default, this property is set to null which internally is treated as FALSE.
        self._prevent_managed_app_backup: Optional[bool] = None
        # Whether or not to uninstall the app when device is removed from Intune.
        self._uninstall_on_device_removal: Optional[bool] = None
        # Whether or not to use device licensing.
        self._use_device_licensing: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOsVppAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOsVppAppAssignmentSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOsVppAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_app_assignment_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "preventAutoAppUpdate": lambda n : setattr(self, 'prevent_auto_app_update', n.get_bool_value()),
            "preventManagedAppBackup": lambda n : setattr(self, 'prevent_managed_app_backup', n.get_bool_value()),
            "uninstallOnDeviceRemoval": lambda n : setattr(self, 'uninstall_on_device_removal', n.get_bool_value()),
            "useDeviceLicensing": lambda n : setattr(self, 'use_device_licensing', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def prevent_auto_app_update(self,) -> Optional[bool]:
        """
        Gets the preventAutoAppUpdate property value. When TRUE, indicates that the app should not be automatically updated with the latest version from Apple app store. When FALSE, indicates that the app may be auto updated. By default, this property is set to null which internally is treated as FALSE.
        Returns: Optional[bool]
        """
        return self._prevent_auto_app_update
    
    @prevent_auto_app_update.setter
    def prevent_auto_app_update(self,value: Optional[bool] = None) -> None:
        """
        Sets the preventAutoAppUpdate property value. When TRUE, indicates that the app should not be automatically updated with the latest version from Apple app store. When FALSE, indicates that the app may be auto updated. By default, this property is set to null which internally is treated as FALSE.
        Args:
            value: Value to set for the prevent_auto_app_update property.
        """
        self._prevent_auto_app_update = value
    
    @property
    def prevent_managed_app_backup(self,) -> Optional[bool]:
        """
        Gets the preventManagedAppBackup property value. When TRUE, indicates that the app should not be backed up to iCloud. When FALSE, indicates that the app may be backed up to iCloud. By default, this property is set to null which internally is treated as FALSE.
        Returns: Optional[bool]
        """
        return self._prevent_managed_app_backup
    
    @prevent_managed_app_backup.setter
    def prevent_managed_app_backup(self,value: Optional[bool] = None) -> None:
        """
        Sets the preventManagedAppBackup property value. When TRUE, indicates that the app should not be backed up to iCloud. When FALSE, indicates that the app may be backed up to iCloud. By default, this property is set to null which internally is treated as FALSE.
        Args:
            value: Value to set for the prevent_managed_app_backup property.
        """
        self._prevent_managed_app_backup = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("preventAutoAppUpdate", self.prevent_auto_app_update)
        writer.write_bool_value("preventManagedAppBackup", self.prevent_managed_app_backup)
        writer.write_bool_value("uninstallOnDeviceRemoval", self.uninstall_on_device_removal)
        writer.write_bool_value("useDeviceLicensing", self.use_device_licensing)
    
    @property
    def uninstall_on_device_removal(self,) -> Optional[bool]:
        """
        Gets the uninstallOnDeviceRemoval property value. Whether or not to uninstall the app when device is removed from Intune.
        Returns: Optional[bool]
        """
        return self._uninstall_on_device_removal
    
    @uninstall_on_device_removal.setter
    def uninstall_on_device_removal(self,value: Optional[bool] = None) -> None:
        """
        Sets the uninstallOnDeviceRemoval property value. Whether or not to uninstall the app when device is removed from Intune.
        Args:
            value: Value to set for the uninstall_on_device_removal property.
        """
        self._uninstall_on_device_removal = value
    
    @property
    def use_device_licensing(self,) -> Optional[bool]:
        """
        Gets the useDeviceLicensing property value. Whether or not to use device licensing.
        Returns: Optional[bool]
        """
        return self._use_device_licensing
    
    @use_device_licensing.setter
    def use_device_licensing(self,value: Optional[bool] = None) -> None:
        """
        Sets the useDeviceLicensing property value. Whether or not to use device licensing.
        Args:
            value: Value to set for the use_device_licensing property.
        """
        self._use_device_licensing = value
    

