from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_integer_setting_value_default_template, device_management_configuration_integer_setting_value_definition_template, device_management_configuration_simple_setting_value_template

from . import device_management_configuration_simple_setting_value_template

@dataclass
class DeviceManagementConfigurationIntegerSettingValueTemplate(device_management_configuration_simple_setting_value_template.DeviceManagementConfigurationSimpleSettingValueTemplate):
    odata_type = "#microsoft.graph.deviceManagementConfigurationIntegerSettingValueTemplate"
    # Integer Setting Value Default Template.
    default_value: Optional[device_management_configuration_integer_setting_value_default_template.DeviceManagementConfigurationIntegerSettingValueDefaultTemplate] = None
    # Recommended value definition.
    recommended_value_definition: Optional[device_management_configuration_integer_setting_value_definition_template.DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate] = None
    # Required value definition.
    required_value_definition: Optional[device_management_configuration_integer_setting_value_definition_template.DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationIntegerSettingValueTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationIntegerSettingValueTemplate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationIntegerSettingValueTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_integer_setting_value_default_template, device_management_configuration_integer_setting_value_definition_template, device_management_configuration_simple_setting_value_template

        from . import device_management_configuration_integer_setting_value_default_template, device_management_configuration_integer_setting_value_definition_template, device_management_configuration_simple_setting_value_template

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_object_value(device_management_configuration_integer_setting_value_default_template.DeviceManagementConfigurationIntegerSettingValueDefaultTemplate)),
            "recommendedValueDefinition": lambda n : setattr(self, 'recommended_value_definition', n.get_object_value(device_management_configuration_integer_setting_value_definition_template.DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate)),
            "requiredValueDefinition": lambda n : setattr(self, 'required_value_definition', n.get_object_value(device_management_configuration_integer_setting_value_definition_template.DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate)),
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
        writer.write_object_value("defaultValue", self.default_value)
        writer.write_object_value("recommendedValueDefinition", self.recommended_value_definition)
        writer.write_object_value("requiredValueDefinition", self.required_value_definition)
    

