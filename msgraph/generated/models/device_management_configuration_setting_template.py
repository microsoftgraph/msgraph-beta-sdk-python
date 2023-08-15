from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
    from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementConfigurationSettingTemplate(Entity):
    """
    Setting Template
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # List of related Setting Definitions
    setting_definitions: Optional[List[DeviceManagementConfigurationSettingDefinition]] = None
    # Setting Instance Template
    setting_instance_template: Optional[DeviceManagementConfigurationSettingInstanceTemplate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSettingTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSettingTemplate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationSettingTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
        from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate
        from .entity import Entity

        from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition
        from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "settingDefinitions": lambda n : setattr(self, 'setting_definitions', n.get_collection_of_object_values(DeviceManagementConfigurationSettingDefinition)),
            "settingInstanceTemplate": lambda n : setattr(self, 'setting_instance_template', n.get_object_value(DeviceManagementConfigurationSettingInstanceTemplate)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("settingDefinitions", self.setting_definitions)
        writer.write_object_value("settingInstanceTemplate", self.setting_instance_template)
    

