from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
governance_resource = lazy_import('msgraph.generated.models.governance_resource')
governance_role_assignment_request_status = lazy_import('msgraph.generated.models.governance_role_assignment_request_status')
governance_role_definition = lazy_import('msgraph.generated.models.governance_role_definition')
governance_schedule = lazy_import('msgraph.generated.models.governance_schedule')
governance_subject = lazy_import('msgraph.generated.models.governance_subject')

class GovernanceRoleAssignmentRequest(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def assignment_state(self,) -> Optional[str]:
        """
        Gets the assignmentState property value. Required. The state of the assignment. The possible values are: Eligible (for eligible assignment),  Active (if it is directly assigned), Active (by administrators, or activated on an eligible assignment by the users).
        Returns: Optional[str]
        """
        return self._assignment_state
    
    @assignment_state.setter
    def assignment_state(self,value: Optional[str] = None) -> None:
        """
        Sets the assignmentState property value. Required. The state of the assignment. The possible values are: Eligible (for eligible assignment),  Active (if it is directly assigned), Active (by administrators, or activated on an eligible assignment by the users).
        Args:
            value: Value to set for the assignmentState property.
        """
        self._assignment_state = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new governanceRoleAssignmentRequest and sets the default values.
        """
        super().__init__()
        # Required. The state of the assignment. The possible values are: Eligible (for eligible assignment),  Active (if it is directly assigned), Active (by administrators, or activated on an eligible assignment by the users).
        self._assignment_state: Optional[str] = None
        # If this is a request for role activation, it represents the id of the eligible assignment being referred; Otherwise, the value is null.
        self._linked_eligible_role_assignment_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A message provided by users and administrators when create the request about why it is needed.
        self._reason: Optional[str] = None
        # Read-only. The request create time. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._requested_date_time: Optional[datetime] = None
        # Read-only. The resource that the request aims to.
        self._resource: Optional[governance_resource.GovernanceResource] = None
        # Required. The unique identifier of the Azure resource that is associated with the role assignment request. Azure resources can include subscriptions, resource groups, virtual machines, and SQL databases.
        self._resource_id: Optional[str] = None
        # Read-only. The role definition that the request aims to.
        self._role_definition: Optional[governance_role_definition.GovernanceRoleDefinition] = None
        # Required. The identifier of the Azure role definition that the role assignment request is associated with.
        self._role_definition_id: Optional[str] = None
        # The schedule object of the role assignment request.
        self._schedule: Optional[governance_schedule.GovernanceSchedule] = None
        # The status of the role assignment request.
        self._status: Optional[governance_role_assignment_request_status.GovernanceRoleAssignmentRequestStatus] = None
        # Read-only. The user/group principal.
        self._subject: Optional[governance_subject.GovernanceSubject] = None
        # Required. The unique identifier of the principal or subject that the role assignment request is associated with. Principals can be users, groups, or service principals.
        self._subject_id: Optional[str] = None
        # Required. Representing the type of the operation on the role assignment. The possible values are: AdminAdd , UserAdd , AdminUpdate , AdminRemove , UserRemove , UserExtend , AdminExtend , UserRenew , AdminRenew.
        self._type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GovernanceRoleAssignmentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceRoleAssignmentRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GovernanceRoleAssignmentRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignment_state": lambda n : setattr(self, 'assignment_state', n.get_str_value()),
            "linked_eligible_role_assignment_id": lambda n : setattr(self, 'linked_eligible_role_assignment_id', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "requested_date_time": lambda n : setattr(self, 'requested_date_time', n.get_datetime_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(governance_resource.GovernanceResource)),
            "resource_id": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "role_definition": lambda n : setattr(self, 'role_definition', n.get_object_value(governance_role_definition.GovernanceRoleDefinition)),
            "role_definition_id": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(governance_schedule.GovernanceSchedule)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(governance_role_assignment_request_status.GovernanceRoleAssignmentRequestStatus)),
            "subject": lambda n : setattr(self, 'subject', n.get_object_value(governance_subject.GovernanceSubject)),
            "subject_id": lambda n : setattr(self, 'subject_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def linked_eligible_role_assignment_id(self,) -> Optional[str]:
        """
        Gets the linkedEligibleRoleAssignmentId property value. If this is a request for role activation, it represents the id of the eligible assignment being referred; Otherwise, the value is null.
        Returns: Optional[str]
        """
        return self._linked_eligible_role_assignment_id
    
    @linked_eligible_role_assignment_id.setter
    def linked_eligible_role_assignment_id(self,value: Optional[str] = None) -> None:
        """
        Sets the linkedEligibleRoleAssignmentId property value. If this is a request for role activation, it represents the id of the eligible assignment being referred; Otherwise, the value is null.
        Args:
            value: Value to set for the linkedEligibleRoleAssignmentId property.
        """
        self._linked_eligible_role_assignment_id = value
    
    @property
    def reason(self,) -> Optional[str]:
        """
        Gets the reason property value. A message provided by users and administrators when create the request about why it is needed.
        Returns: Optional[str]
        """
        return self._reason
    
    @reason.setter
    def reason(self,value: Optional[str] = None) -> None:
        """
        Sets the reason property value. A message provided by users and administrators when create the request about why it is needed.
        Args:
            value: Value to set for the reason property.
        """
        self._reason = value
    
    @property
    def requested_date_time(self,) -> Optional[datetime]:
        """
        Gets the requestedDateTime property value. Read-only. The request create time. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._requested_date_time
    
    @requested_date_time.setter
    def requested_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the requestedDateTime property value. Read-only. The request create time. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the requestedDateTime property.
        """
        self._requested_date_time = value
    
    @property
    def resource(self,) -> Optional[governance_resource.GovernanceResource]:
        """
        Gets the resource property value. Read-only. The resource that the request aims to.
        Returns: Optional[governance_resource.GovernanceResource]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[governance_resource.GovernanceResource] = None) -> None:
        """
        Sets the resource property value. Read-only. The resource that the request aims to.
        Args:
            value: Value to set for the resource property.
        """
        self._resource = value
    
    @property
    def resource_id(self,) -> Optional[str]:
        """
        Gets the resourceId property value. Required. The unique identifier of the Azure resource that is associated with the role assignment request. Azure resources can include subscriptions, resource groups, virtual machines, and SQL databases.
        Returns: Optional[str]
        """
        return self._resource_id
    
    @resource_id.setter
    def resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceId property value. Required. The unique identifier of the Azure resource that is associated with the role assignment request. Azure resources can include subscriptions, resource groups, virtual machines, and SQL databases.
        Args:
            value: Value to set for the resourceId property.
        """
        self._resource_id = value
    
    @property
    def role_definition(self,) -> Optional[governance_role_definition.GovernanceRoleDefinition]:
        """
        Gets the roleDefinition property value. Read-only. The role definition that the request aims to.
        Returns: Optional[governance_role_definition.GovernanceRoleDefinition]
        """
        return self._role_definition
    
    @role_definition.setter
    def role_definition(self,value: Optional[governance_role_definition.GovernanceRoleDefinition] = None) -> None:
        """
        Sets the roleDefinition property value. Read-only. The role definition that the request aims to.
        Args:
            value: Value to set for the roleDefinition property.
        """
        self._role_definition = value
    
    @property
    def role_definition_id(self,) -> Optional[str]:
        """
        Gets the roleDefinitionId property value. Required. The identifier of the Azure role definition that the role assignment request is associated with.
        Returns: Optional[str]
        """
        return self._role_definition_id
    
    @role_definition_id.setter
    def role_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleDefinitionId property value. Required. The identifier of the Azure role definition that the role assignment request is associated with.
        Args:
            value: Value to set for the roleDefinitionId property.
        """
        self._role_definition_id = value
    
    @property
    def schedule(self,) -> Optional[governance_schedule.GovernanceSchedule]:
        """
        Gets the schedule property value. The schedule object of the role assignment request.
        Returns: Optional[governance_schedule.GovernanceSchedule]
        """
        return self._schedule
    
    @schedule.setter
    def schedule(self,value: Optional[governance_schedule.GovernanceSchedule] = None) -> None:
        """
        Sets the schedule property value. The schedule object of the role assignment request.
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
        super().serialize(writer)
        writer.write_str_value("assignmentState", self.assignment_state)
        writer.write_str_value("linkedEligibleRoleAssignmentId", self.linked_eligible_role_assignment_id)
        writer.write_str_value("reason", self.reason)
        writer.write_datetime_value("requestedDateTime", self.requested_date_time)
        writer.write_object_value("resource", self.resource)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_object_value("roleDefinition", self.role_definition)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
        writer.write_object_value("schedule", self.schedule)
        writer.write_object_value("status", self.status)
        writer.write_object_value("subject", self.subject)
        writer.write_str_value("subjectId", self.subject_id)
        writer.write_str_value("type", self.type)
    
    @property
    def status(self,) -> Optional[governance_role_assignment_request_status.GovernanceRoleAssignmentRequestStatus]:
        """
        Gets the status property value. The status of the role assignment request.
        Returns: Optional[governance_role_assignment_request_status.GovernanceRoleAssignmentRequestStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[governance_role_assignment_request_status.GovernanceRoleAssignmentRequestStatus] = None) -> None:
        """
        Sets the status property value. The status of the role assignment request.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def subject(self,) -> Optional[governance_subject.GovernanceSubject]:
        """
        Gets the subject property value. Read-only. The user/group principal.
        Returns: Optional[governance_subject.GovernanceSubject]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[governance_subject.GovernanceSubject] = None) -> None:
        """
        Sets the subject property value. Read-only. The user/group principal.
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    
    @property
    def subject_id(self,) -> Optional[str]:
        """
        Gets the subjectId property value. Required. The unique identifier of the principal or subject that the role assignment request is associated with. Principals can be users, groups, or service principals.
        Returns: Optional[str]
        """
        return self._subject_id
    
    @subject_id.setter
    def subject_id(self,value: Optional[str] = None) -> None:
        """
        Sets the subjectId property value. Required. The unique identifier of the principal or subject that the role assignment request is associated with. Principals can be users, groups, or service principals.
        Args:
            value: Value to set for the subjectId property.
        """
        self._subject_id = value
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. Required. Representing the type of the operation on the role assignment. The possible values are: AdminAdd , UserAdd , AdminUpdate , AdminRemove , UserRemove , UserExtend , AdminExtend , UserRenew , AdminRenew.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. Required. Representing the type of the operation on the role assignment. The possible values are: AdminAdd , UserAdd , AdminUpdate , AdminRemove , UserRemove , UserExtend , AdminExtend , UserRenew , AdminRenew.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

