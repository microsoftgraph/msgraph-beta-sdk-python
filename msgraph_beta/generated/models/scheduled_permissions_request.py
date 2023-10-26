from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .permissions_definition import PermissionsDefinition
    from .request_schedule import RequestSchedule
    from .status_detail import StatusDetail
    from .ticket_info import TicketInfo

from .entity import Entity

@dataclass
class ScheduledPermissionsRequest(Entity):
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The justification property
    justification: Optional[str] = None
    # The notes property
    notes: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The requestedPermissions property
    requested_permissions: Optional[PermissionsDefinition] = None
    # The scheduleInfo property
    schedule_info: Optional[RequestSchedule] = None
    # The statusDetail property
    status_detail: Optional[StatusDetail] = None
    # The ticketInfo property
    ticket_info: Optional[TicketInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ScheduledPermissionsRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ScheduledPermissionsRequest
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ScheduledPermissionsRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .permissions_definition import PermissionsDefinition
        from .request_schedule import RequestSchedule
        from .status_detail import StatusDetail
        from .ticket_info import TicketInfo

        from .entity import Entity
        from .permissions_definition import PermissionsDefinition
        from .request_schedule import RequestSchedule
        from .status_detail import StatusDetail
        from .ticket_info import TicketInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "requestedPermissions": lambda n : setattr(self, 'requested_permissions', n.get_object_value(PermissionsDefinition)),
            "scheduleInfo": lambda n : setattr(self, 'schedule_info', n.get_object_value(RequestSchedule)),
            "statusDetail": lambda n : setattr(self, 'status_detail', n.get_enum_value(StatusDetail)),
            "ticketInfo": lambda n : setattr(self, 'ticket_info', n.get_object_value(TicketInfo)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("justification", self.justification)
        writer.write_str_value("notes", self.notes)
        writer.write_object_value("requestedPermissions", self.requested_permissions)
        writer.write_object_value("scheduleInfo", self.schedule_info)
        writer.write_enum_value("statusDetail", self.status_detail)
        writer.write_object_value("ticketInfo", self.ticket_info)
    

