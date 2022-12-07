from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_answer = lazy_import('msgraph.generated.models.access_package_answer')
access_package_question = lazy_import('msgraph.generated.models.access_package_question')
request_schedule = lazy_import('msgraph.generated.models.request_schedule')

class AccessPackageAssignmentRequestRequirements(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageAssignmentRequestRequirements and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Answers that have already been provided.
        self._existing_answers: Optional[List[access_package_answer.AccessPackageAnswer]] = None
        # Indicates whether a request must be approved by an approver.
        self._is_approval_required: Optional[bool] = None
        # Indicates whether approval is required when a user tries to extend their access.
        self._is_approval_required_for_extension: Optional[bool] = None
        # Indicates whether the requestor is allowed to set a custom schedule.
        self._is_custom_assignment_schedule_allowed: Optional[bool] = None
        # Indicates whether a requestor must supply justification when submitting an assignment request.
        self._is_requestor_justification_required: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The description of the policy that the user is trying to request access using.
        self._policy_description: Optional[str] = None
        # The display name of the policy that the user is trying to request access using.
        self._policy_display_name: Optional[str] = None
        # The identifier of the policy that these requirements are associated with. This identifier can be used when creating a new assignment request.
        self._policy_id: Optional[str] = None
        # Questions that are configured on the policy. The questions can be required or optional; callers can determine whether a question is required or optional based on the isRequired property on accessPackageQuestion.
        self._questions: Optional[List[access_package_question.AccessPackageQuestion]] = None
        # Schedule restrictions enforced, if any.
        self._schedule: Optional[request_schedule.RequestSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentRequestRequirements:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentRequestRequirements
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAssignmentRequestRequirements()
    
    @property
    def existing_answers(self,) -> Optional[List[access_package_answer.AccessPackageAnswer]]:
        """
        Gets the existingAnswers property value. Answers that have already been provided.
        Returns: Optional[List[access_package_answer.AccessPackageAnswer]]
        """
        return self._existing_answers
    
    @existing_answers.setter
    def existing_answers(self,value: Optional[List[access_package_answer.AccessPackageAnswer]] = None) -> None:
        """
        Sets the existingAnswers property value. Answers that have already been provided.
        Args:
            value: Value to set for the existingAnswers property.
        """
        self._existing_answers = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "existing_answers": lambda n : setattr(self, 'existing_answers', n.get_collection_of_object_values(access_package_answer.AccessPackageAnswer)),
            "is_approval_required": lambda n : setattr(self, 'is_approval_required', n.get_bool_value()),
            "is_approval_required_for_extension": lambda n : setattr(self, 'is_approval_required_for_extension', n.get_bool_value()),
            "is_custom_assignment_schedule_allowed": lambda n : setattr(self, 'is_custom_assignment_schedule_allowed', n.get_bool_value()),
            "is_requestor_justification_required": lambda n : setattr(self, 'is_requestor_justification_required', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policy_description": lambda n : setattr(self, 'policy_description', n.get_str_value()),
            "policy_display_name": lambda n : setattr(self, 'policy_display_name', n.get_str_value()),
            "policy_id": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "questions": lambda n : setattr(self, 'questions', n.get_collection_of_object_values(access_package_question.AccessPackageQuestion)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(request_schedule.RequestSchedule)),
        }
        return fields
    
    @property
    def is_approval_required(self,) -> Optional[bool]:
        """
        Gets the isApprovalRequired property value. Indicates whether a request must be approved by an approver.
        Returns: Optional[bool]
        """
        return self._is_approval_required
    
    @is_approval_required.setter
    def is_approval_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isApprovalRequired property value. Indicates whether a request must be approved by an approver.
        Args:
            value: Value to set for the isApprovalRequired property.
        """
        self._is_approval_required = value
    
    @property
    def is_approval_required_for_extension(self,) -> Optional[bool]:
        """
        Gets the isApprovalRequiredForExtension property value. Indicates whether approval is required when a user tries to extend their access.
        Returns: Optional[bool]
        """
        return self._is_approval_required_for_extension
    
    @is_approval_required_for_extension.setter
    def is_approval_required_for_extension(self,value: Optional[bool] = None) -> None:
        """
        Sets the isApprovalRequiredForExtension property value. Indicates whether approval is required when a user tries to extend their access.
        Args:
            value: Value to set for the isApprovalRequiredForExtension property.
        """
        self._is_approval_required_for_extension = value
    
    @property
    def is_custom_assignment_schedule_allowed(self,) -> Optional[bool]:
        """
        Gets the isCustomAssignmentScheduleAllowed property value. Indicates whether the requestor is allowed to set a custom schedule.
        Returns: Optional[bool]
        """
        return self._is_custom_assignment_schedule_allowed
    
    @is_custom_assignment_schedule_allowed.setter
    def is_custom_assignment_schedule_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCustomAssignmentScheduleAllowed property value. Indicates whether the requestor is allowed to set a custom schedule.
        Args:
            value: Value to set for the isCustomAssignmentScheduleAllowed property.
        """
        self._is_custom_assignment_schedule_allowed = value
    
    @property
    def is_requestor_justification_required(self,) -> Optional[bool]:
        """
        Gets the isRequestorJustificationRequired property value. Indicates whether a requestor must supply justification when submitting an assignment request.
        Returns: Optional[bool]
        """
        return self._is_requestor_justification_required
    
    @is_requestor_justification_required.setter
    def is_requestor_justification_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRequestorJustificationRequired property value. Indicates whether a requestor must supply justification when submitting an assignment request.
        Args:
            value: Value to set for the isRequestorJustificationRequired property.
        """
        self._is_requestor_justification_required = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def policy_description(self,) -> Optional[str]:
        """
        Gets the policyDescription property value. The description of the policy that the user is trying to request access using.
        Returns: Optional[str]
        """
        return self._policy_description
    
    @policy_description.setter
    def policy_description(self,value: Optional[str] = None) -> None:
        """
        Sets the policyDescription property value. The description of the policy that the user is trying to request access using.
        Args:
            value: Value to set for the policyDescription property.
        """
        self._policy_description = value
    
    @property
    def policy_display_name(self,) -> Optional[str]:
        """
        Gets the policyDisplayName property value. The display name of the policy that the user is trying to request access using.
        Returns: Optional[str]
        """
        return self._policy_display_name
    
    @policy_display_name.setter
    def policy_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the policyDisplayName property value. The display name of the policy that the user is trying to request access using.
        Args:
            value: Value to set for the policyDisplayName property.
        """
        self._policy_display_name = value
    
    @property
    def policy_id(self,) -> Optional[str]:
        """
        Gets the policyId property value. The identifier of the policy that these requirements are associated with. This identifier can be used when creating a new assignment request.
        Returns: Optional[str]
        """
        return self._policy_id
    
    @policy_id.setter
    def policy_id(self,value: Optional[str] = None) -> None:
        """
        Sets the policyId property value. The identifier of the policy that these requirements are associated with. This identifier can be used when creating a new assignment request.
        Args:
            value: Value to set for the policyId property.
        """
        self._policy_id = value
    
    @property
    def questions(self,) -> Optional[List[access_package_question.AccessPackageQuestion]]:
        """
        Gets the questions property value. Questions that are configured on the policy. The questions can be required or optional; callers can determine whether a question is required or optional based on the isRequired property on accessPackageQuestion.
        Returns: Optional[List[access_package_question.AccessPackageQuestion]]
        """
        return self._questions
    
    @questions.setter
    def questions(self,value: Optional[List[access_package_question.AccessPackageQuestion]] = None) -> None:
        """
        Sets the questions property value. Questions that are configured on the policy. The questions can be required or optional; callers can determine whether a question is required or optional based on the isRequired property on accessPackageQuestion.
        Args:
            value: Value to set for the questions property.
        """
        self._questions = value
    
    @property
    def schedule(self,) -> Optional[request_schedule.RequestSchedule]:
        """
        Gets the schedule property value. Schedule restrictions enforced, if any.
        Returns: Optional[request_schedule.RequestSchedule]
        """
        return self._schedule
    
    @schedule.setter
    def schedule(self,value: Optional[request_schedule.RequestSchedule] = None) -> None:
        """
        Sets the schedule property value. Schedule restrictions enforced, if any.
        Args:
            value: Value to set for the schedule property.
        """
        self._schedule = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
        writer.write_additional_data_value(self.additional_data)
    

