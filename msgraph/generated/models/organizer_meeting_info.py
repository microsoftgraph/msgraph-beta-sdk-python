from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_set, meeting_info

from . import meeting_info

@dataclass
class OrganizerMeetingInfo(meeting_info.MeetingInfo):
    odata_type = "#microsoft.graph.organizerMeetingInfo"
    # The organizer property
    organizer: Optional[identity_set.IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OrganizerMeetingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OrganizerMeetingInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OrganizerMeetingInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_set, meeting_info

        from . import identity_set, meeting_info

        fields: Dict[str, Callable[[Any], None]] = {
            "organizer": lambda n : setattr(self, 'organizer', n.get_object_value(identity_set.IdentitySet)),
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
        writer.write_object_value("organizer", self.organizer)
    

