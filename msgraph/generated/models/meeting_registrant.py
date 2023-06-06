from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import custom_question_answer, meeting_registrant_base, meeting_registrant_status

from . import meeting_registrant_base

@dataclass
class MeetingRegistrant(meeting_registrant_base.MeetingRegistrantBase):
    odata_type = "#microsoft.graph.meetingRegistrant"
    # The registrant's answer to custom questions.
    custom_question_answers: Optional[List[custom_question_answer.CustomQuestionAnswer]] = None
    # The email address of the registrant.
    email: Optional[str] = None
    # The first name of the registrant.
    first_name: Optional[str] = None
    # The last name of the registrant.
    last_name: Optional[str] = None
    # Time in UTC when the registrant registers for the meeting. Read-only.
    registration_date_time: Optional[datetime] = None
    # The registration status of the registrant. Read-only.
    status: Optional[meeting_registrant_status.MeetingRegistrantStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingRegistrant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingRegistrant
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MeetingRegistrant()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import custom_question_answer, meeting_registrant_base, meeting_registrant_status

        fields: Dict[str, Callable[[Any], None]] = {
            "customQuestionAnswers": lambda n : setattr(self, 'custom_question_answers', n.get_collection_of_object_values(custom_question_answer.CustomQuestionAnswer)),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "registrationDateTime": lambda n : setattr(self, 'registration_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(meeting_registrant_status.MeetingRegistrantStatus)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("customQuestionAnswers", self.custom_question_answers)
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("lastName", self.last_name)
        writer.write_datetime_value("registrationDateTime", self.registration_date_time)
        writer.write_enum_value("status", self.status)
    

