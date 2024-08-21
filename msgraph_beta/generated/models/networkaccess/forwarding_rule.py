from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .forwarding_rule_action import ForwardingRuleAction
    from .internet_access_forwarding_rule import InternetAccessForwardingRule
    from .m365_forwarding_rule import M365ForwardingRule
    from .network_destination_type import NetworkDestinationType
    from .policy_rule import PolicyRule
    from .private_access_forwarding_rule import PrivateAccessForwardingRule
    from .rule_destination import RuleDestination

from .policy_rule import PolicyRule

@dataclass
class ForwardingRule(PolicyRule):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.forwardingRule"
    # The action property
    action: Optional[ForwardingRuleAction] = None
    # Destinations maintain a list of potential destinations and destination types that the user may access within the context of a network filtering policy. This includes IP addresses and fully qualified domain names (FQDNs)/URLs.
    destinations: Optional[List[RuleDestination]] = None
    # The ruleType property
    rule_type: Optional[NetworkDestinationType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ForwardingRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ForwardingRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.internetAccessForwardingRule".casefold():
            from .internet_access_forwarding_rule import InternetAccessForwardingRule

            return InternetAccessForwardingRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.m365ForwardingRule".casefold():
            from .m365_forwarding_rule import M365ForwardingRule

            return M365ForwardingRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.privateAccessForwardingRule".casefold():
            from .private_access_forwarding_rule import PrivateAccessForwardingRule

            return PrivateAccessForwardingRule()
        return ForwardingRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .forwarding_rule_action import ForwardingRuleAction
        from .internet_access_forwarding_rule import InternetAccessForwardingRule
        from .m365_forwarding_rule import M365ForwardingRule
        from .network_destination_type import NetworkDestinationType
        from .policy_rule import PolicyRule
        from .private_access_forwarding_rule import PrivateAccessForwardingRule
        from .rule_destination import RuleDestination

        from .forwarding_rule_action import ForwardingRuleAction
        from .internet_access_forwarding_rule import InternetAccessForwardingRule
        from .m365_forwarding_rule import M365ForwardingRule
        from .network_destination_type import NetworkDestinationType
        from .policy_rule import PolicyRule
        from .private_access_forwarding_rule import PrivateAccessForwardingRule
        from .rule_destination import RuleDestination

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(ForwardingRuleAction)),
            "destinations": lambda n : setattr(self, 'destinations', n.get_collection_of_object_values(RuleDestination)),
            "ruleType": lambda n : setattr(self, 'rule_type', n.get_enum_value(NetworkDestinationType)),
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
        writer.write_enum_value("action", self.action)
        writer.write_collection_of_object_values("destinations", self.destinations)
        writer.write_enum_value("ruleType", self.rule_type)
    

