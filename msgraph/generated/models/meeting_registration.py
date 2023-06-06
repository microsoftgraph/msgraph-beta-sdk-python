from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import meeting_registration_base, meeting_registration_question, meeting_speaker

from . import meeting_registration_base

@dataclass
class MeetingRegistration(meeting_registration_base.MeetingRegistrationBase):
    odata_type = "#microsoft.graph.meetingRegistration"
    # Custom registration questions.
    custom_questions: Optional[List[meeting_registration_question.MeetingRegistrationQuestion]] = None
    # The description of the meeting.
    description: Optional[str] = None
    # The meeting end time in UTC.
    end_date_time: Optional[datetime] = None
    # The number of times the registration page has been visited. Read-only.
    registration_page_view_count: Optional[int] = None
    # The URL of the registration page. Read-only.
    registration_page_web_url: Optional[str] = None
    # The meeting speaker's information.
    speakers: Optional[List[meeting_speaker.MeetingSpeaker]] = None
    # The meeting start time in UTC.
    start_date_time: Optional[datetime] = None
    # The subject of the meeting.
    subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingRegistration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingRegistration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MeetingRegistration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import meeting_registration_base, meeting_registration_question, meeting_speaker

        fields: Dict[str, Callable[[Any], None]] = {
            "customQuestions": lambda n : setattr(self, 'custom_questions', n.get_collection_of_object_values(meeting_registration_question.MeetingRegistrationQuestion)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "registrationPageViewCount": lambda n : setattr(self, 'registration_page_view_count', n.get_int_value()),
            "registrationPageWebUrl": lambda n : setattr(self, 'registration_page_web_url', n.get_str_value()),
            "speakers": lambda n : setattr(self, 'speakers', n.get_collection_of_object_values(meeting_speaker.MeetingSpeaker)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
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
        writer.write_collection_of_object_values("customQuestions", self.custom_questions)
        writer.write_str_value("description", self.description)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_int_value("registrationPageViewCount", self.registration_page_view_count)
        writer.write_str_value("registrationPageWebUrl", self.registration_page_web_url)
        writer.write_collection_of_object_values("speakers", self.speakers)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("subject", self.subject)
    

