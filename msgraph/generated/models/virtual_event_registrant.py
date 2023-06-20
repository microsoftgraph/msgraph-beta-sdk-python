from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, virtual_event_attendee_registration_status, virtual_event_registration_question_answer

from . import entity

@dataclass
class VirtualEventRegistrant(entity.Entity):
    # Time in UTC when the registrant cancels their registration for the virtual event. Only appears when applicable.
    cancelation_date_time: Optional[datetime] = None
    # Email address of the registrant.
    email: Optional[str] = None
    # First name of the registrant.
    first_name: Optional[str] = None
    # Last name of the registrant.
    last_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Time in UTC when the registrant registers for the virtual event.
    registration_date_time: Optional[datetime] = None
    # The registrant's answer to the registration questions.
    registration_question_answers: Optional[List[virtual_event_registration_question_answer.VirtualEventRegistrationQuestionAnswer]] = None
    # Registration status of the registrant. Read-only.
    status: Optional[virtual_event_attendee_registration_status.VirtualEventAttendeeRegistrationStatus] = None
    # The registrant's AAD user ID. Only appears when the registrant is registered in AAD.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventRegistrant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventRegistrant
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventRegistrant()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, virtual_event_attendee_registration_status, virtual_event_registration_question_answer

        from . import entity, virtual_event_attendee_registration_status, virtual_event_registration_question_answer

        fields: Dict[str, Callable[[Any], None]] = {
            "cancelationDateTime": lambda n : setattr(self, 'cancelation_date_time', n.get_datetime_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "registrationDateTime": lambda n : setattr(self, 'registration_date_time', n.get_datetime_value()),
            "registrationQuestionAnswers": lambda n : setattr(self, 'registration_question_answers', n.get_collection_of_object_values(virtual_event_registration_question_answer.VirtualEventRegistrationQuestionAnswer)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(virtual_event_attendee_registration_status.VirtualEventAttendeeRegistrationStatus)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_datetime_value("cancelationDateTime", self.cancelation_date_time)
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("lastName", self.last_name)
        writer.write_datetime_value("registrationDateTime", self.registration_date_time)
        writer.write_collection_of_object_values("registrationQuestionAnswers", self.registration_question_answers)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("userId", self.user_id)
    

