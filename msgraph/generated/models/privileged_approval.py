from __future__ import annotations
from datetime import datetime, timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

approval_state = lazy_import('msgraph.generated.models.approval_state')
entity = lazy_import('msgraph.generated.models.entity')
privileged_role = lazy_import('msgraph.generated.models.privileged_role')
privileged_role_assignment_request = lazy_import('msgraph.generated.models.privileged_role_assignment_request')

class PrivilegedApproval(entity.Entity):
    @property
    def approval_duration(self,) -> Optional[Timedelta]:
        """
        Gets the approvalDuration property value. The approvalDuration property
        Returns: Optional[Timedelta]
        """
        return self._approval_duration
    
    @approval_duration.setter
    def approval_duration(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the approvalDuration property value. The approvalDuration property
        Args:
            value: Value to set for the approvalDuration property.
        """
        self._approval_duration = value
    
    @property
    def approval_state(self,) -> Optional[approval_state.ApprovalState]:
        """
        Gets the approvalState property value. Possible values are: pending, approved, denied, aborted, canceled.
        Returns: Optional[approval_state.ApprovalState]
        """
        return self._approval_state
    
    @approval_state.setter
    def approval_state(self,value: Optional[approval_state.ApprovalState] = None) -> None:
        """
        Sets the approvalState property value. Possible values are: pending, approved, denied, aborted, canceled.
        Args:
            value: Value to set for the approvalState property.
        """
        self._approval_state = value
    
    @property
    def approval_type(self,) -> Optional[str]:
        """
        Gets the approvalType property value. The approvalType property
        Returns: Optional[str]
        """
        return self._approval_type
    
    @approval_type.setter
    def approval_type(self,value: Optional[str] = None) -> None:
        """
        Sets the approvalType property value. The approvalType property
        Args:
            value: Value to set for the approvalType property.
        """
        self._approval_type = value
    
    @property
    def approver_reason(self,) -> Optional[str]:
        """
        Gets the approverReason property value. The approverReason property
        Returns: Optional[str]
        """
        return self._approver_reason
    
    @approver_reason.setter
    def approver_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the approverReason property value. The approverReason property
        Args:
            value: Value to set for the approverReason property.
        """
        self._approver_reason = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new PrivilegedApproval and sets the default values.
        """
        super().__init__()
        # The approvalDuration property
        self._approval_duration: Optional[Timedelta] = None
        # Possible values are: pending, approved, denied, aborted, canceled.
        self._approval_state: Optional[approval_state.ApprovalState] = None
        # The approvalType property
        self._approval_type: Optional[str] = None
        # The approverReason property
        self._approver_reason: Optional[str] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._end_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Read-only. The role assignment request for this approval object
        self._request: Optional[privileged_role_assignment_request.PrivilegedRoleAssignmentRequest] = None
        # The requestorReason property
        self._requestor_reason: Optional[str] = None
        # The roleId property
        self._role_id: Optional[str] = None
        # The roleInfo property
        self._role_info: Optional[privileged_role.PrivilegedRole] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._start_date_time: Optional[datetime] = None
        # The userId property
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedApproval:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedApproval
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedApproval()
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "approval_duration": lambda n : setattr(self, 'approval_duration', n.get_object_value(Timedelta)),
            "approval_state": lambda n : setattr(self, 'approval_state', n.get_enum_value(approval_state.ApprovalState)),
            "approval_type": lambda n : setattr(self, 'approval_type', n.get_str_value()),
            "approver_reason": lambda n : setattr(self, 'approver_reason', n.get_str_value()),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "request": lambda n : setattr(self, 'request', n.get_object_value(privileged_role_assignment_request.PrivilegedRoleAssignmentRequest)),
            "requestor_reason": lambda n : setattr(self, 'requestor_reason', n.get_str_value()),
            "role_id": lambda n : setattr(self, 'role_id', n.get_str_value()),
            "role_info": lambda n : setattr(self, 'role_info', n.get_object_value(privileged_role.PrivilegedRole)),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def request(self,) -> Optional[privileged_role_assignment_request.PrivilegedRoleAssignmentRequest]:
        """
        Gets the request property value. Read-only. The role assignment request for this approval object
        Returns: Optional[privileged_role_assignment_request.PrivilegedRoleAssignmentRequest]
        """
        return self._request
    
    @request.setter
    def request(self,value: Optional[privileged_role_assignment_request.PrivilegedRoleAssignmentRequest] = None) -> None:
        """
        Sets the request property value. Read-only. The role assignment request for this approval object
        Args:
            value: Value to set for the request property.
        """
        self._request = value
    
    @property
    def requestor_reason(self,) -> Optional[str]:
        """
        Gets the requestorReason property value. The requestorReason property
        Returns: Optional[str]
        """
        return self._requestor_reason
    
    @requestor_reason.setter
    def requestor_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the requestorReason property value. The requestorReason property
        Args:
            value: Value to set for the requestorReason property.
        """
        self._requestor_reason = value
    
    @property
    def role_id(self,) -> Optional[str]:
        """
        Gets the roleId property value. The roleId property
        Returns: Optional[str]
        """
        return self._role_id
    
    @role_id.setter
    def role_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleId property value. The roleId property
        Args:
            value: Value to set for the roleId property.
        """
        self._role_id = value
    
    @property
    def role_info(self,) -> Optional[privileged_role.PrivilegedRole]:
        """
        Gets the roleInfo property value. The roleInfo property
        Returns: Optional[privileged_role.PrivilegedRole]
        """
        return self._role_info
    
    @role_info.setter
    def role_info(self,value: Optional[privileged_role.PrivilegedRole] = None) -> None:
        """
        Sets the roleInfo property value. The roleInfo property
        Args:
            value: Value to set for the roleInfo property.
        """
        self._role_info = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("approvalDuration", self.approval_duration)
        writer.write_enum_value("approvalState", self.approval_state)
        writer.write_str_value("approvalType", self.approval_type)
        writer.write_str_value("approverReason", self.approver_reason)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_object_value("request", self.request)
        writer.write_str_value("requestorReason", self.requestor_reason)
        writer.write_str_value("roleId", self.role_id)
        writer.write_object_value("roleInfo", self.role_info)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("userId", self.user_id)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The userId property
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The userId property
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    

