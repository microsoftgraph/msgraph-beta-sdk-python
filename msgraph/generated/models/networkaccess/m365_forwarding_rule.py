from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import forwarding_category, forwarding_rule, networking_protocol

from . import forwarding_rule

@dataclass
class M365ForwardingRule(forwarding_rule.ForwardingRule):
    odata_type = "#microsoft.graph.networkaccess.m365ForwardingRule"
    # The category property
    category: Optional[forwarding_category.ForwardingCategory] = None
    # The ports property
    ports: Optional[List[str]] = None
    # The protocol property
    protocol: Optional[networking_protocol.NetworkingProtocol] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> M365ForwardingRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: M365ForwardingRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return M365ForwardingRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import forwarding_category, forwarding_rule, networking_protocol

        from . import forwarding_category, forwarding_rule, networking_protocol

        fields: Dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(forwarding_category.ForwardingCategory)),
            "ports": lambda n : setattr(self, 'ports', n.get_collection_of_primitive_values(str)),
            "protocol": lambda n : setattr(self, 'protocol', n.get_enum_value(networking_protocol.NetworkingProtocol)),
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
        writer.write_enum_value("category", self.category)
        writer.write_collection_of_primitive_values("ports", self.ports)
        writer.write_enum_value("protocol", self.protocol)
    

