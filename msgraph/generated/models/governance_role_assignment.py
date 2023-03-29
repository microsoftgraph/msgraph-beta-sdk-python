from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, governance_resource, governance_role_definition, governance_subject

from . import entity

class GovernanceRoleAssignment(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new governanceRoleAssignment and sets the default values.
        """
        super().__init__()
        # The state of the assignment. The value can be Eligible for eligible assignment or Active if it is directly assigned Active by administrators, or activated on an eligible assignment by the users.
        self._assignment_state: Optional[str] = None
        # For a non-permanent role assignment, this is the time when the role assignment will be expired. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._end_date_time: Optional[datetime] = None
        # The external ID the resource that is used to identify the role assignment in the provider.
        self._external_id: Optional[str] = None
        # Read-only. If this is an active assignment and created due to activation on an eligible assignment, it represents the object of that eligible assignment; Otherwise, the value is null.
        self._linked_eligible_role_assignment: Optional[GovernanceRoleAssignment] = None
        # If this is an active assignment and created due to activation on an eligible assignment, it represents the ID of that eligible assignment; Otherwise, the value is null.
        self._linked_eligible_role_assignment_id: Optional[str] = None
        # The type of member. The value can be: Inherited (if the role assignment is inherited from a parent resource scope), Group (if the role assignment is not inherited, but comes from the membership of a group assignment), or User (if the role assignment is neither inherited nor from a group assignment).
        self._member_type: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Read-only. The resource associated with the role assignment.
        self._resource: Optional[governance_resource.GovernanceResource] = None
        # Required. The ID of the resource which the role assignment is associated with.
        self._resource_id: Optional[str] = None
        # Read-only. The role definition associated with the role assignment.
        self._role_definition: Optional[governance_role_definition.GovernanceRoleDefinition] = None
        # Required. The ID of the role definition which the role assignment is associated with.
        self._role_definition_id: Optional[str] = None
        # The start time of the role assignment. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._start_date_time: Optional[datetime] = None
        # The status property
        self._status: Optional[str] = None
        # Read-only. The subject associated with the role assignment.
        self._subject: Optional[governance_subject.GovernanceSubject] = None
        # Required. The ID of the subject which the role assignment is associated with.
        self._subject_id: Optional[str] = None
    
    @property
    def assignment_state(self,) -> Optional[str]:
        """
        Gets the assignmentState property value. The state of the assignment. The value can be Eligible for eligible assignment or Active if it is directly assigned Active by administrators, or activated on an eligible assignment by the users.
        Returns: Optional[str]
        """
        return self._assignment_state
    
    @assignment_state.setter
    def assignment_state(self,value: Optional[str] = None) -> None:
        """
        Sets the assignmentState property value. The state of the assignment. The value can be Eligible for eligible assignment or Active if it is directly assigned Active by administrators, or activated on an eligible assignment by the users.
        Args:
            value: Value to set for the assignment_state property.
        """
        self._assignment_state = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GovernanceRoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceRoleAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GovernanceRoleAssignment()
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. For a non-permanent role assignment, this is the time when the role assignment will be expired. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. For a non-permanent role assignment, this is the time when the role assignment will be expired. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the end_date_time property.
        """
        self._end_date_time = value
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. The external ID the resource that is used to identify the role assignment in the provider.
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. The external ID the resource that is used to identify the role assignment in the provider.
        Args:
            value: Value to set for the external_id property.
        """
        self._external_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, governance_resource, governance_role_definition, governance_subject

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentState": lambda n : setattr(self, 'assignment_state', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "linkedEligibleRoleAssignment": lambda n : setattr(self, 'linked_eligible_role_assignment', n.get_object_value(GovernanceRoleAssignment)),
            "linkedEligibleRoleAssignmentId": lambda n : setattr(self, 'linked_eligible_role_assignment_id', n.get_str_value()),
            "memberType": lambda n : setattr(self, 'member_type', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(governance_resource.GovernanceResource)),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "roleDefinition": lambda n : setattr(self, 'role_definition', n.get_object_value(governance_role_definition.GovernanceRoleDefinition)),
            "roleDefinitionId": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_object_value(governance_subject.GovernanceSubject)),
            "subjectId": lambda n : setattr(self, 'subject_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def linked_eligible_role_assignment(self,) -> Optional[GovernanceRoleAssignment]:
        """
        Gets the linkedEligibleRoleAssignment property value. Read-only. If this is an active assignment and created due to activation on an eligible assignment, it represents the object of that eligible assignment; Otherwise, the value is null.
        Returns: Optional[GovernanceRoleAssignment]
        """
        return self._linked_eligible_role_assignment
    
    @linked_eligible_role_assignment.setter
    def linked_eligible_role_assignment(self,value: Optional[GovernanceRoleAssignment] = None) -> None:
        """
        Sets the linkedEligibleRoleAssignment property value. Read-only. If this is an active assignment and created due to activation on an eligible assignment, it represents the object of that eligible assignment; Otherwise, the value is null.
        Args:
            value: Value to set for the linked_eligible_role_assignment property.
        """
        self._linked_eligible_role_assignment = value
    
    @property
    def linked_eligible_role_assignment_id(self,) -> Optional[str]:
        """
        Gets the linkedEligibleRoleAssignmentId property value. If this is an active assignment and created due to activation on an eligible assignment, it represents the ID of that eligible assignment; Otherwise, the value is null.
        Returns: Optional[str]
        """
        return self._linked_eligible_role_assignment_id
    
    @linked_eligible_role_assignment_id.setter
    def linked_eligible_role_assignment_id(self,value: Optional[str] = None) -> None:
        """
        Sets the linkedEligibleRoleAssignmentId property value. If this is an active assignment and created due to activation on an eligible assignment, it represents the ID of that eligible assignment; Otherwise, the value is null.
        Args:
            value: Value to set for the linked_eligible_role_assignment_id property.
        """
        self._linked_eligible_role_assignment_id = value
    
    @property
    def member_type(self,) -> Optional[str]:
        """
        Gets the memberType property value. The type of member. The value can be: Inherited (if the role assignment is inherited from a parent resource scope), Group (if the role assignment is not inherited, but comes from the membership of a group assignment), or User (if the role assignment is neither inherited nor from a group assignment).
        Returns: Optional[str]
        """
        return self._member_type
    
    @member_type.setter
    def member_type(self,value: Optional[str] = None) -> None:
        """
        Sets the memberType property value. The type of member. The value can be: Inherited (if the role assignment is inherited from a parent resource scope), Group (if the role assignment is not inherited, but comes from the membership of a group assignment), or User (if the role assignment is neither inherited nor from a group assignment).
        Args:
            value: Value to set for the member_type property.
        """
        self._member_type = value
    
    @property
    def resource(self,) -> Optional[governance_resource.GovernanceResource]:
        """
        Gets the resource property value. Read-only. The resource associated with the role assignment.
        Returns: Optional[governance_resource.GovernanceResource]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[governance_resource.GovernanceResource] = None) -> None:
        """
        Sets the resource property value. Read-only. The resource associated with the role assignment.
        Args:
            value: Value to set for the resource property.
        """
        self._resource = value
    
    @property
    def resource_id(self,) -> Optional[str]:
        """
        Gets the resourceId property value. Required. The ID of the resource which the role assignment is associated with.
        Returns: Optional[str]
        """
        return self._resource_id
    
    @resource_id.setter
    def resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceId property value. Required. The ID of the resource which the role assignment is associated with.
        Args:
            value: Value to set for the resource_id property.
        """
        self._resource_id = value
    
    @property
    def role_definition(self,) -> Optional[governance_role_definition.GovernanceRoleDefinition]:
        """
        Gets the roleDefinition property value. Read-only. The role definition associated with the role assignment.
        Returns: Optional[governance_role_definition.GovernanceRoleDefinition]
        """
        return self._role_definition
    
    @role_definition.setter
    def role_definition(self,value: Optional[governance_role_definition.GovernanceRoleDefinition] = None) -> None:
        """
        Sets the roleDefinition property value. Read-only. The role definition associated with the role assignment.
        Args:
            value: Value to set for the role_definition property.
        """
        self._role_definition = value
    
    @property
    def role_definition_id(self,) -> Optional[str]:
        """
        Gets the roleDefinitionId property value. Required. The ID of the role definition which the role assignment is associated with.
        Returns: Optional[str]
        """
        return self._role_definition_id
    
    @role_definition_id.setter
    def role_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleDefinitionId property value. Required. The ID of the role definition which the role assignment is associated with.
        Args:
            value: Value to set for the role_definition_id property.
        """
        self._role_definition_id = value
    
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
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("externalId", self.external_id)
        writer.write_object_value("linkedEligibleRoleAssignment", self.linked_eligible_role_assignment)
        writer.write_str_value("linkedEligibleRoleAssignmentId", self.linked_eligible_role_assignment_id)
        writer.write_str_value("memberType", self.member_type)
        writer.write_object_value("resource", self.resource)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_object_value("roleDefinition", self.role_definition)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("status", self.status)
        writer.write_object_value("subject", self.subject)
        writer.write_str_value("subjectId", self.subject_id)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The start time of the role assignment. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The start time of the role assignment. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the start_date_time property.
        """
        self._start_date_time = value
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The status property
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def subject(self,) -> Optional[governance_subject.GovernanceSubject]:
        """
        Gets the subject property value. Read-only. The subject associated with the role assignment.
        Returns: Optional[governance_subject.GovernanceSubject]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[governance_subject.GovernanceSubject] = None) -> None:
        """
        Sets the subject property value. Read-only. The subject associated with the role assignment.
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    
    @property
    def subject_id(self,) -> Optional[str]:
        """
        Gets the subjectId property value. Required. The ID of the subject which the role assignment is associated with.
        Returns: Optional[str]
        """
        return self._subject_id
    
    @subject_id.setter
    def subject_id(self,value: Optional[str] = None) -> None:
        """
        Sets the subjectId property value. Required. The ID of the subject which the role assignment is associated with.
        Args:
            value: Value to set for the subject_id property.
        """
        self._subject_id = value
    

