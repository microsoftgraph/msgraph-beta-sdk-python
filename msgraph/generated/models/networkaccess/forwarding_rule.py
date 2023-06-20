from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import forwarding_rule_action, m365_forwarding_rule, network_destination_type, policy_rule, private_access_forwarding_rule, rule_destination

from . import policy_rule

@dataclass
class ForwardingRule(policy_rule.PolicyRule):
    odata_type = "#microsoft.graph.networkaccess.forwardingRule"
    # The action property
    action: Optional[forwarding_rule_action.ForwardingRuleAction] = None
    # The destinations property
    destinations: Optional[List[rule_destination.RuleDestination]] = None
    # The ruleType property
    rule_type: Optional[network_destination_type.NetworkDestinationType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ForwardingRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ForwardingRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.m365ForwardingRule".casefold():
            from . import m365_forwarding_rule

            return m365_forwarding_rule.M365ForwardingRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.privateAccessForwardingRule".casefold():
            from . import private_access_forwarding_rule

            return private_access_forwarding_rule.PrivateAccessForwardingRule()
        return ForwardingRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import forwarding_rule_action, m365_forwarding_rule, network_destination_type, policy_rule, private_access_forwarding_rule, rule_destination

        from . import forwarding_rule_action, m365_forwarding_rule, network_destination_type, policy_rule, private_access_forwarding_rule, rule_destination

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(forwarding_rule_action.ForwardingRuleAction)),
            "destinations": lambda n : setattr(self, 'destinations', n.get_collection_of_object_values(rule_destination.RuleDestination)),
            "ruleType": lambda n : setattr(self, 'rule_type', n.get_enum_value(network_destination_type.NetworkDestinationType)),
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
        writer.write_enum_value("action", self.action)
        writer.write_collection_of_object_values("destinations", self.destinations)
        writer.write_enum_value("ruleType", self.rule_type)
    

