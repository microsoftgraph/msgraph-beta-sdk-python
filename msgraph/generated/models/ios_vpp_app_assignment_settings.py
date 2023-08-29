from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app_assignment_settings import MobileAppAssignmentSettings

from .mobile_app_assignment_settings import MobileAppAssignmentSettings

@dataclass
class IosVppAppAssignmentSettings(MobileAppAssignmentSettings):
    """
    Contains properties used to assign an iOS VPP mobile app to a group.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosVppAppAssignmentSettings"
    # Whether or not the app can be removed by the user.
    is_removable: Optional[bool] = None
    # When TRUE, indicates that the app should not be automatically updated with the latest version from Apple app store. When FALSE, indicates that the app may be auto updated. By default, this property is set to null which internally is treated as FALSE.
    prevent_auto_app_update: Optional[bool] = None
    # When TRUE, indicates that the app should not be backed up to iCloud. When FALSE, indicates that the app may be backed up to iCloud. By default, this property is set to null which internally is treated as FALSE.
    prevent_managed_app_backup: Optional[bool] = None
    # Whether or not to uninstall the app when device is removed from Intune.
    uninstall_on_device_removal: Optional[bool] = None
    # Whether or not to use device licensing.
    use_device_licensing: Optional[bool] = None
    # The VPN Configuration Id to apply for this app.
    vpn_configuration_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosVppAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosVppAppAssignmentSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosVppAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings

        from .mobile_app_assignment_settings import MobileAppAssignmentSettings

        fields: Dict[str, Callable[[Any], None]] = {
            "isRemovable": lambda n : setattr(self, 'is_removable', n.get_bool_value()),
            "preventAutoAppUpdate": lambda n : setattr(self, 'prevent_auto_app_update', n.get_bool_value()),
            "preventManagedAppBackup": lambda n : setattr(self, 'prevent_managed_app_backup', n.get_bool_value()),
            "uninstallOnDeviceRemoval": lambda n : setattr(self, 'uninstall_on_device_removal', n.get_bool_value()),
            "useDeviceLicensing": lambda n : setattr(self, 'use_device_licensing', n.get_bool_value()),
            "vpnConfigurationId": lambda n : setattr(self, 'vpn_configuration_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("isRemovable", self.is_removable)
        writer.write_bool_value("preventAutoAppUpdate", self.prevent_auto_app_update)
        writer.write_bool_value("preventManagedAppBackup", self.prevent_managed_app_backup)
        writer.write_bool_value("uninstallOnDeviceRemoval", self.uninstall_on_device_removal)
        writer.write_bool_value("useDeviceLicensing", self.use_device_licensing)
        writer.write_str_value("vpnConfigurationId", self.vpn_configuration_id)
    

