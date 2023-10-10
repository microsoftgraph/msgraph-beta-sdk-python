from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .user_set import UserSet

@dataclass
class ApprovalStage(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The number of days that a request can be pending a response before it's automatically denied.
    approval_stage_time_out_in_days: Optional[int] = None
    # If escalation is enabled and the primary approvers don't respond before the escalation time, the escalationApprovers are the users who will be asked to approve requests. This can be a collection of singleUser, groupMembers, requestorManager, internalSponsors and externalSponsors.  When creating or updating a policy, if there are no escalation approvers, or escalation approvers aren't required for the stage, the value of this property should be an empty collection.
    escalation_approvers: Optional[List[UserSet]] = None
    # If escalation is required, the time a request can be pending a response from a primary approver.
    escalation_time_in_minutes: Optional[int] = None
    # Indicates whether the approver is required to provide a justification for approving a request.
    is_approver_justification_required: Optional[bool] = None
    # If true, then one or more escalation approvers are configured in this approval stage.
    is_escalation_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The users who are asked to approve requests. A collection of singleUser, groupMembers, requestorManager, internalSponsors, externalSponsors and targetUserSponsors. When creating or updating a policy, include at least one userSet in this collection.
    primary_approvers: Optional[List[UserSet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApprovalStage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApprovalStage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ApprovalStage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .user_set import UserSet

        from .user_set import UserSet

        fields: Dict[str, Callable[[Any], None]] = {
            "approvalStageTimeOutInDays": lambda n : setattr(self, 'approval_stage_time_out_in_days', n.get_int_value()),
            "escalationApprovers": lambda n : setattr(self, 'escalation_approvers', n.get_collection_of_object_values(UserSet)),
            "escalationTimeInMinutes": lambda n : setattr(self, 'escalation_time_in_minutes', n.get_int_value()),
            "isApproverJustificationRequired": lambda n : setattr(self, 'is_approver_justification_required', n.get_bool_value()),
            "isEscalationEnabled": lambda n : setattr(self, 'is_escalation_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "primaryApprovers": lambda n : setattr(self, 'primary_approvers', n.get_collection_of_object_values(UserSet)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("approvalStageTimeOutInDays", self.approval_stage_time_out_in_days)
        writer.write_collection_of_object_values("escalationApprovers", self.escalation_approvers)
        writer.write_int_value("escalationTimeInMinutes", self.escalation_time_in_minutes)
        writer.write_bool_value("isApproverJustificationRequired", self.is_approver_justification_required)
        writer.write_bool_value("isEscalationEnabled", self.is_escalation_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("primaryApprovers", self.primary_approvers)
        writer.write_additional_data_value(self.additional_data)
    

