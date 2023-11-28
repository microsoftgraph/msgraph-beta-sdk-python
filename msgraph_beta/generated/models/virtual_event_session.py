from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .date_time_time_zone import DateTimeTimeZone
    from .online_meeting_base import OnlineMeetingBase
    from .virtual_event_presenter import VirtualEventPresenter
    from .virtual_event_registration import VirtualEventRegistration

from .online_meeting_base import OnlineMeetingBase

@dataclass
class VirtualEventSession(OnlineMeetingBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.virtualEventSession"
    # The endDateTime property
    end_date_time: Optional[DateTimeTimeZone] = None
    # The presenters property
    presenters: Optional[List[VirtualEventPresenter]] = None
    # The registrations property
    registrations: Optional[List[VirtualEventRegistration]] = None
    # The startDateTime property
    start_date_time: Optional[DateTimeTimeZone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventSession:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventSession
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventSession()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .date_time_time_zone import DateTimeTimeZone
        from .online_meeting_base import OnlineMeetingBase
        from .virtual_event_presenter import VirtualEventPresenter
        from .virtual_event_registration import VirtualEventRegistration

        from .date_time_time_zone import DateTimeTimeZone
        from .online_meeting_base import OnlineMeetingBase
        from .virtual_event_presenter import VirtualEventPresenter
        from .virtual_event_registration import VirtualEventRegistration

        fields: Dict[str, Callable[[Any], None]] = {
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_object_value(DateTimeTimeZone)),
            "presenters": lambda n : setattr(self, 'presenters', n.get_collection_of_object_values(VirtualEventPresenter)),
            "registrations": lambda n : setattr(self, 'registrations', n.get_collection_of_object_values(VirtualEventRegistration)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_object_value(DateTimeTimeZone)),
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
        writer.write_object_value("endDateTime", self.end_date_time)
        writer.write_collection_of_object_values("presenters", self.presenters)
        writer.write_collection_of_object_values("registrations", self.registrations)
        writer.write_object_value("startDateTime", self.start_date_time)
    

