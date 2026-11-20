from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .enforcement_mode import EnforcementMode
    from .policy_effects import PolicyEffects
    from .policy_evaluation_error_detail import PolicyEvaluationErrorDetail

@dataclass
class PoliciesEvaluationDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The appliedPolicyEffects property
    applied_policy_effects: Optional[PolicyEffects] = None
    # The assignedPolicyDisplayName property
    assigned_policy_display_name: Optional[str] = None
    # The assignmentUniqueName property
    assignment_unique_name: Optional[str] = None
    # The enforcementMode property
    enforcement_mode: Optional[EnforcementMode] = None
    # The errorDetails property
    error_details: Optional[PolicyEvaluationErrorDetail] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The reasons property
    reasons: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PoliciesEvaluationDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PoliciesEvaluationDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PoliciesEvaluationDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .enforcement_mode import EnforcementMode
        from .policy_effects import PolicyEffects
        from .policy_evaluation_error_detail import PolicyEvaluationErrorDetail

        from .enforcement_mode import EnforcementMode
        from .policy_effects import PolicyEffects
        from .policy_evaluation_error_detail import PolicyEvaluationErrorDetail

        fields: dict[str, Callable[[Any], None]] = {
            "appliedPolicyEffects": lambda n : setattr(self, 'applied_policy_effects', n.get_collection_of_enum_values(PolicyEffects)),
            "assignedPolicyDisplayName": lambda n : setattr(self, 'assigned_policy_display_name', n.get_str_value()),
            "assignmentUniqueName": lambda n : setattr(self, 'assignment_unique_name', n.get_str_value()),
            "enforcementMode": lambda n : setattr(self, 'enforcement_mode', n.get_enum_value(EnforcementMode)),
            "errorDetails": lambda n : setattr(self, 'error_details', n.get_object_value(PolicyEvaluationErrorDetail)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reasons": lambda n : setattr(self, 'reasons', n.get_collection_of_primitive_values(str)),
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
        writer.write_enum_value("appliedPolicyEffects", self.applied_policy_effects)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

