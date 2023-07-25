from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_segment import ApplicationSegment

from .application_segment import ApplicationSegment

@dataclass
class IpApplicationSegment(ApplicationSegment):
    odata_type = "#microsoft.graph.ipApplicationSegment"
    # The destinationHost property
    destination_host: Optional[str] = None
    # The port property
    port: Optional[int] = None
    # The ports property
    ports: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IpApplicationSegment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IpApplicationSegment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IpApplicationSegment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .application_segment import ApplicationSegment

        from .application_segment import ApplicationSegment

        fields: Dict[str, Callable[[Any], None]] = {
            "destinationHost": lambda n : setattr(self, 'destination_host', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "ports": lambda n : setattr(self, 'ports', n.get_collection_of_primitive_values(str)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("destinationHost", self.destination_host)
        writer.write_int_value("port", self.port)
        writer.write_collection_of_primitive_values("ports", self.ports)
    

