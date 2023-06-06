from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, privileged_access_group_assignment_schedule, privileged_access_group_eligibility_schedule, request_schedule

from . import entity

@dataclass
class PrivilegedAccessSchedule(entity.Entity):
    # When the schedule was created. Optional.
    created_date_time: Optional[datetime] = None
    # The identifier of the access assignment or eligibility request that created this schedule. Optional.
    created_using: Optional[str] = None
    # When the schedule was last modified. Optional.
    modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the period of the access assignment or eligibility. The scheduleInfo can represent a single occurrence or multiple recurring instances. Required.
    schedule_info: Optional[request_schedule.RequestSchedule] = None
    # The status of the access assignment or eligibility request. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable. Optional.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccessSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessSchedule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.privilegedAccessGroupAssignmentSchedule":
                from . import privileged_access_group_assignment_schedule

                return privileged_access_group_assignment_schedule.PrivilegedAccessGroupAssignmentSchedule()
            if mapping_value == "#microsoft.graph.privilegedAccessGroupEligibilitySchedule":
                from . import privileged_access_group_eligibility_schedule

                return privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule()
        return PrivilegedAccessSchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, privileged_access_group_assignment_schedule, privileged_access_group_eligibility_schedule, request_schedule

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "createdUsing": lambda n : setattr(self, 'created_using', n.get_str_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "scheduleInfo": lambda n : setattr(self, 'schedule_info', n.get_object_value(request_schedule.RequestSchedule)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("createdUsing", self.created_using)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_object_value("scheduleInfo", self.schedule_info)
        writer.write_str_value("status", self.status)
    

