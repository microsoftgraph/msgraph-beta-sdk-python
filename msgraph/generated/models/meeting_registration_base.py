from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, external_meeting_registration, meeting_audience, meeting_registrant_base, meeting_registration

from . import entity

@dataclass
class MeetingRegistrationBase(entity.Entity):
    # Specifies who can register for the meeting.
    allowed_registrant: Optional[meeting_audience.MeetingAudience] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Registrants of the online meeting.
    registrants: Optional[List[meeting_registrant_base.MeetingRegistrantBase]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingRegistrationBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingRegistrationBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalMeetingRegistration".casefold():
            from . import external_meeting_registration

            return external_meeting_registration.ExternalMeetingRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.meetingRegistration".casefold():
            from . import meeting_registration

            return meeting_registration.MeetingRegistration()
        return MeetingRegistrationBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, external_meeting_registration, meeting_audience, meeting_registrant_base, meeting_registration

        from . import entity, external_meeting_registration, meeting_audience, meeting_registrant_base, meeting_registration

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedRegistrant": lambda n : setattr(self, 'allowed_registrant', n.get_enum_value(meeting_audience.MeetingAudience)),
            "registrants": lambda n : setattr(self, 'registrants', n.get_collection_of_object_values(meeting_registrant_base.MeetingRegistrantBase)),
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
        writer.write_enum_value("allowedRegistrant", self.allowed_registrant)
        writer.write_collection_of_object_values("registrants", self.registrants)
    

