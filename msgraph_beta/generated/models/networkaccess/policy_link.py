from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .filtering_policy_link import FilteringPolicyLink
    from .forwarding_policy_link import ForwardingPolicyLink
    from .policy import Policy
    from .status import Status

from ..entity import Entity

@dataclass
class PolicyLink(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The policy property
    policy: Optional[Policy] = None
    # The state property
    state: Optional[Status] = None
    # Version.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyLink:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyLink
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.filteringPolicyLink".casefold():
            from .filtering_policy_link import FilteringPolicyLink

            return FilteringPolicyLink()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.forwardingPolicyLink".casefold():
            from .forwarding_policy_link import ForwardingPolicyLink

            return ForwardingPolicyLink()
        return PolicyLink()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .filtering_policy_link import FilteringPolicyLink
        from .forwarding_policy_link import ForwardingPolicyLink
        from .policy import Policy
        from .status import Status

        from ..entity import Entity
        from .filtering_policy_link import FilteringPolicyLink
        from .forwarding_policy_link import ForwardingPolicyLink
        from .policy import Policy
        from .status import Status

        fields: Dict[str, Callable[[Any], None]] = {
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(Policy)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(Status)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_object_value("policy", self.policy)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("version", self.version)
    

