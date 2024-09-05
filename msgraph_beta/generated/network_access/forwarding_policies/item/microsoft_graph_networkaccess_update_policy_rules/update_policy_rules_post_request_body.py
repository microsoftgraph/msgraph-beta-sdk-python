from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.networkaccess.policy_rule_delta import PolicyRuleDelta

@dataclass
class UpdatePolicyRulesPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The rules property
    rules: Optional[List[PolicyRuleDelta]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdatePolicyRulesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdatePolicyRulesPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdatePolicyRulesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.networkaccess.policy_rule_delta import PolicyRuleDelta

        from .....models.networkaccess.policy_rule_delta import PolicyRuleDelta

        fields: Dict[str, Callable[[Any], None]] = {
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(PolicyRuleDelta)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("rules", self.rules)
        writer.write_additional_data_value(self.additional_data)
    

