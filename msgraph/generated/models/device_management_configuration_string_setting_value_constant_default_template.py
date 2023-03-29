from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_string_setting_value_default_template

from . import device_management_configuration_string_setting_value_default_template

class DeviceManagementConfigurationStringSettingValueConstantDefaultTemplate(device_management_configuration_string_setting_value_default_template.DeviceManagementConfigurationStringSettingValueDefaultTemplate):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationStringSettingValueConstantDefaultTemplate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationStringSettingValueConstantDefaultTemplate"
        # Default Constant Value
        self._constant_value: Optional[str] = None
    
    @property
    def constant_value(self,) -> Optional[str]:
        """
        Gets the constantValue property value. Default Constant Value
        Returns: Optional[str]
        """
        return self._constant_value
    
    @constant_value.setter
    def constant_value(self,value: Optional[str] = None) -> None:
        """
        Sets the constantValue property value. Default Constant Value
        Args:
            value: Value to set for the constant_value property.
        """
        self._constant_value = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationStringSettingValueConstantDefaultTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationStringSettingValueConstantDefaultTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationStringSettingValueConstantDefaultTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_string_setting_value_default_template

        fields: Dict[str, Callable[[Any], None]] = {
            "constantValue": lambda n : setattr(self, 'constant_value', n.get_str_value()),
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
        writer.write_str_value("constantValue", self.constant_value)
    

