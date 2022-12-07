from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_setting_instance = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance')
device_management_configuration_simple_setting_value = lazy_import('msgraph.generated.models.device_management_configuration_simple_setting_value')

class DeviceManagementConfigurationSimpleSettingInstance(device_management_configuration_setting_instance.DeviceManagementConfigurationSettingInstance):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationSimpleSettingInstance and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationSimpleSettingInstance"
        # The simpleSettingValue property
        self._simple_setting_value: Optional[device_management_configuration_simple_setting_value.DeviceManagementConfigurationSimpleSettingValue] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSimpleSettingInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSimpleSettingInstance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationSimpleSettingInstance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "simple_setting_value": lambda n : setattr(self, 'simple_setting_value', n.get_object_value(device_management_configuration_simple_setting_value.DeviceManagementConfigurationSimpleSettingValue)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("simpleSettingValue", self.simple_setting_value)
    
    @property
    def simple_setting_value(self,) -> Optional[device_management_configuration_simple_setting_value.DeviceManagementConfigurationSimpleSettingValue]:
        """
        Gets the simpleSettingValue property value. The simpleSettingValue property
        Returns: Optional[device_management_configuration_simple_setting_value.DeviceManagementConfigurationSimpleSettingValue]
        """
        return self._simple_setting_value
    
    @simple_setting_value.setter
    def simple_setting_value(self,value: Optional[device_management_configuration_simple_setting_value.DeviceManagementConfigurationSimpleSettingValue] = None) -> None:
        """
        Sets the simpleSettingValue property value. The simpleSettingValue property
        Args:
            value: Value to set for the simpleSettingValue property.
        """
        self._simple_setting_value = value
    

