from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_setting_definition = lazy_import('msgraph.generated.models.device_management_configuration_setting_definition')
device_management_configuration_setting_instance_template = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance_template')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementConfigurationSettingTemplate(entity.Entity):
    """
    Setting Template
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementConfigurationSettingTemplate and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of related Setting Definitions
        self._setting_definitions: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]] = None
        # Setting Instance Template
        self._setting_instance_template: Optional[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationSettingTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "setting_definitions": lambda n : setattr(self, 'setting_definitions', n.get_collection_of_object_values(device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition)),
            "setting_instance_template": lambda n : setattr(self, 'setting_instance_template', n.get_object_value(device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate)),
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
        writer.write_collection_of_object_values("settingDefinitions", self.setting_definitions)
        writer.write_object_value("settingInstanceTemplate", self.setting_instance_template)
    
    @property
    def setting_definitions(self,) -> Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]]:
        """
        Gets the settingDefinitions property value. List of related Setting Definitions
        Returns: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]]
        """
        return self._setting_definitions
    
    @setting_definitions.setter
    def setting_definitions(self,value: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]] = None) -> None:
        """
        Sets the settingDefinitions property value. List of related Setting Definitions
        Args:
            value: Value to set for the settingDefinitions property.
        """
        self._setting_definitions = value
    
    @property
    def setting_instance_template(self,) -> Optional[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate]:
        """
        Gets the settingInstanceTemplate property value. Setting Instance Template
        Returns: Optional[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate]
        """
        return self._setting_instance_template
    
    @setting_instance_template.setter
    def setting_instance_template(self,value: Optional[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate] = None) -> None:
        """
        Sets the settingInstanceTemplate property value. Setting Instance Template
        Args:
            value: Value to set for the settingInstanceTemplate property.
        """
        self._setting_instance_template = value
    

