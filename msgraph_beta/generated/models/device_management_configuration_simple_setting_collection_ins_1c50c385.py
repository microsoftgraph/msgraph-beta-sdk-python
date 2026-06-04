from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate
    from .device_management_configuration_simple_setting_value_template import DeviceManagementConfigurationSimpleSettingValueTemplate

from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

@dataclass
class DeviceManagementConfigurationSimpleSettingCollectionIns_1c50c385(DeviceManagementConfigurationSettingInstanceTemplate, Parsable):
    """
    Simple Setting Collection Instance Template Original name: DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionInstanceTemplate"
    # Linked policy may append values which are not present in the template.
    allow_unmanaged_values: Optional[bool] = None
    # Simple Setting Collection Value Template
    simple_setting_collection_value_template: Optional[list[DeviceManagementConfigurationSimpleSettingValueTemplate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationSimpleSettingCollectionIns_1c50c385:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSimpleSettingCollectionIns_1c50c385
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationSimpleSettingCollectionIns_1c50c385()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate
        from .device_management_configuration_simple_setting_value_template import DeviceManagementConfigurationSimpleSettingValueTemplate

        from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate
        from .device_management_configuration_simple_setting_value_template import DeviceManagementConfigurationSimpleSettingValueTemplate

        fields: dict[str, Callable[[Any], None]] = {
            "allowUnmanagedValues": lambda n : setattr(self, 'allow_unmanaged_values', n.get_bool_value()),
            "simpleSettingCollectionValueTemplate": lambda n : setattr(self, 'simple_setting_collection_value_template', n.get_collection_of_object_values(DeviceManagementConfigurationSimpleSettingValueTemplate)),
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
        writer.write_collection_of_object_values("simpleSettingCollectionValueTemplate", self.simple_setting_collection_value_template)
    

