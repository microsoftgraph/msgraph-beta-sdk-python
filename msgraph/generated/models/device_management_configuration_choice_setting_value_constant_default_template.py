from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_choice_setting_value_default_template = lazy_import('msgraph.generated.models.device_management_configuration_choice_setting_value_default_template')
device_management_configuration_setting_instance_template = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance_template')

class DeviceManagementConfigurationChoiceSettingValueConstantDefaultTemplate(device_management_configuration_choice_setting_value_default_template.DeviceManagementConfigurationChoiceSettingValueDefaultTemplate):
    @property
    def children(self,) -> Optional[List[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate]]:
        """
        Gets the children property value. Option Children
        Returns: Optional[List[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate]]
        """
        return self._children
    
    @children.setter
    def children(self,value: Optional[List[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate]] = None) -> None:
        """
        Sets the children property value. Option Children
        Args:
            value: Value to set for the children property.
        """
        self._children = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationChoiceSettingValueConstantDefaultTemplate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationChoiceSettingValueConstantDefaultTemplate"
        # Option Children
        self._children: Optional[List[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate]] = None
        # Default Constant Value
        self._setting_definition_option_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationChoiceSettingValueConstantDefaultTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationChoiceSettingValueConstantDefaultTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationChoiceSettingValueConstantDefaultTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate)),
            "setting_definition_option_id": lambda n : setattr(self, 'setting_definition_option_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("children", self.children)
        writer.write_str_value("settingDefinitionOptionId", self.setting_definition_option_id)
    
    @property
    def setting_definition_option_id(self,) -> Optional[str]:
        """
        Gets the settingDefinitionOptionId property value. Default Constant Value
        Returns: Optional[str]
        """
        return self._setting_definition_option_id
    
    @setting_definition_option_id.setter
    def setting_definition_option_id(self,value: Optional[str] = None) -> None:
        """
        Sets the settingDefinitionOptionId property value. Default Constant Value
        Args:
            value: Value to set for the settingDefinitionOptionId property.
        """
        self._setting_definition_option_id = value
    

