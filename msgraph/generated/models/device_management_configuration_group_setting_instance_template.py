from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_configuration_group_setting_value_template = lazy_import('msgraph.generated.models.device_management_configuration_group_setting_value_template')
device_management_configuration_setting_instance_template = lazy_import('msgraph.generated.models.device_management_configuration_setting_instance_template')

class DeviceManagementConfigurationGroupSettingInstanceTemplate(device_management_configuration_setting_instance_template.DeviceManagementConfigurationSettingInstanceTemplate):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementConfigurationGroupSettingInstanceTemplate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementConfigurationGroupSettingInstanceTemplate"
        # Group Setting Value Template
        self._group_setting_value_template: Optional[device_management_configuration_group_setting_value_template.DeviceManagementConfigurationGroupSettingValueTemplate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationGroupSettingInstanceTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationGroupSettingInstanceTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementConfigurationGroupSettingInstanceTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "group_setting_value_template": lambda n : setattr(self, 'group_setting_value_template', n.get_object_value(device_management_configuration_group_setting_value_template.DeviceManagementConfigurationGroupSettingValueTemplate)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_setting_value_template(self,) -> Optional[device_management_configuration_group_setting_value_template.DeviceManagementConfigurationGroupSettingValueTemplate]:
        """
        Gets the groupSettingValueTemplate property value. Group Setting Value Template
        Returns: Optional[device_management_configuration_group_setting_value_template.DeviceManagementConfigurationGroupSettingValueTemplate]
        """
        return self._group_setting_value_template
    
    @group_setting_value_template.setter
    def group_setting_value_template(self,value: Optional[device_management_configuration_group_setting_value_template.DeviceManagementConfigurationGroupSettingValueTemplate] = None) -> None:
        """
        Sets the groupSettingValueTemplate property value. Group Setting Value Template
        Args:
            value: Value to set for the groupSettingValueTemplate property.
        """
        self._group_setting_value_template = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("groupSettingValueTemplate", self.group_setting_value_template)
    

