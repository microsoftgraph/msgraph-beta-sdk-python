from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import teamwork_user_identity

@dataclass
class TeamworkOnlineMeetingInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The identifier of the calendar event associated with the meeting.
    calendar_event_id: Optional[str] = None
    # The URL which can be clicked on to join or uniquely identify the meeting.
    join_web_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The organizer of the meeting.
    organizer: Optional[teamwork_user_identity.TeamworkUserIdentity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkOnlineMeetingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkOnlineMeetingInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamworkOnlineMeetingInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import teamwork_user_identity

        from . import teamwork_user_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "calendarEventId": lambda n : setattr(self, 'calendar_event_id', n.get_str_value()),
            "joinWebUrl": lambda n : setattr(self, 'join_web_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organizer": lambda n : setattr(self, 'organizer', n.get_object_value(teamwork_user_identity.TeamworkUserIdentity)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("calendarEventId", self.calendar_event_id)
        writer.write_str_value("joinWebUrl", self.join_web_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("organizer", self.organizer)
        writer.write_additional_data_value(self.additional_data)
    

