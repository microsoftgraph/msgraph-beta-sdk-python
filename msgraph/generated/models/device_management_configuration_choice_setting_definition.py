from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_choice_setting_collection_definition, device_management_configuration_option_definition, device_management_configuration_setting_definition

from . import device_management_configuration_setting_definition

class DeviceManagementConfigurationChoiceSettingDefinition(device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationChoiceSettingDefinition and sets the default values.
        """
        super().__init__()
        # Default option for the choice setting.
        self._default_option_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Options for the setting that can be selected.
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
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionDefinition":
                from . import device_management_configuration_choice_setting_collection_definition

                return device_management_configuration_choice_setting_collection_definition.DeviceManagementConfigurationChoiceSettingCollectionDefinition()
        return DeviceManagementConfigurationChoiceSettingDefinition()
    
    @property
    def default_option_id(self,) -> Optional[str]:
        """
        Gets the defaultOptionId property value. Default option for the choice setting.
        Returns: Optional[str]
        """
        return self._default_option_id
    
    @default_option_id.setter
    def default_option_id(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultOptionId property value. Default option for the choice setting.
        Args:
            value: Value to set for the default_option_id property.
        """
        self._default_option_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_configuration_choice_setting_collection_definition, device_management_configuration_option_definition, device_management_configuration_setting_definition

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultOptionId": lambda n : setattr(self, 'default_option_id', n.get_str_value()),
            "options": lambda n : setattr(self, 'options', n.get_collection_of_object_values(device_management_configuration_option_definition.DeviceManagementConfigurationOptionDefinition)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def options(self,) -> Optional[List[device_management_configuration_option_definition.DeviceManagementConfigurationOptionDefinition]]:
        """
        Gets the options property value. Options for the setting that can be selected.
        Returns: Optional[List[device_management_configuration_option_definition.DeviceManagementConfigurationOptionDefinition]]
        """
        return self._options
    
    @options.setter
    def options(self,value: Optional[List[device_management_configuration_option_definition.DeviceManagementConfigurationOptionDefinition]] = None) -> None:
        """
        Sets the options property value. Options for the setting that can be selected.
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
    

