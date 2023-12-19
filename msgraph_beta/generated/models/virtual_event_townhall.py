from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .communications_user_identity import CommunicationsUserIdentity
    from .virtual_event import VirtualEvent
    from .virtual_event_townhall_audience import VirtualEventTownhall_audience

from .virtual_event import VirtualEvent

@dataclass
class VirtualEventTownhall(VirtualEvent):
    # The audience property
    audience: Optional[VirtualEventTownhall_audience] = None
    # The coOrganizers property
    co_organizers: Optional[List[CommunicationsUserIdentity]] = None
    # The invitedAttendees property
    invited_attendees: Optional[List[CommunicationsUserIdentity]] = None
    # The isInviteOnly property
    is_invite_only: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventTownhall:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventTownhall
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventTownhall()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .communications_user_identity import CommunicationsUserIdentity
        from .virtual_event import VirtualEvent
        from .virtual_event_townhall_audience import VirtualEventTownhall_audience

        from .communications_user_identity import CommunicationsUserIdentity
        from .virtual_event import VirtualEvent
        from .virtual_event_townhall_audience import VirtualEventTownhall_audience

        fields: Dict[str, Callable[[Any], None]] = {
            "audience": lambda n : setattr(self, 'audience', n.get_enum_value(VirtualEventTownhall_audience)),
            "coOrganizers": lambda n : setattr(self, 'co_organizers', n.get_collection_of_object_values(CommunicationsUserIdentity)),
            "invitedAttendees": lambda n : setattr(self, 'invited_attendees', n.get_collection_of_object_values(CommunicationsUserIdentity)),
            "isInviteOnly": lambda n : setattr(self, 'is_invite_only', n.get_bool_value()),
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
        writer.write_enum_value("audience", self.audience)
        writer.write_collection_of_object_values("coOrganizers", self.co_organizers)
        writer.write_collection_of_object_values("invitedAttendees", self.invited_attendees)
        writer.write_bool_value("isInviteOnly", self.is_invite_only)
    

