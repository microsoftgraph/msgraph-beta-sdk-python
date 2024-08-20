from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application import Application
    from .application_segment import ApplicationSegment
    from .private_network_destination_type import PrivateNetworkDestinationType
    from .private_network_protocol import PrivateNetworkProtocol

from .application_segment import ApplicationSegment

@dataclass
class IpApplicationSegment(ApplicationSegment):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.ipApplicationSegment"
    # The application property
    application: Optional[Application] = None
    # The destinationHost property
    destination_host: Optional[str] = None
    # The destinationType property
    destination_type: Optional[PrivateNetworkDestinationType] = None
    # The port property
    port: Optional[int] = None
    # The ports property
    ports: Optional[List[str]] = None
    # The protocol property
    protocol: Optional[PrivateNetworkProtocol] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IpApplicationSegment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IpApplicationSegment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IpApplicationSegment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .application import Application
        from .application_segment import ApplicationSegment
        from .private_network_destination_type import PrivateNetworkDestinationType
        from .private_network_protocol import PrivateNetworkProtocol

        from .application import Application
        from .application_segment import ApplicationSegment
        from .private_network_destination_type import PrivateNetworkDestinationType
        from .private_network_protocol import PrivateNetworkProtocol

        fields: Dict[str, Callable[[Any], None]] = {
            "application": lambda n : setattr(self, 'application', n.get_object_value(Application)),
            "destinationHost": lambda n : setattr(self, 'destination_host', n.get_str_value()),
            "destinationType": lambda n : setattr(self, 'destination_type', n.get_enum_value(PrivateNetworkDestinationType)),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "ports": lambda n : setattr(self, 'ports', n.get_collection_of_primitive_values(str)),
            "protocol": lambda n : setattr(self, 'protocol', n.get_collection_of_enum_values(PrivateNetworkProtocol)),
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
        writer.write_object_value("application", self.application)
        writer.write_str_value("destinationHost", self.destination_host)
        writer.write_enum_value("destinationType", self.destination_type)
        writer.write_int_value("port", self.port)
        writer.write_collection_of_primitive_values("ports", self.ports)
        writer.write_enum_value("protocol", self.protocol)
    

