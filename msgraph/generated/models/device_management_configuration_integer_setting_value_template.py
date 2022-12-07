from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_integer_setting_value_default_template = lazy_import('msgraph.generated.models.device_management_configuration_integer_setting_value_default_template')
device_management_configuration_integer_setting_value_definition_template = lazy_import('msgraph.generated.models.device_management_configuration_integer_setting_value_definition_template')
device_management_configuration_simple_setting_value_template = lazy_import('msgraph.generated.models.device_management_configuration_simple_setting_value_template')

class DeviceManagementConfigurationIntegerSettingValueTemplate(device_management_configuration_simple_setting_value_template.DeviceManagementConfigurationSimpleSettingValueTemplate):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationIntegerSettingValueTemplate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationIntegerSettingValueTemplate"
        # Integer Setting Value Default Template.
        self._default_value: Optional[device_management_configuration_integer_setting_value_default_template.DeviceManagementConfigurationIntegerSettingValueDefaultTemplate] = None
        # Recommended value definition.
        self._recommended_value_definition: Optional[device_management_configuration_integer_setting_value_definition_template.DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate] = None
        # Required value definition.
        self._required_value_definition: Optional[device_management_configuration_integer_setting_value_definition_template.DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationIntegerSettingValueTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationIntegerSettingValueTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationIntegerSettingValueTemplate()
    
    @property
    def default_value(self,) -> Optional[device_management_configuration_integer_setting_value_default_template.DeviceManagementConfigurationIntegerSettingValueDefaultTemplate]:
        """
        Gets the defaultValue property value. Integer Setting Value Default Template.
        Returns: Optional[device_management_configuration_integer_setting_value_default_template.DeviceManagementConfigurationIntegerSettingValueDefaultTemplate]
        """
        return self._default_value
    
    @default_value.setter
    def default_value(self,value: Optional[device_management_configuration_integer_setting_value_default_template.DeviceManagementConfigurationIntegerSettingValueDefaultTemplate] = None) -> None:
        """
        Sets the defaultValue property value. Integer Setting Value Default Template.
        Args:
            value: Value to set for the defaultValue property.
        """
        self._default_value = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_value": lambda n : setattr(self, 'default_value', n.get_object_value(device_management_configuration_integer_setting_value_default_template.DeviceManagementConfigurationIntegerSettingValueDefaultTemplate)),
            "recommended_value_definition": lambda n : setattr(self, 'recommended_value_definition', n.get_object_value(device_management_configuration_integer_setting_value_definition_template.DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate)),
            "required_value_definition": lambda n : setattr(self, 'required_value_definition', n.get_object_value(device_management_configuration_integer_setting_value_definition_template.DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def recommended_value_definition(self,) -> Optional[device_management_configuration_integer_setting_value_definition_template.DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate]:
        """
        Gets the recommendedValueDefinition property value. Recommended value definition.
        Returns: Optional[device_management_configuration_integer_setting_value_definition_template.DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate]
        """
        return self._recommended_value_definition
    
    @recommended_value_definition.setter
    def recommended_value_definition(self,value: Optional[device_management_configuration_integer_setting_value_definition_template.DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate] = None) -> None:
        """
        Sets the recommendedValueDefinition property value. Recommended value definition.
        Args:
            value: Value to set for the recommendedValueDefinition property.
        """
        self._recommended_value_definition = value
    
    @property
    def required_value_definition(self,) -> Optional[device_management_configuration_integer_setting_value_definition_template.DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate]:
        """
        Gets the requiredValueDefinition property value. Required value definition.
        Returns: Optional[device_management_configuration_integer_setting_value_definition_template.DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate]
        """
        return self._required_value_definition
    
    @required_value_definition.setter
    def required_value_definition(self,value: Optional[device_management_configuration_integer_setting_value_definition_template.DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate] = None) -> None:
        """
        Sets the requiredValueDefinition property value. Required value definition.
        Args:
            value: Value to set for the requiredValueDefinition property.
        """
        self._required_value_definition = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("defaultValue", self.default_value)
        writer.write_object_value("recommendedValueDefinition", self.recommended_value_definition)
        writer.write_object_value("requiredValueDefinition", self.required_value_definition)
    

