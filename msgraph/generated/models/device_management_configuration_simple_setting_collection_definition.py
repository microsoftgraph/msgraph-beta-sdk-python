from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition

from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition

@dataclass
class DeviceManagementConfigurationSimpleSettingCollectionDefinition(DeviceManagementConfigurationSimpleSettingDefinition):
    # Maximum number of simple settings in the collection. Valid values 1 to 100
    maximum_count: Optional[int] = None
    # Minimum number of simple settings in the collection. Valid values 1 to 100
    minimum_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementConfigurationSimpleSettingCollectionDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationSimpleSettingCollectionDefinition
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationSimpleSettingCollectionDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition

        from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition

        fields: Dict[str, Callable[[Any], None]] = {
            "maximumCount": lambda n : setattr(self, 'maximum_count', n.get_int_value()),
            "minimumCount": lambda n : setattr(self, 'minimum_count', n.get_int_value()),
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
        writer.write_int_value("maximumCount", self.maximum_count)
        writer.write_int_value("minimumCount", self.minimum_count)
    

