from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_simple_setting_value_template = lazy_import('msgraph.generated.models.device_management_configuration_simple_setting_value_template')
device_management_configuration_string_setting_value_default_template = lazy_import('msgraph.generated.models.device_management_configuration_string_setting_value_default_template')

class DeviceManagementConfigurationStringSettingValueTemplate(device_management_configuration_simple_setting_value_template.DeviceManagementConfigurationSimpleSettingValueTemplate):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationStringSettingValueTemplate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationStringSettingValueTemplate"
        # String Setting Value Default Template.
        self._default_value: Optional[device_management_configuration_string_setting_value_default_template.DeviceManagementConfigurationStringSettingValueDefaultTemplate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationStringSettingValueTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationStringSettingValueTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationStringSettingValueTemplate()
    
    @property
    def default_value(self,) -> Optional[device_management_configuration_string_setting_value_default_template.DeviceManagementConfigurationStringSettingValueDefaultTemplate]:
        """
        Gets the defaultValue property value. String Setting Value Default Template.
        Returns: Optional[device_management_configuration_string_setting_value_default_template.DeviceManagementConfigurationStringSettingValueDefaultTemplate]
        """
        return self._default_value
    
    @default_value.setter
    def default_value(self,value: Optional[device_management_configuration_string_setting_value_default_template.DeviceManagementConfigurationStringSettingValueDefaultTemplate] = None) -> None:
        """
        Sets the defaultValue property value. String Setting Value Default Template.
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
            "default_value": lambda n : setattr(self, 'default_value', n.get_object_value(device_management_configuration_string_setting_value_default_template.DeviceManagementConfigurationStringSettingValueDefaultTemplate)),
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
        writer.write_object_value("defaultValue", self.default_value)
    

