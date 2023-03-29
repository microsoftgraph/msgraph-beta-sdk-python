from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_reference_setting_value, device_management_configuration_simple_setting_value

from . import device_management_configuration_simple_setting_value

class DeviceManagementConfigurationStringSettingValue(device_management_configuration_simple_setting_value.DeviceManagementConfigurationSimpleSettingValue):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationStringSettingValue and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationStringSettingValue"
        # Value of the string setting.
        self._value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationStringSettingValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationStringSettingValue
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationReferenceSettingValue":
                from . import device_management_configuration_reference_setting_value

                return device_management_configuration_reference_setting_value.DeviceManagementConfigurationReferenceSettingValue()
        return DeviceManagementConfigurationStringSettingValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_reference_setting_value, device_management_configuration_simple_setting_value

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_str_value("value", self.value)
    
    @property
    def value(self,) -> Optional[str]:
        """
        Gets the value property value. Value of the string setting.
        Returns: Optional[str]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[str] = None) -> None:
        """
        Sets the value property value. Value of the string setting.
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

