from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .forwarding_rule import ForwardingRule
    from .networking_protocol import NetworkingProtocol

from .forwarding_rule import ForwardingRule

@dataclass
class InternetAccessForwardingRule(ForwardingRule, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.internetAccessForwardingRule"
    # The ports property
    ports: Optional[List[str]] = None
    # The protocol property
    protocol: Optional[NetworkingProtocol] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InternetAccessForwardingRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InternetAccessForwardingRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InternetAccessForwardingRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .forwarding_rule import ForwardingRule
        from .networking_protocol import NetworkingProtocol

        from .forwarding_rule import ForwardingRule
        from .networking_protocol import NetworkingProtocol

        fields: Dict[str, Callable[[Any], None]] = {
            "ports": lambda n : setattr(self, 'ports', n.get_collection_of_primitive_values(str)),
            "protocol": lambda n : setattr(self, 'protocol', n.get_enum_value(NetworkingProtocol)),
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
        from .forwarding_rule import ForwardingRule
        from .networking_protocol import NetworkingProtocol

        writer.write_collection_of_primitive_values("ports", self.ports)
        writer.write_enum_value("protocol", self.protocol)
    

