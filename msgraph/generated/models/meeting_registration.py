from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

meeting_registration_base = lazy_import('msgraph.generated.models.meeting_registration_base')
meeting_registration_question = lazy_import('msgraph.generated.models.meeting_registration_question')
meeting_speaker = lazy_import('msgraph.generated.models.meeting_speaker')

class MeetingRegistration(meeting_registration_base.MeetingRegistrationBase):
    def __init__(self,) -> None:
        """
        Instantiates a new MeetingRegistration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.meetingRegistration"
        # Custom registration questions.
        self._custom_questions: Optional[List[meeting_registration_question.MeetingRegistrationQuestion]] = None
        # The description of the meeting.
        self._description: Optional[str] = None
        # The meeting end time in UTC.
        self._end_date_time: Optional[datetime] = None
        # The number of times the registration page has been visited. Read-only.
        self._registration_page_view_count: Optional[int] = None
        # The URL of the registration page. Read-only.
        self._registration_page_web_url: Optional[str] = None
        # The meeting speaker's information.
        self._speakers: Optional[List[meeting_speaker.MeetingSpeaker]] = None
        # The meeting start time in UTC.
        self._start_date_time: Optional[datetime] = None
        # The subject of the meeting.
        self._subject: Optional[str] = None
    
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
    
    @property
    def custom_questions(self,) -> Optional[List[meeting_registration_question.MeetingRegistrationQuestion]]:
        """
        Gets the customQuestions property value. Custom registration questions.
        Returns: Optional[List[meeting_registration_question.MeetingRegistrationQuestion]]
        """
        return self._custom_questions
    
    @custom_questions.setter
    def custom_questions(self,value: Optional[List[meeting_registration_question.MeetingRegistrationQuestion]] = None) -> None:
        """
        Sets the customQuestions property value. Custom registration questions.
        Args:
            value: Value to set for the customQuestions property.
        """
        self._custom_questions = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the meeting.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the meeting.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The meeting end time in UTC.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The meeting end time in UTC.
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "custom_questions": lambda n : setattr(self, 'custom_questions', n.get_collection_of_object_values(meeting_registration_question.MeetingRegistrationQuestion)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "registration_page_view_count": lambda n : setattr(self, 'registration_page_view_count', n.get_int_value()),
            "registration_page_web_url": lambda n : setattr(self, 'registration_page_web_url', n.get_str_value()),
            "speakers": lambda n : setattr(self, 'speakers', n.get_collection_of_object_values(meeting_speaker.MeetingSpeaker)),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def registration_page_view_count(self,) -> Optional[int]:
        """
        Gets the registrationPageViewCount property value. The number of times the registration page has been visited. Read-only.
        Returns: Optional[int]
        """
        return self._registration_page_view_count
    
    @registration_page_view_count.setter
    def registration_page_view_count(self,value: Optional[int] = None) -> None:
        """
        Sets the registrationPageViewCount property value. The number of times the registration page has been visited. Read-only.
        Args:
            value: Value to set for the registrationPageViewCount property.
        """
        self._registration_page_view_count = value
    
    @property
    def registration_page_web_url(self,) -> Optional[str]:
        """
        Gets the registrationPageWebUrl property value. The URL of the registration page. Read-only.
        Returns: Optional[str]
        """
        return self._registration_page_web_url
    
    @registration_page_web_url.setter
    def registration_page_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the registrationPageWebUrl property value. The URL of the registration page. Read-only.
        Args:
            value: Value to set for the registrationPageWebUrl property.
        """
        self._registration_page_web_url = value
    
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
    
    @property
    def speakers(self,) -> Optional[List[meeting_speaker.MeetingSpeaker]]:
        """
        Gets the speakers property value. The meeting speaker's information.
        Returns: Optional[List[meeting_speaker.MeetingSpeaker]]
        """
        return self._speakers
    
    @speakers.setter
    def speakers(self,value: Optional[List[meeting_speaker.MeetingSpeaker]] = None) -> None:
        """
        Sets the speakers property value. The meeting speaker's information.
        Args:
            value: Value to set for the speakers property.
        """
        self._speakers = value
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The meeting start time in UTC.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The meeting start time in UTC.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. The subject of the meeting.
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. The subject of the meeting.
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    

