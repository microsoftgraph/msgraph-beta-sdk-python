from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_group_setting_value_template import DeviceManagementConfigurationGroupSettingValueTemplate
    from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

@dataclass
class DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate(DeviceManagementConfigurationSettingInstanceTemplate, Parsable):
    """
    Group Setting Collection Instance Template
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementConfigurationGroupSettingCollectionInstanceTemplate"
    # Linked policy may append values which are not present in the template.
    allow_unmanaged_values: Optional[bool] = None
    # Group Setting Collection Value Template
    group_setting_collection_value_template: Optional[list[DeviceManagementConfigurationGroupSettingValueTemplate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_group_setting_value_template import DeviceManagementConfigurationGroupSettingValueTemplate
        from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

        from .device_management_configuration_group_setting_value_template import DeviceManagementConfigurationGroupSettingValueTemplate
        from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

        fields: dict[str, Callable[[Any], None]] = {
            "allowUnmanagedValues": lambda n : setattr(self, 'allow_unmanaged_values', n.get_bool_value()),
            "groupSettingCollectionValueTemplate": lambda n : setattr(self, 'group_setting_collection_value_template', n.get_collection_of_object_values(DeviceManagementConfigurationGroupSettingValueTemplate)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("allowUnmanagedValues", self.allow_unmanaged_values)
        writer.write_collection_of_object_values("groupSettingCollectionValueTemplate", self.group_setting_collection_value_template)
    

