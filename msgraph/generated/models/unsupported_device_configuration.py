from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration, unsupported_device_configuration_detail

from . import device_configuration

@dataclass
class UnsupportedDeviceConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.unsupportedDeviceConfiguration"
    # Details describing why the entity is unsupported. This collection can contain a maximum of 1000 elements.
    details: Optional[List[unsupported_device_configuration_detail.UnsupportedDeviceConfigurationDetail]] = None
    # The type of entity that would be returned otherwise.
    original_entity_type_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnsupportedDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnsupportedDeviceConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnsupportedDeviceConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_configuration, unsupported_device_configuration_detail

        fields: Dict[str, Callable[[Any], None]] = {
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(unsupported_device_configuration_detail.UnsupportedDeviceConfigurationDetail)),
            "originalEntityTypeName": lambda n : setattr(self, 'original_entity_type_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("details", self.details)
        writer.write_str_value("originalEntityTypeName", self.original_entity_type_name)
    

