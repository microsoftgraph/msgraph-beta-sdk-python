from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
governance_schedule = lazy_import('msgraph.generated.models.governance_schedule')
privileged_role = lazy_import('msgraph.generated.models.privileged_role')

class PrivilegedRoleAssignmentRequest(entity.Entity):
    @property
    def assignment_state(self,) -> Optional[str]:
        """
        Gets the assignmentState property value. The state of the assignment. The value can be Eligible for eligible assignment Active - if it is directly assigned Active by administrators, or activated on an eligible assignment by the users.
        Returns: Optional[str]
        """
        return self._assignment_state
    
    @assignment_state.setter
    def assignment_state(self,value: Optional[str] = None) -> None:
        """
        Sets the assignmentState property value. The state of the assignment. The value can be Eligible for eligible assignment Active - if it is directly assigned Active by administrators, or activated on an eligible assignment by the users.
        Args:
            value: Value to set for the assignmentState property.
        """
        self._assignment_state = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new privilegedRoleAssignmentRequest and sets the default values.
        """
        super().__init__()
        # The state of the assignment. The value can be Eligible for eligible assignment Active - if it is directly assigned Active by administrators, or activated on an eligible assignment by the users.
        self._assignment_state: Optional[str] = None
        # The duration of a role assignment.
        self._duration: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The reason for the role assignment.
        self._reason: Optional[str] = None
        # Read-only. The request create time. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._requested_date_time: Optional[datetime] = None
        # The id of the role.
        self._role_id: Optional[str] = None
        # The roleInfo object of the role assignment request.
        self._role_info: Optional[privileged_role.PrivilegedRole] = None
        # The schedule object of the role assignment request.
        self._schedule: Optional[governance_schedule.GovernanceSchedule] = None
        # Read-only.The status of the role assignment request. The value can be NotStarted,Completed,RequestedApproval,Scheduled,Approved,ApprovalDenied,ApprovalAborted,Cancelling,Cancelled,Revoked,RequestExpired.
        self._status: Optional[str] = None
        # The ticketNumber for the role assignment.
        self._ticket_number: Optional[str] = None
        # The ticketSystem for the role assignment.
        self._ticket_system: Optional[str] = None
        # Representing the type of the operation on the role assignment. The value can be AdminAdd: Administrators add users to roles;UserAdd: Users add role assignments.
        self._type: Optional[str] = None
        # The id of the user.
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedRoleAssignmentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedRoleAssignmentRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedRoleAssignmentRequest()
    
    @property
    def duration(self,) -> Optional[str]:
        """
        Gets the duration property value. The duration of a role assignment.
        Returns: Optional[str]
        """
        return self._duration
    
    @duration.setter
    def duration(self,value: Optional[str] = None) -> None:
        """
        Sets the duration property value. The duration of a role assignment.
        Args:
            value: Value to set for the duration property.
        """
        self._duration = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignment_state": lambda n : setattr(self, 'assignment_state', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "requested_date_time": lambda n : setattr(self, 'requested_date_time', n.get_datetime_value()),
            "role_id": lambda n : setattr(self, 'role_id', n.get_str_value()),
            "role_info": lambda n : setattr(self, 'role_info', n.get_object_value(privileged_role.PrivilegedRole)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(governance_schedule.GovernanceSchedule)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "ticket_number": lambda n : setattr(self, 'ticket_number', n.get_str_value()),
            "ticket_system": lambda n : setattr(self, 'ticket_system', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def reason(self,) -> Optional[str]:
        """
        Gets the reason property value. The reason for the role assignment.
        Returns: Optional[str]
        """
        return self._reason
    
    @reason.setter
    def reason(self,value: Optional[str] = None) -> None:
        """
        Sets the reason property value. The reason for the role assignment.
        Args:
            value: Value to set for the reason property.
        """
        self._reason = value
    
    @property
    def requested_date_time(self,) -> Optional[datetime]:
        """
        Gets the requestedDateTime property value. Read-only. The request create time. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._requested_date_time
    
    @requested_date_time.setter
    def requested_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the requestedDateTime property value. Read-only. The request create time. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the requestedDateTime property.
        """
        self._requested_date_time = value
    
    @property
    def role_id(self,) -> Optional[str]:
        """
        Gets the roleId property value. The id of the role.
        Returns: Optional[str]
        """
        return self._role_id
    
    @role_id.setter
    def role_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleId property value. The id of the role.
        Args:
            value: Value to set for the roleId property.
        """
        self._role_id = value
    
    @property
    def role_info(self,) -> Optional[privileged_role.PrivilegedRole]:
        """
        Gets the roleInfo property value. The roleInfo object of the role assignment request.
        Returns: Optional[privileged_role.PrivilegedRole]
        """
        return self._role_info
    
    @role_info.setter
    def role_info(self,value: Optional[privileged_role.PrivilegedRole] = None) -> None:
        """
        Sets the roleInfo property value. The roleInfo object of the role assignment request.
        Args:
            value: Value to set for the roleInfo property.
        """
        self._role_info = value
    
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
        writer.write_str_value("duration", self.duration)
        writer.write_str_value("reason", self.reason)
        writer.write_datetime_value("requestedDateTime", self.requested_date_time)
        writer.write_str_value("roleId", self.role_id)
        writer.write_object_value("roleInfo", self.role_info)
        writer.write_object_value("schedule", self.schedule)
        writer.write_str_value("status", self.status)
        writer.write_str_value("ticketNumber", self.ticket_number)
        writer.write_str_value("ticketSystem", self.ticket_system)
        writer.write_str_value("type", self.type)
        writer.write_str_value("userId", self.user_id)
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. Read-only.The status of the role assignment request. The value can be NotStarted,Completed,RequestedApproval,Scheduled,Approved,ApprovalDenied,ApprovalAborted,Cancelling,Cancelled,Revoked,RequestExpired.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. Read-only.The status of the role assignment request. The value can be NotStarted,Completed,RequestedApproval,Scheduled,Approved,ApprovalDenied,ApprovalAborted,Cancelling,Cancelled,Revoked,RequestExpired.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def ticket_number(self,) -> Optional[str]:
        """
        Gets the ticketNumber property value. The ticketNumber for the role assignment.
        Returns: Optional[str]
        """
        return self._ticket_number
    
    @ticket_number.setter
    def ticket_number(self,value: Optional[str] = None) -> None:
        """
        Sets the ticketNumber property value. The ticketNumber for the role assignment.
        Args:
            value: Value to set for the ticketNumber property.
        """
        self._ticket_number = value
    
    @property
    def ticket_system(self,) -> Optional[str]:
        """
        Gets the ticketSystem property value. The ticketSystem for the role assignment.
        Returns: Optional[str]
        """
        return self._ticket_system
    
    @ticket_system.setter
    def ticket_system(self,value: Optional[str] = None) -> None:
        """
        Sets the ticketSystem property value. The ticketSystem for the role assignment.
        Args:
            value: Value to set for the ticketSystem property.
        """
        self._ticket_system = value
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. Representing the type of the operation on the role assignment. The value can be AdminAdd: Administrators add users to roles;UserAdd: Users add role assignments.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. Representing the type of the operation on the role assignment. The value can be AdminAdd: Administrators add users to roles;UserAdd: Users add role assignments.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The id of the user.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The id of the user.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    

