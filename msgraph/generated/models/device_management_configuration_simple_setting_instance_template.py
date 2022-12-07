from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_setting_instance_template = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance_template')
device_management_configuration_simple_setting_value_template = lazy_import('msgraph.generated.models.device_management_configuration_simple_setting_value_template')

class DeviceManagementConfigurationSimpleSettingInstanceTemplate(device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationSimpleSettingInstanceTemplate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationSimpleSettingInstanceTemplate"
        # Simple Setting Value Template
        self._simple_setting_value_template: Optional[device_management_configuration_simple_setting_value_template.DeviceManagementConfigurationSimpleSettingValueTemplate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSimpleSettingInstanceTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSimpleSettingInstanceTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationSimpleSettingInstanceTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "simple_setting_value_template": lambda n : setattr(self, 'simple_setting_value_template', n.get_object_value(device_management_configuration_simple_setting_value_template.DeviceManagementConfigurationSimpleSettingValueTemplate)),
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
        writer.write_object_value("simpleSettingValueTemplate", self.simple_setting_value_template)
    
    @property
    def simple_setting_value_template(self,) -> Optional[device_management_configuration_simple_setting_value_template.DeviceManagementConfigurationSimpleSettingValueTemplate]:
        """
        Gets the simpleSettingValueTemplate property value. Simple Setting Value Template
        Returns: Optional[device_management_configuration_simple_setting_value_template.DeviceManagementConfigurationSimpleSettingValueTemplate]
        """
        return self._simple_setting_value_template
    
    @simple_setting_value_template.setter
    def simple_setting_value_template(self,value: Optional[device_management_configuration_simple_setting_value_template.DeviceManagementConfigurationSimpleSettingValueTemplate] = None) -> None:
        """
        Sets the simpleSettingValueTemplate property value. Simple Setting Value Template
        Args:
            value: Value to set for the simpleSettingValueTemplate property.
        """
        self._simple_setting_value_template = value
    

