from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_option_definition = lazy_import('msgraph.generated.models.device_management_configuration_option_definition')
device_management_configuration_setting_definition = lazy_import('msgraph.generated.models.device_management_configuration_setting_definition')

class DeviceManagementConfigurationChoiceSettingDefinition(device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationChoiceSettingDefinition and sets the default values.
        """
        super().__init__()
        # Default option for choice setting
        self._default_option_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Options for the setting that can be selected
        self._options: Optional[List[device_management_configuration_option_definition.DeviceManagementConfigurationOptionDefinition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationChoiceSettingDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationChoiceSettingDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationChoiceSettingDefinition()
    
    @property
    def default_option_id(self,) -> Optional[str]:
        """
        Gets the defaultOptionId property value. Default option for choice setting
        Returns: Optional[str]
        """
        return self._default_option_id
    
    @default_option_id.setter
    def default_option_id(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultOptionId property value. Default option for choice setting
        Args:
            value: Value to set for the defaultOptionId property.
        """
        self._default_option_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_option_id": lambda n : setattr(self, 'default_option_id', n.get_str_value()),
            "options": lambda n : setattr(self, 'options', n.get_collection_of_object_values(device_management_configuration_option_definition.DeviceManagementConfigurationOptionDefinition)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def options(self,) -> Optional[List[device_management_configuration_option_definition.DeviceManagementConfigurationOptionDefinition]]:
        """
        Gets the options property value. Options for the setting that can be selected
        Returns: Optional[List[device_management_configuration_option_definition.DeviceManagementConfigurationOptionDefinition]]
        """
        return self._options
    
    @options.setter
    def options(self,value: Optional[List[device_management_configuration_option_definition.DeviceManagementConfigurationOptionDefinition]] = None) -> None:
        """
        Sets the options property value. Options for the setting that can be selected
        Args:
            value: Value to set for the options property.
        """
        self._options = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("defaultOptionId", self.default_option_id)
        writer.write_collection_of_object_values("options", self.options)
    

