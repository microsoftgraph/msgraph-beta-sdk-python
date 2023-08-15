from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .unsupported_device_configuration_detail import UnsupportedDeviceConfigurationDetail

from .device_configuration import DeviceConfiguration

@dataclass
class UnsupportedDeviceConfiguration(DeviceConfiguration):
    """
    UnsupportedDeviceConfiguration is used when an entity cannot be mapped to another model-compliant subtype of deviceConfiguration.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.unsupportedDeviceConfiguration"
    # Details describing why the entity is unsupported. This collection can contain a maximum of 1000 elements.
    details: Optional[List[UnsupportedDeviceConfigurationDetail]] = None
    # The type of entity that would be returned otherwise.
    original_entity_type_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnsupportedDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnsupportedDeviceConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UnsupportedDeviceConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .unsupported_device_configuration_detail import UnsupportedDeviceConfigurationDetail

        from .device_configuration import DeviceConfiguration
        from .unsupported_device_configuration_detail import UnsupportedDeviceConfigurationDetail

        fields: Dict[str, Callable[[Any], None]] = {
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(UnsupportedDeviceConfigurationDetail)),
            "originalEntityTypeName": lambda n : setattr(self, 'original_entity_type_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("details", self.details)
        writer.write_str_value("originalEntityTypeName", self.original_entity_type_name)
    

