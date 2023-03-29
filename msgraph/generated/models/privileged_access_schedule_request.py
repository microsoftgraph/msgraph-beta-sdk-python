from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import privileged_access_group_assignment_schedule_request, privileged_access_group_eligibility_schedule_request, request, request_schedule, schedule_request_actions, ticket_info

from . import request

class PrivilegedAccessScheduleRequest(request.Request):
    def __init__(self,) -> None:
        """
        Instantiates a new PrivilegedAccessScheduleRequest and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.privilegedAccessScheduleRequest"
        # The action property
        self._action: Optional[schedule_request_actions.ScheduleRequestActions] = None
        # The isValidationOnly property
        self._is_validation_only: Optional[bool] = None
        # The justification property
        self._justification: Optional[str] = None
        # The scheduleInfo property
        self._schedule_info: Optional[request_schedule.RequestSchedule] = None
        # The ticketInfo property
        self._ticket_info: Optional[ticket_info.TicketInfo] = None
    
    @property
    def action(self,) -> Optional[schedule_request_actions.ScheduleRequestActions]:
        """
        Gets the action property value. The action property
        Returns: Optional[schedule_request_actions.ScheduleRequestActions]
        """
        return self._action
    
    @action.setter
    def action(self,value: Optional[schedule_request_actions.ScheduleRequestActions] = None) -> None:
        """
        Sets the action property value. The action property
        Args:
            value: Value to set for the action property.
        """
        self._action = value
    
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
    
    @property
    def is_validation_only(self,) -> Optional[bool]:
        """
        Gets the isValidationOnly property value. The isValidationOnly property
        Returns: Optional[bool]
        """
        return self._is_validation_only
    
    @is_validation_only.setter
    def is_validation_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the isValidationOnly property value. The isValidationOnly property
        Args:
            value: Value to set for the is_validation_only property.
        """
        self._is_validation_only = value
    
    @property
    def justification(self,) -> Optional[str]:
        """
        Gets the justification property value. The justification property
        Returns: Optional[str]
        """
        return self._justification
    
    @justification.setter
    def justification(self,value: Optional[str] = None) -> None:
        """
        Sets the justification property value. The justification property
        Args:
            value: Value to set for the justification property.
        """
        self._justification = value
    
    @property
    def schedule_info(self,) -> Optional[request_schedule.RequestSchedule]:
        """
        Gets the scheduleInfo property value. The scheduleInfo property
        Returns: Optional[request_schedule.RequestSchedule]
        """
        return self._schedule_info
    
    @schedule_info.setter
    def schedule_info(self,value: Optional[request_schedule.RequestSchedule] = None) -> None:
        """
        Sets the scheduleInfo property value. The scheduleInfo property
        Args:
            value: Value to set for the schedule_info property.
        """
        self._schedule_info = value
    
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
    
    @property
    def ticket_info(self,) -> Optional[ticket_info.TicketInfo]:
        """
        Gets the ticketInfo property value. The ticketInfo property
        Returns: Optional[ticket_info.TicketInfo]
        """
        return self._ticket_info
    
    @ticket_info.setter
    def ticket_info(self,value: Optional[ticket_info.TicketInfo] = None) -> None:
        """
        Sets the ticketInfo property value. The ticketInfo property
        Args:
            value: Value to set for the ticket_info property.
        """
        self._ticket_info = value
    

