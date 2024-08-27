from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.policy_set_assignment import PolicySetAssignment
    from .....models.policy_set_item import PolicySetItem

@dataclass
class UpdatePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The addedPolicySetItems property
    added_policy_set_items: Optional[List[PolicySetItem]] = None
    # The assignments property
    assignments: Optional[List[PolicySetAssignment]] = None
    # The deletedPolicySetItems property
    deleted_policy_set_items: Optional[List[str]] = None
    # The updatedPolicySetItems property
    updated_policy_set_items: Optional[List[PolicySetItem]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdatePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdatePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.policy_set_assignment import PolicySetAssignment
        from .....models.policy_set_item import PolicySetItem

        from .....models.policy_set_assignment import PolicySetAssignment
        from .....models.policy_set_item import PolicySetItem

        fields: Dict[str, Callable[[Any], None]] = {
            "addedPolicySetItems": lambda n : setattr(self, 'added_policy_set_items', n.get_collection_of_object_values(PolicySetItem)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(PolicySetAssignment)),
            "deletedPolicySetItems": lambda n : setattr(self, 'deleted_policy_set_items', n.get_collection_of_primitive_values(str)),
            "updatedPolicySetItems": lambda n : setattr(self, 'updated_policy_set_items', n.get_collection_of_object_values(PolicySetItem)),
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
        writer.write_collection_of_object_values("addedPolicySetItems", self.added_policy_set_items)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_primitive_values("deletedPolicySetItems", self.deleted_policy_set_items)
        writer.write_collection_of_object_values("updatedPolicySetItems", self.updated_policy_set_items)
        writer.write_additional_data_value(self.additional_data)
    

