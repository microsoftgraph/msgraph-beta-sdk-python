from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import directory_object, group, privileged_access_group_eligibility_schedule, privileged_access_group_relationships, privileged_access_schedule_request

from . import privileged_access_schedule_request

@dataclass
class PrivilegedAccessGroupEligibilityScheduleRequest(privileged_access_schedule_request.PrivilegedAccessScheduleRequest):
    odata_type = "#microsoft.graph.privilegedAccessGroupEligibilityScheduleRequest"
    # The identifier of membership or ownership eligibility relationship to the group. Required. The possible values are: owner, member, unknownFutureValue.
    access_id: Optional[privileged_access_group_relationships.PrivilegedAccessGroupRelationships] = None
    # References the group that is the scope of the membership or ownership eligibility request through PIM for groups. Supports $expand.
    group: Optional[group.Group] = None
    # The identifier of the group representing the scope of the membership and ownership eligibility through PIM for groups. Required.
    group_id: Optional[str] = None
    # References the principal that's in the scope of the membership or ownership eligibility request through the group that's governed by PIM. Supports $expand.
    principal: Optional[directory_object.DirectoryObject] = None
    # The identifier of the principal whose membership or ownership eligibility to the group is managed through PIM for groups. Required.
    principal_id: Optional[str] = None
    # Schedule created by this request.
    target_schedule: Optional[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule] = None
    # The identifier of the schedule that's created from the eligibility request. Optional.
    target_schedule_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccessGroupEligibilityScheduleRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessGroupEligibilityScheduleRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedAccessGroupEligibilityScheduleRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import directory_object, group, privileged_access_group_eligibility_schedule, privileged_access_group_relationships, privileged_access_schedule_request

        fields: Dict[str, Callable[[Any], None]] = {
            "accessId": lambda n : setattr(self, 'access_id', n.get_enum_value(privileged_access_group_relationships.PrivilegedAccessGroupRelationships)),
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
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalId", self.principal_id)
        writer.write_object_value("targetSchedule", self.target_schedule)
        writer.write_str_value("targetScheduleId", self.target_schedule_id)
    

