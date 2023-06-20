from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, external_meeting_registrant, meeting_registrant

from . import entity

@dataclass
class MeetingRegistrantBase(entity.Entity):
    # A unique web URL for the registrant to join the meeting. Read-only.
    join_web_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingRegistrantBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingRegistrantBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalMeetingRegistrant".casefold():
            from . import external_meeting_registrant

            return external_meeting_registrant.ExternalMeetingRegistrant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.meetingRegistrant".casefold():
            from . import meeting_registrant

            return meeting_registrant.MeetingRegistrant()
        return MeetingRegistrantBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, external_meeting_registrant, meeting_registrant

        from . import entity, external_meeting_registrant, meeting_registrant

        fields: Dict[str, Callable[[Any], None]] = {
            "joinWebUrl": lambda n : setattr(self, 'join_web_url', n.get_str_value()),
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
        writer.write_str_value("joinWebUrl", self.join_web_url)
    

