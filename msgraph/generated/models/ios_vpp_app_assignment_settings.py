from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_app_assignment_settings = lazy_import('msgraph.generated.models.mobile_app_assignment_settings')

class IosVppAppAssignmentSettings(mobile_app_assignment_settings.MobileAppAssignmentSettings):
    def __init__(self,) -> None:
        """
        Instantiates a new IosVppAppAssignmentSettings and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosVppAppAssignmentSettings"
        # Whether or not the app can be removed by the user.
        self._is_removable: Optional[bool] = None
        # Whether or not to uninstall the app when device is removed from Intune.
        self._uninstall_on_device_removal: Optional[bool] = None
        # Whether or not to use device licensing.
        self._use_device_licensing: Optional[bool] = None
        # The VPN Configuration Id to apply for this app.
        self._vpn_configuration_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosVppAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosVppAppAssignmentSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosVppAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "isRemovable": lambda n : setattr(self, 'is_removable', n.get_bool_value()),
            "uninstallOnDeviceRemoval": lambda n : setattr(self, 'uninstall_on_device_removal', n.get_bool_value()),
            "useDeviceLicensing": lambda n : setattr(self, 'use_device_licensing', n.get_bool_value()),
            "vpnConfigurationId": lambda n : setattr(self, 'vpn_configuration_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_removable(self,) -> Optional[bool]:
        """
        Gets the isRemovable property value. Whether or not the app can be removed by the user.
        Returns: Optional[bool]
        """
        return self._is_removable
    
    @is_removable.setter
    def is_removable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRemovable property value. Whether or not the app can be removed by the user.
        Args:
            value: Value to set for the is_removable property.
        """
        self._is_removable = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isRemovable", self.is_removable)
        writer.write_bool_value("uninstallOnDeviceRemoval", self.uninstall_on_device_removal)
        writer.write_bool_value("useDeviceLicensing", self.use_device_licensing)
        writer.write_str_value("vpnConfigurationId", self.vpn_configuration_id)
    
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
    
    @property
    def vpn_configuration_id(self,) -> Optional[str]:
        """
        Gets the vpnConfigurationId property value. The VPN Configuration Id to apply for this app.
        Returns: Optional[str]
        """
        return self._vpn_configuration_id
    
    @vpn_configuration_id.setter
    def vpn_configuration_id(self,value: Optional[str] = None) -> None:
        """
        Sets the vpnConfigurationId property value. The VPN Configuration Id to apply for this app.
        Args:
            value: Value to set for the vpn_configuration_id property.
        """
        self._vpn_configuration_id = value
    

