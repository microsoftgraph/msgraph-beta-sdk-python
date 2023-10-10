from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .permissions_request_occurrence_status import PermissionsRequestOccurrenceStatus
    from .status_detail import StatusDetail

from .entity import Entity

@dataclass
class PermissionsRequestChange(Entity):
    # The activeOccurrenceStatus property
    active_occurrence_status: Optional[PermissionsRequestOccurrenceStatus] = None
    # The modificationDateTime property
    modification_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The permissionsRequestId property
    permissions_request_id: Optional[str] = None
    # The statusDetail property
    status_detail: Optional[StatusDetail] = None
    # The ticketId property
    ticket_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PermissionsRequestChange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PermissionsRequestChange
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PermissionsRequestChange()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .permissions_request_occurrence_status import PermissionsRequestOccurrenceStatus
        from .status_detail import StatusDetail

        from .entity import Entity
        from .permissions_request_occurrence_status import PermissionsRequestOccurrenceStatus
        from .status_detail import StatusDetail

        fields: Dict[str, Callable[[Any], None]] = {
            "activeOccurrenceStatus": lambda n : setattr(self, 'active_occurrence_status', n.get_enum_value(PermissionsRequestOccurrenceStatus)),
            "modificationDateTime": lambda n : setattr(self, 'modification_date_time', n.get_datetime_value()),
            "permissionsRequestId": lambda n : setattr(self, 'permissions_request_id', n.get_str_value()),
            "statusDetail": lambda n : setattr(self, 'status_detail', n.get_enum_value(StatusDetail)),
            "ticketId": lambda n : setattr(self, 'ticket_id', n.get_str_value()),
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
        writer.write_enum_value("activeOccurrenceStatus", self.active_occurrence_status)
        writer.write_datetime_value("modificationDateTime", self.modification_date_time)
        writer.write_str_value("permissionsRequestId", self.permissions_request_id)
        writer.write_enum_value("statusDetail", self.status_detail)
        writer.write_str_value("ticketId", self.ticket_id)
    

