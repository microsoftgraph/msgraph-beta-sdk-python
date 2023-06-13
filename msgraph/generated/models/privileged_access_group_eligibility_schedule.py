from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import directory_object, group, privileged_access_group_member_type, privileged_access_group_relationships, privileged_access_schedule

from . import privileged_access_schedule

@dataclass
class PrivilegedAccessGroupEligibilitySchedule(privileged_access_schedule.PrivilegedAccessSchedule):
    odata_type = "#microsoft.graph.privilegedAccessGroupEligibilitySchedule"
    # The identifier of the membership or ownership eligibility to the group that is governed by PIM. Required. The possible values are: owner, member.
    access_id: Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships] = None
    # References the group that is the scope of the membership or ownership eligibility through PIM for groups. Supports $expand.
    group: Optional[group.Group] = None
    # The identifier of the group representing the scope of the membership or ownership eligibility through PIM for groups. Required.
    group_id: Optional[str] = None
    # Indicates whether the assignment is derived from a group assignment. It can further imply whether the caller can manage the schedule. Required. The possible values are: direct, group, unknownFutureValue.
    member_type: Optional[privileged_access_group_member_type.PrivilegedAccessGroupMemberType] = None
    # References the principal that's in the scope of this membership or ownership eligibility request to the group that's governed by PIM. Supports $expand.
    principal: Optional[directory_object.DirectoryObject] = None
    # The identifier of the principal whose membership or ownership eligibility is granted through PIM for groups. Required.
    principal_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccessGroupEligibilitySchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessGroupEligibilitySchedule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedAccessGroupEligibilitySchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import directory_object, group, privileged_access_group_member_type, privileged_access_group_relationships, privileged_access_schedule

        fields: Dict[str, Callable[[Any], None]] = {
            "accessId": lambda n : setattr(self, 'access_id', n.get_enum_value(privileged_access_group_relationships.PrivilegedAccessGroupRelationships)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("accessId", self.access_id)
        writer.write_object_value("group", self.group)
        writer.write_str_value("groupId", self.group_id)
        writer.write_enum_value("memberType", self.member_type)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalId", self.principal_id)
    

