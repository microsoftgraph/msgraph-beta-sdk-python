from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_answer import AccessPackageAnswer
    from .access_package_question import AccessPackageQuestion
    from .request_schedule import RequestSchedule
    from .verifiable_credential_requirement_status import VerifiableCredentialRequirementStatus

@dataclass
class AccessPackageAssignmentRequestRequirements(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Answers that have already been provided.
    existing_answers: Optional[List[AccessPackageAnswer]] = None
    # Indicates whether a request must be approved by an approver.
    is_approval_required: Optional[bool] = None
    # Indicates whether approval is required when a user tries to extend their access.
    is_approval_required_for_extension: Optional[bool] = None
    # Indicates whether the requestor is allowed to set a custom schedule.
    is_custom_assignment_schedule_allowed: Optional[bool] = None
    # Indicates whether a requestor must supply justification when submitting an assignment request.
    is_requestor_justification_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The description of the policy that the user is trying to request access using.
    policy_description: Optional[str] = None
    # The display name of the policy that the user is trying to request access using.
    policy_display_name: Optional[str] = None
    # The identifier of the policy that these requirements are associated with. This identifier can be used when creating a new assignment request.
    policy_id: Optional[str] = None
    # Questions that are configured on the policy. The questions can be required or optional; callers can determine whether a question is required or optional based on the isRequired property on accessPackageQuestion.
    questions: Optional[List[AccessPackageQuestion]] = None
    # Schedule restrictions enforced, if any.
    schedule: Optional[RequestSchedule] = None
    # The status of the process to process the verifiable credential, if any.
    verifiable_credential_requirement_status: Optional[VerifiableCredentialRequirementStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageAssignmentRequestRequirements:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentRequestRequirements
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAssignmentRequestRequirements()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_answer import AccessPackageAnswer
        from .access_package_question import AccessPackageQuestion
        from .request_schedule import RequestSchedule
        from .verifiable_credential_requirement_status import VerifiableCredentialRequirementStatus

        from .access_package_answer import AccessPackageAnswer
        from .access_package_question import AccessPackageQuestion
        from .request_schedule import RequestSchedule
        from .verifiable_credential_requirement_status import VerifiableCredentialRequirementStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "existingAnswers": lambda n : setattr(self, 'existing_answers', n.get_collection_of_object_values(AccessPackageAnswer)),
            "isApprovalRequired": lambda n : setattr(self, 'is_approval_required', n.get_bool_value()),
            "isApprovalRequiredForExtension": lambda n : setattr(self, 'is_approval_required_for_extension', n.get_bool_value()),
            "isCustomAssignmentScheduleAllowed": lambda n : setattr(self, 'is_custom_assignment_schedule_allowed', n.get_bool_value()),
            "isRequestorJustificationRequired": lambda n : setattr(self, 'is_requestor_justification_required', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyDescription": lambda n : setattr(self, 'policy_description', n.get_str_value()),
            "policyDisplayName": lambda n : setattr(self, 'policy_display_name', n.get_str_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "questions": lambda n : setattr(self, 'questions', n.get_collection_of_object_values(AccessPackageQuestion)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(RequestSchedule)),
            "verifiableCredentialRequirementStatus": lambda n : setattr(self, 'verifiable_credential_requirement_status', n.get_object_value(VerifiableCredentialRequirementStatus)),
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
        writer.write_collection_of_object_values("existingAnswers", self.existing_answers)
        writer.write_bool_value("isApprovalRequired", self.is_approval_required)
        writer.write_bool_value("isApprovalRequiredForExtension", self.is_approval_required_for_extension)
        writer.write_bool_value("isCustomAssignmentScheduleAllowed", self.is_custom_assignment_schedule_allowed)
        writer.write_bool_value("isRequestorJustificationRequired", self.is_requestor_justification_required)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("policyDescription", self.policy_description)
        writer.write_str_value("policyDisplayName", self.policy_display_name)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_collection_of_object_values("questions", self.questions)
        writer.write_object_value("schedule", self.schedule)
        writer.write_object_value("verifiableCredentialRequirementStatus", self.verifiable_credential_requirement_status)
        writer.write_additional_data_value(self.additional_data)
    

