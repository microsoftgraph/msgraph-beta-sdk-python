from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.conditional_access_context import ConditionalAccessContext
    from ....models.conditional_access_what_if_conditions import ConditionalAccessWhatIfConditions
    from ....models.conditional_access_what_if_subject import ConditionalAccessWhatIfSubject

@dataclass
class EvaluatePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The appliedPoliciesOnly property
    applied_policies_only: Optional[bool] = None
    # The conditionalAccessContext property
    conditional_access_context: Optional[ConditionalAccessContext] = None
    # The conditionalAccessWhatIfConditions property
    conditional_access_what_if_conditions: Optional[ConditionalAccessWhatIfConditions] = None
    # The conditionalAccessWhatIfSubject property
    conditional_access_what_if_subject: Optional[ConditionalAccessWhatIfSubject] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EvaluatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EvaluatePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EvaluatePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models.conditional_access_context import ConditionalAccessContext
        from ....models.conditional_access_what_if_conditions import ConditionalAccessWhatIfConditions
        from ....models.conditional_access_what_if_subject import ConditionalAccessWhatIfSubject

        from ....models.conditional_access_context import ConditionalAccessContext
        from ....models.conditional_access_what_if_conditions import ConditionalAccessWhatIfConditions
        from ....models.conditional_access_what_if_subject import ConditionalAccessWhatIfSubject

        fields: Dict[str, Callable[[Any], None]] = {
            "appliedPoliciesOnly": lambda n : setattr(self, 'applied_policies_only', n.get_bool_value()),
            "conditionalAccessContext": lambda n : setattr(self, 'conditional_access_context', n.get_object_value(ConditionalAccessContext)),
            "conditionalAccessWhatIfConditions": lambda n : setattr(self, 'conditional_access_what_if_conditions', n.get_object_value(ConditionalAccessWhatIfConditions)),
            "conditionalAccessWhatIfSubject": lambda n : setattr(self, 'conditional_access_what_if_subject', n.get_object_value(ConditionalAccessWhatIfSubject)),
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
        writer.write_bool_value("appliedPoliciesOnly", self.applied_policies_only)
        writer.write_object_value("conditionalAccessContext", self.conditional_access_context)
        writer.write_object_value("conditionalAccessWhatIfConditions", self.conditional_access_what_if_conditions)
        writer.write_object_value("conditionalAccessWhatIfSubject", self.conditional_access_what_if_subject)
        writer.write_additional_data_value(self.additional_data)
    

