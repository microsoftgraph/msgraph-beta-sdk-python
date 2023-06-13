from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import approval, entity, privileged_access_group_assignment_schedule, privileged_access_group_assignment_schedule_instance, privileged_access_group_assignment_schedule_request, privileged_access_group_eligibility_schedule, privileged_access_group_eligibility_schedule_instance, privileged_access_group_eligibility_schedule_request

from . import entity

@dataclass
class PrivilegedAccessGroup(entity.Entity):
    # The assignmentApprovals property
    assignment_approvals: Optional[List[approval.Approval]] = None
    # The instances of assignment schedules to activate a just-in-time access.
    assignment_schedule_instances: Optional[List[privileged_access_group_assignment_schedule_instance.PrivilegedAccessGroupAssignmentScheduleInstance]] = None
    # The schedule requests for operations to create, update, delete, extend, and renew an assignment.
    assignment_schedule_requests: Optional[List[privileged_access_group_assignment_schedule_request.PrivilegedAccessGroupAssignmentScheduleRequest]] = None
    # The assignment schedules to activate a just-in-time access.
    assignment_schedules: Optional[List[privileged_access_group_assignment_schedule.PrivilegedAccessGroupAssignmentSchedule]] = None
    # The instances of eligibility schedules to activate a just-in-time access.
    eligibility_schedule_instances: Optional[List[privileged_access_group_eligibility_schedule_instance.PrivilegedAccessGroupEligibilityScheduleInstance]] = None
    # The schedule requests for operations to create, update, delete, extend, and renew an eligibility.
    eligibility_schedule_requests: Optional[List[privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest]] = None
    # The eligibility schedules to activate a just-in-time access.
    eligibility_schedules: Optional[List[privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccessGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedAccessGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import approval, entity, privileged_access_group_assignment_schedule, privileged_access_group_assignment_schedule_instance, privileged_access_group_assignment_schedule_request, privileged_access_group_eligibility_schedule, privileged_access_group_eligibility_schedule_instance, privileged_access_group_eligibility_schedule_request

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentApprovals": lambda n : setattr(self, 'assignment_approvals', n.get_collection_of_object_values(approval.Approval)),
            "assignmentSchedules": lambda n : setattr(self, 'assignment_schedules', n.get_collection_of_object_values(privileged_access_group_assignment_schedule.PrivilegedAccessGroupAssignmentSchedule)),
            "assignmentScheduleInstances": lambda n : setattr(self, 'assignment_schedule_instances', n.get_collection_of_object_values(privileged_access_group_assignment_schedule_instance.PrivilegedAccessGroupAssignmentScheduleInstance)),
            "assignmentScheduleRequests": lambda n : setattr(self, 'assignment_schedule_requests', n.get_collection_of_object_values(privileged_access_group_assignment_schedule_request.PrivilegedAccessGroupAssignmentScheduleRequest)),
            "eligibilitySchedules": lambda n : setattr(self, 'eligibility_schedules', n.get_collection_of_object_values(privileged_access_group_eligibility_schedule.PrivilegedAccessGroupEligibilitySchedule)),
            "eligibilityScheduleInstances": lambda n : setattr(self, 'eligibility_schedule_instances', n.get_collection_of_object_values(privileged_access_group_eligibility_schedule_instance.PrivilegedAccessGroupEligibilityScheduleInstance)),
            "eligibilityScheduleRequests": lambda n : setattr(self, 'eligibility_schedule_requests', n.get_collection_of_object_values(privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest)),
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
        writer.write_collection_of_object_values("assignmentApprovals", self.assignment_approvals)
        writer.write_collection_of_object_values("assignmentSchedules", self.assignment_schedules)
        writer.write_collection_of_object_values("assignmentScheduleInstances", self.assignment_schedule_instances)
        writer.write_collection_of_object_values("assignmentScheduleRequests", self.assignment_schedule_requests)
        writer.write_collection_of_object_values("eligibilitySchedules", self.eligibility_schedules)
        writer.write_collection_of_object_values("eligibilityScheduleInstances", self.eligibility_schedule_instances)
        writer.write_collection_of_object_values("eligibilityScheduleRequests", self.eligibility_schedule_requests)
    

