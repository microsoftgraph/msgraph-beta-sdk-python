from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import directory_object, group, privileged_access_group_assignment_type, privileged_access_group_eligibility_schedule, privileged_access_group_member_type, privileged_access_group_relationships, privileged_access_schedule

from . import privileged_access_schedule

@dataclass
class PrivilegedAccessGroupAssignmentSchedule(privileged_access_schedule.PrivilegedAccessSchedule):
    odata_type = "#microsoft.graph.privilegedAccessGroupAssignmentSchedule"
    # The identifier of the membership or ownership assignment to the group that is governed by PIM. Required. The possible values are: owner, member, unknownFutureValue.
    access_id: Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships] = None
    # When the request activates an ownership or membership assignment in PIM for groups, this object represents the eligibility relationship. Otherwise, it is null. Supports $expand.
    activated_using: Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule] = None
    # Indicates whether the membership or ownership assignment for the principal is granted through activation or direct assignment. Required. The possible values are: assigned, activated, unknownFutureValue.
    assignment_type: Optional[privileged_access_group_assignment_type.PrivilegedAccessGroupAssignmentType] = None
    # References the group that is the scope of the membership or ownership assignment through PIM for groups. Supports $expand.
    group: Optional[group.Group] = None
    # The identifier of the group representing the scope of the membership or ownership assignment through PIM for groups. Required.
    group_id: Optional[str] = None
    # Indicates whether the assignment is derived from a direct group assignment or through a transitive assignment. The possible values are: direct, group, unknownFutureValue.
    member_type: Optional[privileged_access_group_member_type.PrivilegedAccessGroupMemberType] = None
    # References the principal that's in the scope of this membership or ownership assignment request to the group that's governed by PIM. Supports $expand.
    principal: Optional[directory_object.DirectoryObject] = None
    # The identifier of the principal whose membership or ownership assignment is granted through PIM for groups. Required.
    principal_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccessGroupAssignmentSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessGroupAssignmentSchedule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PrivilegedAccessGroupAssignmentSchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import directory_object, group, privileged_access_group_assignment_type, privileged_access_group_eligibility_schedule, privileged_access_group_member_type, privileged_access_group_relationships, privileged_access_schedule

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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("accessId", self.access_id)
        writer.write_object_value("activatedUsing", self.activated_using)
        writer.write_enum_value("assignmentType", self.assignment_type)
        writer.write_object_value("group", self.group)
        writer.write_str_value("groupId", self.group_id)
        writer.write_enum_value("memberType", self.member_type)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalId", self.principal_id)
    

