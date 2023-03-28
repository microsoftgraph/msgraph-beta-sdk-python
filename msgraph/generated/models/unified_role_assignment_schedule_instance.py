from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_eligibility_schedule_instance, unified_role_schedule_instance_base

from . import unified_role_schedule_instance_base

class UnifiedRoleAssignmentScheduleInstance(unified_role_schedule_instance_base.UnifiedRoleScheduleInstanceBase):
    def __init__(self,) -> None:
        """
        Instantiates a new UnifiedRoleAssignmentScheduleInstance and sets the default values.
        """
        super().__init__()
        # If the request is from an eligible administrator to activate a role, this parameter will show the related eligible assignment for that activation. Otherwise, it is null. Supports $expand.
        self._activated_using: Optional[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance] = None
        # Type of the assignment which can either be Assigned or Activated. Supports $filter (eq, ne).
        self._assignment_type: Optional[str] = None
        # The end date of the schedule instance.
        self._end_date_time: Optional[datetime] = None
        # How the assignments is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleAssignmentSchedule can be managed by the caller. Supports $filter (eq, ne).
        self._member_type: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The identifier of the role assignment in Azure AD.
        self._role_assignment_origin_id: Optional[str] = None
        # The identifier of the unifiedRoleAssignmentSchedule object from which this instance was created.
        self._role_assignment_schedule_id: Optional[str] = None
        # When this instance starts.
        self._start_date_time: Optional[datetime] = None
    
    @property
    def activated_using(self,) -> Optional[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]:
        """
        Gets the activatedUsing property value. If the request is from an eligible administrator to activate a role, this parameter will show the related eligible assignment for that activation. Otherwise, it is null. Supports $expand.
        Returns: Optional[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]
        """
        return self._activated_using
    
    @activated_using.setter
    def activated_using(self,value: Optional[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance] = None) -> None:
        """
        Sets the activatedUsing property value. If the request is from an eligible administrator to activate a role, this parameter will show the related eligible assignment for that activation. Otherwise, it is null. Supports $expand.
        Args:
            value: Value to set for the activated_using property.
        """
        self._activated_using = value
    
    @property
    def assignment_type(self,) -> Optional[str]:
        """
        Gets the assignmentType property value. Type of the assignment which can either be Assigned or Activated. Supports $filter (eq, ne).
        Returns: Optional[str]
        """
        return self._assignment_type
    
    @assignment_type.setter
    def assignment_type(self,value: Optional[str] = None) -> None:
        """
        Sets the assignmentType property value. Type of the assignment which can either be Assigned or Activated. Supports $filter (eq, ne).
        Args:
            value: Value to set for the assignment_type property.
        """
        self._assignment_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleAssignmentScheduleInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleAssignmentScheduleInstance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleAssignmentScheduleInstance()
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The end date of the schedule instance.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The end date of the schedule instance.
        Args:
            value: Value to set for the end_date_time property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import unified_role_eligibility_schedule_instance, unified_role_schedule_instance_base

        fields: Dict[str, Callable[[Any], None]] = {
            "activatedUsing": lambda n : setattr(self, 'activated_using', n.get_object_value(unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance)),
            "assignmentType": lambda n : setattr(self, 'assignment_type', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "memberType": lambda n : setattr(self, 'member_type', n.get_str_value()),
            "roleAssignmentOriginId": lambda n : setattr(self, 'role_assignment_origin_id', n.get_str_value()),
            "roleAssignmentScheduleId": lambda n : setattr(self, 'role_assignment_schedule_id', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def member_type(self,) -> Optional[str]:
        """
        Gets the memberType property value. How the assignments is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleAssignmentSchedule can be managed by the caller. Supports $filter (eq, ne).
        Returns: Optional[str]
        """
        return self._member_type
    
    @member_type.setter
    def member_type(self,value: Optional[str] = None) -> None:
        """
        Sets the memberType property value. How the assignments is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleAssignmentSchedule can be managed by the caller. Supports $filter (eq, ne).
        Args:
            value: Value to set for the member_type property.
        """
        self._member_type = value
    
    @property
    def role_assignment_origin_id(self,) -> Optional[str]:
        """
        Gets the roleAssignmentOriginId property value. The identifier of the role assignment in Azure AD.
        Returns: Optional[str]
        """
        return self._role_assignment_origin_id
    
    @role_assignment_origin_id.setter
    def role_assignment_origin_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleAssignmentOriginId property value. The identifier of the role assignment in Azure AD.
        Args:
            value: Value to set for the role_assignment_origin_id property.
        """
        self._role_assignment_origin_id = value
    
    @property
    def role_assignment_schedule_id(self,) -> Optional[str]:
        """
        Gets the roleAssignmentScheduleId property value. The identifier of the unifiedRoleAssignmentSchedule object from which this instance was created.
        Returns: Optional[str]
        """
        return self._role_assignment_schedule_id
    
    @role_assignment_schedule_id.setter
    def role_assignment_schedule_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleAssignmentScheduleId property value. The identifier of the unifiedRoleAssignmentSchedule object from which this instance was created.
        Args:
            value: Value to set for the role_assignment_schedule_id property.
        """
        self._role_assignment_schedule_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("activatedUsing", self.activated_using)
        writer.write_str_value("assignmentType", self.assignment_type)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("memberType", self.member_type)
        writer.write_str_value("roleAssignmentOriginId", self.role_assignment_origin_id)
        writer.write_str_value("roleAssignmentScheduleId", self.role_assignment_schedule_id)
        writer.write_datetime_value("startDateTime", self.start_date_time)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. When this instance starts.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. When this instance starts.
        Args:
            value: Value to set for the start_date_time property.
        """
        self._start_date_time = value
    

