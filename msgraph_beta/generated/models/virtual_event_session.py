from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .online_meeting import OnlineMeeting
    from .virtual_event_registration import VirtualEventRegistration

from .online_meeting import OnlineMeeting

@dataclass
class VirtualEventSession(OnlineMeeting):
    # The OdataType property
    odata_type: Optional[str] = None
    # Registration records of this virtual event session.
    registrations: Optional[List[VirtualEventRegistration]] = None
    
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
        from .online_meeting import OnlineMeeting
        from .virtual_event_registration import VirtualEventRegistration

        from .online_meeting import OnlineMeeting
        from .virtual_event_registration import VirtualEventRegistration

        fields: Dict[str, Callable[[Any], None]] = {
            "registrations": lambda n : setattr(self, 'registrations', n.get_collection_of_object_values(VirtualEventRegistration)),
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
        writer.write_collection_of_object_values("registrations", self.registrations)
    

