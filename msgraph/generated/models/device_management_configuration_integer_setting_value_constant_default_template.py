from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_integer_setting_value_default_template = lazy_import('msgraph.generated.models.device_management_configuration_integer_setting_value_default_template')

class DeviceManagementConfigurationIntegerSettingValueConstantDefaultTemplate(device_management_configuration_integer_setting_value_default_template.DeviceManagementConfigurationIntegerSettingValueDefaultTemplate):
    @property
    def constant_value(self,) -> Optional[int]:
        """
        Gets the constantValue property value. Default Constant Value. Valid values -2147483648 to 2147483647
        Returns: Optional[int]
        """
        return self._constant_value
    
    @constant_value.setter
    def constant_value(self,value: Optional[int] = None) -> None:
        """
        Sets the constantValue property value. Default Constant Value. Valid values -2147483648 to 2147483647
        Args:
            value: Value to set for the constantValue property.
        """
        self._constant_value = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationIntegerSettingValueConstantDefaultTemplate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationIntegerSettingValueConstantDefaultTemplate"
        # Default Constant Value. Valid values -2147483648 to 2147483647
        self._constant_value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationIntegerSettingValueConstantDefaultTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationIntegerSettingValueConstantDefaultTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationIntegerSettingValueConstantDefaultTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "constant_value": lambda n : setattr(self, 'constant_value', n.get_int_value()),
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
        writer.write_int_value("constantValue", self.constant_value)
    

