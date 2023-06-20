from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import communications_user_identity, meeting_audience, virtual_event, virtual_event_registration

from . import virtual_event

@dataclass
class VirtualEventWebinar(virtual_event.VirtualEvent):
    # To whom the webinar is visible.
    audience: Optional[meeting_audience.MeetingAudience] = None
    # Identity information of co-organizers of the webinar.
    co_organizers: Optional[List[communications_user_identity.CommunicationsUserIdentity]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Registration configuration of the webinar.
    registration: Optional[virtual_event_registration.VirtualEventRegistration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventWebinar:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventWebinar
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventWebinar()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import communications_user_identity, meeting_audience, virtual_event, virtual_event_registration

        from . import communications_user_identity, meeting_audience, virtual_event, virtual_event_registration

        fields: Dict[str, Callable[[Any], None]] = {
            "audience": lambda n : setattr(self, 'audience', n.get_enum_value(meeting_audience.MeetingAudience)),
            "coOrganizers": lambda n : setattr(self, 'co_organizers', n.get_collection_of_object_values(communications_user_identity.CommunicationsUserIdentity)),
            "registration": lambda n : setattr(self, 'registration', n.get_object_value(virtual_event_registration.VirtualEventRegistration)),
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
        writer.write_enum_value("audience", self.audience)
        writer.write_collection_of_object_values("coOrganizers", self.co_organizers)
        writer.write_object_value("registration", self.registration)
    

