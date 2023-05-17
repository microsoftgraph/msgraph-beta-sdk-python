from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import directory_object, group, privileged_access_group_eligibility_schedule, privileged_access_group_relationships, privileged_access_schedule_request

from . import privileged_access_schedule_request

class PrivilegedAccessGroupAssignmentScheduleRequest(privileged_access_schedule_request.PrivilegedAccessScheduleRequest):
    def __init__(self,) -> None:
        """
        Instantiates a new PrivilegedAccessGroupAssignmentScheduleRequest and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.privilegedAccessGroupAssignmentScheduleRequest"
        # The identifier of a membership or ownership assignment relationship to the group. Required. The possible values are: owner, member, unknownFutureValue.
        self._access_id: Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships] = None
        # When the request activates a membership or ownership assignment in PIM for groups, this object represents the eligibility policy for the group. Otherwise, it is null. Supports $expand.
        self._activated_using: Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule] = None
        # References the group that is the scope of the membership or ownership assignment request through PIM for groups. Supports $expand.
        self._group: Optional[group.Group] = None
        # The identifier of the group representing the scope of the membership or ownership assignment through PIM for groups. Required.
        self._group_id: Optional[str] = None
        # References the principal that's in the scope of this membership or ownership assignment request through the group that's governed by PIM. Supports $expand.
        self._principal: Optional[directory_object.DirectoryObject] = None
        # The identifier of the principal whose membership or ownership assignment to the group is managed through PIM for groups. Supports $filter (eq, ne).
        self._principal_id: Optional[str] = None
        # Schedule created by this request. Supports $expand.
        self._target_schedule: Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule] = None
        # The identifier of the schedule that's created from the membership or ownership assignment request. Supports $filter (eq, ne).
        self._target_schedule_id: Optional[str] = None
    
    @property
    def access_id(self,) -> Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships]:
        """
        Gets the accessId property value. The identifier of a membership or ownership assignment relationship to the group. Required. The possible values are: owner, member, unknownFutureValue.
        Returns: Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships]
        """
        return self._access_id
    
    @access_id.setter
    def access_id(self,value: Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships] = None) -> None:
        """
        Sets the accessId property value. The identifier of a membership or ownership assignment relationship to the group. Required. The possible values are: owner, member, unknownFutureValue.
        Args:
            value: Value to set for the access_id property.
        """
        self._access_id = value
    
    @property
    def activated_using(self,) -> Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule]:
        """
        Gets the activatedUsing property value. When the request activates a membership or ownership assignment in PIM for groups, this object represents the eligibility policy for the group. Otherwise, it is null. Supports $expand.
        Returns: Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule]
        """
        return self._activated_using
    
    @activated_using.setter
    def activated_using(self,value: Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule] = None) -> None:
        """
        Sets the activatedUsing property value. When the request activates a membership or ownership assignment in PIM for groups, this object represents the eligibility policy for the group. Otherwise, it is null. Supports $expand.
        Args:
            value: Value to set for the activated_using property.
        """
        self._activated_using = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccessGroupAssignmentScheduleRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessGroupAssignmentScheduleRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedAccessGroupAssignmentScheduleRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import directory_object, group, privileged_access_group_eligibility_schedule, privileged_access_group_relationships, privileged_access_schedule_request

        fields: Dict[str, Callable[[Any], None]] = {
            "accessId": lambda n : setattr(self, 'access_id', n.get_enum_value(privileged_access_group_relationships.PrivilegedAccessGroupRelationships)),
            "activatedUsing": lambda n : setattr(self, 'activated_using', n.get_object_value(privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule)),
            "group": lambda n : setattr(self, 'group', n.get_object_value(group.Group)),
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "principal": lambda n : setattr(self, 'principal', n.get_object_value(directory_object.DirectoryObject)),
            "principalId": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "targetSchedule": lambda n : setattr(self, 'target_schedule', n.get_object_value(privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule)),
            "targetScheduleId": lambda n : setattr(self, 'target_schedule_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group(self,) -> Optional[group.Group]:
        """
        Gets the group property value. References the group that is the scope of the membership or ownership assignment request through PIM for groups. Supports $expand.
        Returns: Optional[group.Group]
        """
        return self._group
    
    @group.setter
    def group(self,value: Optional[group.Group] = None) -> None:
        """
        Sets the group property value. References the group that is the scope of the membership or ownership assignment request through PIM for groups. Supports $expand.
        Args:
            value: Value to set for the group property.
        """
        self._group = value
    
    @property
    def group_id(self,) -> Optional[str]:
        """
        Gets the groupId property value. The identifier of the group representing the scope of the membership or ownership assignment through PIM for groups. Required.
        Returns: Optional[str]
        """
        return self._group_id
    
    @group_id.setter
    def group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the groupId property value. The identifier of the group representing the scope of the membership or ownership assignment through PIM for groups. Required.
        Args:
            value: Value to set for the group_id property.
        """
        self._group_id = value
    
    @property
    def principal(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the principal property value. References the principal that's in the scope of this membership or ownership assignment request through the group that's governed by PIM. Supports $expand.
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._principal
    
    @principal.setter
    def principal(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the principal property value. References the principal that's in the scope of this membership or ownership assignment request through the group that's governed by PIM. Supports $expand.
        Args:
            value: Value to set for the principal property.
        """
        self._principal = value
    
    @property
    def principal_id(self,) -> Optional[str]:
        """
        Gets the principalId property value. The identifier of the principal whose membership or ownership assignment to the group is managed through PIM for groups. Supports $filter (eq, ne).
        Returns: Optional[str]
        """
        return self._principal_id
    
    @principal_id.setter
    def principal_id(self,value: Optional[str] = None) -> None:
        """
        Sets the principalId property value. The identifier of the principal whose membership or ownership assignment to the group is managed through PIM for groups. Supports $filter (eq, ne).
        Args:
            value: Value to set for the principal_id property.
        """
        self._principal_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("accessId", self.access_id)
        writer.write_object_value("activatedUsing", self.activated_using)
        writer.write_object_value("group", self.group)
        writer.write_str_value("groupId", self.group_id)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalId", self.principal_id)
        writer.write_object_value("targetSchedule", self.target_schedule)
        writer.write_str_value("targetScheduleId", self.target_schedule_id)
    
    @property
    def target_schedule(self,) -> Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule]:
        """
        Gets the targetSchedule property value. Schedule created by this request. Supports $expand.
        Returns: Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule]
        """
        return self._target_schedule
    
    @target_schedule.setter
    def target_schedule(self,value: Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule] = None) -> None:
        """
        Sets the targetSchedule property value. Schedule created by this request. Supports $expand.
        Args:
            value: Value to set for the target_schedule property.
        """
        self._target_schedule = value
    
    @property
    def target_schedule_id(self,) -> Optional[str]:
        """
        Gets the targetScheduleId property value. The identifier of the schedule that's created from the membership or ownership assignment request. Supports $filter (eq, ne).
        Returns: Optional[str]
        """
        return self._target_schedule_id
    
    @target_schedule_id.setter
    def target_schedule_id(self,value: Optional[str] = None) -> None:
        """
        Sets the targetScheduleId property value. The identifier of the schedule that's created from the membership or ownership assignment request. Supports $filter (eq, ne).
        Args:
            value: Value to set for the target_schedule_id property.
        """
        self._target_schedule_id = value
    

