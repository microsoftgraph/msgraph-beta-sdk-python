from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import communications_identity_set, date_time_time_zone, entity, virtual_event_presenter, virtual_event_session, virtual_event_status, virtual_event_webinar

from . import entity

@dataclass
class VirtualEvent(entity.Entity):
    # Identity information of who created the virtual event. Inherited from virtualEvent.
    created_by: Optional[communications_identity_set.CommunicationsIdentitySet] = None
    # Description of the virtual event.
    description: Optional[str] = None
    # Display name of the virtual event
    display_name: Optional[str] = None
    # End time of the virtual event.
    end_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Presenters' information of the virtual event.
    presenters: Optional[List[virtual_event_presenter.VirtualEventPresenter]] = None
    # Sessions of the virtual event.
    sessions: Optional[List[virtual_event_session.VirtualEventSession]] = None
    # Start time of the virtual event.
    start_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
    # Status of the virtual event. The possible values are: draft, published, canceled, unknownFutureValue.
    status: Optional[virtual_event_status.VirtualEventStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEvent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventWebinar".casefold():
            from . import virtual_event_webinar

            return virtual_event_webinar.VirtualEventWebinar()
        return VirtualEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import communications_identity_set, date_time_time_zone, entity, virtual_event_presenter, virtual_event_session, virtual_event_status, virtual_event_webinar

        from . import communications_identity_set, date_time_time_zone, entity, virtual_event_presenter, virtual_event_session, virtual_event_status, virtual_event_webinar

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(communications_identity_set.CommunicationsIdentitySet)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "presenters": lambda n : setattr(self, 'presenters', n.get_collection_of_object_values(virtual_event_presenter.VirtualEventPresenter)),
            "sessions": lambda n : setattr(self, 'sessions', n.get_collection_of_object_values(virtual_event_session.VirtualEventSession)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(virtual_event_status.VirtualEventStatus)),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("endDateTime", self.end_date_time)
        writer.write_collection_of_object_values("presenters", self.presenters)
        writer.write_collection_of_object_values("sessions", self.sessions)
        writer.write_object_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
    

