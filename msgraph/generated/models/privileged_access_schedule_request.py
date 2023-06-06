from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import privileged_access_group_assignment_schedule_request, privileged_access_group_eligibility_schedule_request, request, request_schedule, schedule_request_actions, ticket_info

from . import request

@dataclass
class PrivilegedAccessScheduleRequest(request.Request):
    odata_type = "#microsoft.graph.privilegedAccessScheduleRequest"
    # Represents the type of operation on the group membership or ownership assignment request. The possible values are: adminAssign, adminUpdate, adminRemove, selfActivate, selfDeactivate, adminExtend, adminRenew. adminAssign: For administrators to assign group membership or ownership to principals.adminRemove: For administrators to remove principals from group membership or ownership. adminUpdate: For administrators to change existing group membership or ownership assignments.adminExtend: For administrators to extend expiring assignments.adminRenew: For administrators to renew expired assignments.selfActivate: For principals to activate their assignments.selfDeactivate: For principals to deactivate their active assignments.
    action: Optional[schedule_request_actions.ScheduleRequestActions] = None
    # Determines whether the call is a validation or an actual call. Only set this property if you want to check whether an activation is subject to additional rules like MFA before actually submitting the request.
    is_validation_only: Optional[bool] = None
    # A message provided by users and administrators when create they create the privilegedAccessGroupAssignmentScheduleRequest object.
    justification: Optional[str] = None
    # The period of the group membership or ownership assignment. Recurring schedules are currently unsupported.
    schedule_info: Optional[request_schedule.RequestSchedule] = None
    # Ticket details linked to the group membership or ownership assignment request including details of the ticket number and ticket system.
    ticket_info: Optional[ticket_info.TicketInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccessScheduleRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessScheduleRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.privilegedAccessGroupAssignmentScheduleRequest":
                from . import privileged_access_group_assignment_schedule_request

                return privileged_access_group_assignment_schedule_request.PrivilegedAccessGroupAssignmentScheduleRequest()
            if mapping_value == "#microsoft.graph.privilegedAccessGroupEligibilityScheduleRequest":
                from . import privileged_access_group_eligibility_schedule_request

                return privileged_access_group_eligibility_schedule_request.PrivilegedAccessGroupEligibilityScheduleRequest()
        return PrivilegedAccessScheduleRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import privileged_access_group_assignment_schedule_request, privileged_access_group_eligibility_schedule_request, request, request_schedule, schedule_request_actions, ticket_info

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(schedule_request_actions.ScheduleRequestActions)),
            "isValidationOnly": lambda n : setattr(self, 'is_validation_only', n.get_bool_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "scheduleInfo": lambda n : setattr(self, 'schedule_info', n.get_object_value(request_schedule.RequestSchedule)),
            "ticketInfo": lambda n : setattr(self, 'ticket_info', n.get_object_value(ticket_info.TicketInfo)),
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
        writer.write_enum_value("action", self.action)
        writer.write_bool_value("isValidationOnly", self.is_validation_only)
        writer.write_str_value("justification", self.justification)
        writer.write_object_value("scheduleInfo", self.schedule_info)
        writer.write_object_value("ticketInfo", self.ticket_info)
    

