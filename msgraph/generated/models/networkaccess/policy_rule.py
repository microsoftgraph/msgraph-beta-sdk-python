from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import forwarding_rule, m365_forwarding_rule, private_access_forwarding_rule
    from .. import entity

from .. import entity

@dataclass
class PolicyRule(entity.Entity):
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PolicyRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PolicyRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.forwardingRule".casefold():
            from . import forwarding_rule

            return forwarding_rule.ForwardingRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.m365ForwardingRule".casefold():
            from . import m365_forwarding_rule

            return m365_forwarding_rule.M365ForwardingRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.privateAccessForwardingRule".casefold():
            from . import private_access_forwarding_rule

            return private_access_forwarding_rule.PrivateAccessForwardingRule()
        return PolicyRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import forwarding_rule, m365_forwarding_rule, private_access_forwarding_rule
        from .. import entity

        from . import forwarding_rule, m365_forwarding_rule, private_access_forwarding_rule
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_str_value("name", self.name)
    

