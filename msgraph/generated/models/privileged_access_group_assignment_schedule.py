from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import directory_object, group, privileged_access_group_assignment_type, privileged_access_group_eligibility_schedule, privileged_access_group_member_type, privileged_access_group_relationships, privileged_access_schedule

from . import privileged_access_schedule

class PrivilegedAccessGroupAssignmentSchedule(privileged_access_schedule.PrivilegedAccessSchedule):
    def __init__(self,) -> None:
        """
        Instantiates a new PrivilegedAccessGroupAssignmentSchedule and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.privilegedAccessGroupAssignmentSchedule"
        # The accessId property
        self._access_id: Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships] = None
        # The activatedUsing property
        self._activated_using: Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule] = None
        # The assignmentType property
        self._assignment_type: Optional[privileged_access_group_assignment_type.PrivilegedAccessGroupAssignmentType] = None
        # The group property
        self._group: Optional[group.Group] = None
        # The groupId property
        self._group_id: Optional[str] = None
        # The memberType property
        self._member_type: Optional[privileged_access_group_member_type.PrivilegedAccessGroupMemberType] = None
        # The principal property
        self._principal: Optional[directory_object.DirectoryObject] = None
        # The principalId property
        self._principal_id: Optional[str] = None
    
    @property
    def access_id(self,) -> Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships]:
        """
        Gets the accessId property value. The accessId property
        Returns: Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships]
        """
        return self._access_id
    
    @access_id.setter
    def access_id(self,value: Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships] = None) -> None:
        """
        Sets the accessId property value. The accessId property
        Args:
            value: Value to set for the access_id property.
        """
        self._access_id = value
    
    @property
    def activated_using(self,) -> Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule]:
        """
        Gets the activatedUsing property value. The activatedUsing property
        Returns: Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule]
        """
        return self._activated_using
    
    @activated_using.setter
    def activated_using(self,value: Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule] = None) -> None:
        """
        Sets the activatedUsing property value. The activatedUsing property
        Args:
            value: Value to set for the activated_using property.
        """
        self._activated_using = value
    
    @property
    def assignment_type(self,) -> Optional[privileged_access_group_assignment_type.PrivilegedAccessGroupAssignmentType]:
        """
        Gets the assignmentType property value. The assignmentType property
        Returns: Optional[privileged_access_group_assignment_type.PrivilegedAccessGroupAssignmentType]
        """
        return self._assignment_type
    
    @assignment_type.setter
    def assignment_type(self,value: Optional[privileged_access_group_assignment_type.PrivilegedAccessGroupAssignmentType] = None) -> None:
        """
        Sets the assignmentType property value. The assignmentType property
        Args:
            value: Value to set for the assignment_type property.
        """
        self._assignment_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccessGroupAssignmentSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessGroupAssignmentSchedule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedAccessGroupAssignmentSchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import directory_object, group, privileged_access_group_assignment_type, privileged_access_group_eligibility_schedule, privileged_access_group_member_type, privileged_access_group_relationships, privileged_access_schedule

        fields: Dict[str, Callable[[Any], None]] = {
            "accessId": lambda n : setattr(self, 'access_id', n.get_enum_value(privileged_access_group_relationships.PrivilegedAccessGroupRelationships)),
            "activatedUsing": lambda n : setattr(self, 'activated_using', n.get_object_value(privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule)),
            "assignmentType": lambda n : setattr(self, 'assignment_type', n.get_enum_value(privileged_access_group_assignment_type.PrivilegedAccessGroupAssignmentType)),
            "group": lambda n : setattr(self, 'group', n.get_object_value(group.Group)),
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "memberType": lambda n : setattr(self, 'member_type', n.get_enum_value(privileged_access_group_member_type.PrivilegedAccessGroupMemberType)),
            "principal": lambda n : setattr(self, 'principal', n.get_object_value(directory_object.DirectoryObject)),
            "principalId": lambda n : setattr(self, 'principal_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group(self,) -> Optional[group.Group]:
        """
        Gets the group property value. The group property
        Returns: Optional[group.Group]
        """
        return self._group
    
    @group.setter
    def group(self,value: Optional[group.Group] = None) -> None:
        """
        Sets the group property value. The group property
        Args:
            value: Value to set for the group property.
        """
        self._group = value
    
    @property
    def group_id(self,) -> Optional[str]:
        """
        Gets the groupId property value. The groupId property
        Returns: Optional[str]
        """
        return self._group_id
    
    @group_id.setter
    def group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the groupId property value. The groupId property
        Args:
            value: Value to set for the group_id property.
        """
        self._group_id = value
    
    @property
    def member_type(self,) -> Optional[privileged_access_group_member_type.PrivilegedAccessGroupMemberType]:
        """
        Gets the memberType property value. The memberType property
        Returns: Optional[privileged_access_group_member_type.PrivilegedAccessGroupMemberType]
        """
        return self._member_type
    
    @member_type.setter
    def member_type(self,value: Optional[privileged_access_group_member_type.PrivilegedAccessGroupMemberType] = None) -> None:
        """
        Sets the memberType property value. The memberType property
        Args:
            value: Value to set for the member_type property.
        """
        self._member_type = value
    
    @property
    def principal(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the principal property value. The principal property
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._principal
    
    @principal.setter
    def principal(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the principal property value. The principal property
        Args:
            value: Value to set for the principal property.
        """
        self._principal = value
    
    @property
    def principal_id(self,) -> Optional[str]:
        """
        Gets the principalId property value. The principalId property
        Returns: Optional[str]
        """
        return self._principal_id
    
    @principal_id.setter
    def principal_id(self,value: Optional[str] = None) -> None:
        """
        Sets the principalId property value. The principalId property
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
        writer.write_enum_value("assignmentType", self.assignment_type)
        writer.write_object_value("group", self.group)
        writer.write_str_value("groupId", self.group_id)
        writer.write_enum_value("memberType", self.member_type)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalId", self.principal_id)
    

