from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import forwarding_policy_link, policy, status
    from .. import entity

from .. import entity

@dataclass
class PolicyLink(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The policy property
    policy: Optional[policy.Policy] = None
    # The state property
    state: Optional[status.Status] = None
    # The version property
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PolicyLink:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PolicyLink
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.forwardingPolicyLink".casefold():
            from . import forwarding_policy_link

            return forwarding_policy_link.ForwardingPolicyLink()
        return PolicyLink()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import forwarding_policy_link, policy, status
        from .. import entity

        from . import forwarding_policy_link, policy, status
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(policy.Policy)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(status.Status)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_object_value("policy", self.policy)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("version", self.version)
    

