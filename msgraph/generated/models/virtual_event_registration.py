from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, virtual_event_registrant, virtual_event_registration_question

from . import entity

@dataclass
class VirtualEventRegistration(entity.Entity):
    # Total capacity of the virtual event.
    capacity: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Registration questions.
    questions: Optional[List[virtual_event_registration_question.VirtualEventRegistrationQuestion]] = None
    # Information of attendees who have registered for the virtual event.
    registrants: Optional[List[virtual_event_registrant.VirtualEventRegistrant]] = None
    # Registration URL of the virtual event.
    registration_web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventRegistration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
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
        from . import entity, virtual_event_registrant, virtual_event_registration_question

        from . import entity, virtual_event_registrant, virtual_event_registration_question

        fields: Dict[str, Callable[[Any], None]] = {
            "capacity": lambda n : setattr(self, 'capacity', n.get_int_value()),
            "questions": lambda n : setattr(self, 'questions', n.get_collection_of_object_values(virtual_event_registration_question.VirtualEventRegistrationQuestion)),
            "registrants": lambda n : setattr(self, 'registrants', n.get_collection_of_object_values(virtual_event_registrant.VirtualEventRegistrant)),
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
    

