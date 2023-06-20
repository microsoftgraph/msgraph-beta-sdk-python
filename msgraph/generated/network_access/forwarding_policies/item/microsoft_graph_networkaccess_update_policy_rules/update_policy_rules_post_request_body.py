from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.networkaccess import policy_rule_delta

@dataclass
class UpdatePolicyRulesPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The rules property
    rules: Optional[List[policy_rule_delta.PolicyRuleDelta]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdatePolicyRulesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdatePolicyRulesPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UpdatePolicyRulesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.networkaccess import policy_rule_delta

        from .....models.networkaccess import policy_rule_delta

        fields: Dict[str, Callable[[Any], None]] = {
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(policy_rule_delta.PolicyRuleDelta)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("rules", self.rules)
        writer.write_additional_data_value(self.additional_data)
    

