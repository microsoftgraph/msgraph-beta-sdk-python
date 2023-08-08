from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .virtual_event_registrant import VirtualEventRegistrant
    from .virtual_event_registration_question import VirtualEventRegistrationQuestion

from .entity import Entity

@dataclass
class VirtualEventRegistration(Entity):
    # Total capacity of the virtual event.
    capacity: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Registration questions.
    questions: Optional[List[VirtualEventRegistrationQuestion]] = None
    # Information of attendees who have registered for the virtual event.
    registrants: Optional[List[VirtualEventRegistrant]] = None
    # Registration URL of the virtual event.
    registration_web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventRegistration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventRegistration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventRegistration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .virtual_event_registrant import VirtualEventRegistrant
        from .virtual_event_registration_question import VirtualEventRegistrationQuestion

        from .entity import Entity
        from .virtual_event_registrant import VirtualEventRegistrant
        from .virtual_event_registration_question import VirtualEventRegistrationQuestion

        fields: Dict[str, Callable[[Any], None]] = {
            "capacity": lambda n : setattr(self, 'capacity', n.get_int_value()),
            "questions": lambda n : setattr(self, 'questions', n.get_collection_of_object_values(VirtualEventRegistrationQuestion)),
            "registrants": lambda n : setattr(self, 'registrants', n.get_collection_of_object_values(VirtualEventRegistrant)),
            "registrationWebUrl": lambda n : setattr(self, 'registration_web_url', n.get_str_value()),
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
        writer.write_int_value("capacity", self.capacity)
        writer.write_collection_of_object_values("questions", self.questions)
        writer.write_collection_of_object_values("registrants", self.registrants)
        writer.write_str_value("registrationWebUrl", self.registration_web_url)
    

