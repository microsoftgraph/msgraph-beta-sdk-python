from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_configuration_setting_definition, device_management_configuration_setting_instance_template, entity

from . import entity

@dataclass
class DeviceManagementConfigurationSettingTemplate(entity.Entity):
    """
    Setting Template
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # List of related Setting Definitions
    setting_definitions: Optional[List[device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition]] = None
    # Setting Instance Template
    setting_instance_template: Optional[device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate] = None
    
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
        from . import device_management_configuration_setting_definition, device_management_configuration_setting_instance_template, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "settingDefinitions": lambda n : setattr(self, 'setting_definitions', n.get_collection_of_object_values(device_management_configuration_setting_definition.DeviceManagementConfigurationSettingDefinition)),
            "settingInstanceTemplate": lambda n : setattr(self, 'setting_instance_template', n.get_object_value(device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate)),
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
    

