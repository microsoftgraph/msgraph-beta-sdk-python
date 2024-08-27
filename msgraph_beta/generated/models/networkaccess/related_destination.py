from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .networking_protocol import NetworkingProtocol
    from .related_resource import RelatedResource

from .related_resource import RelatedResource

@dataclass
class RelatedDestination(RelatedResource):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.relatedDestination"
    # The fqdn property
    fqdn: Optional[str] = None
    # The ip property
    ip: Optional[str] = None
    # The networkingProtocol property
    networking_protocol: Optional[NetworkingProtocol] = None
    # The port property
    port: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RelatedDestination:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RelatedDestination
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RelatedDestination()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .networking_protocol import NetworkingProtocol
        from .related_resource import RelatedResource

        from .networking_protocol import NetworkingProtocol
        from .related_resource import RelatedResource

        fields: Dict[str, Callable[[Any], None]] = {
            "fqdn": lambda n : setattr(self, 'fqdn', n.get_str_value()),
            "ip": lambda n : setattr(self, 'ip', n.get_str_value()),
            "networkingProtocol": lambda n : setattr(self, 'networking_protocol', n.get_enum_value(NetworkingProtocol)),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
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
        writer.write_str_value("fqdn", self.fqdn)
        writer.write_str_value("ip", self.ip)
        writer.write_enum_value("networkingProtocol", self.networking_protocol)
        writer.write_int_value("port", self.port)
    

