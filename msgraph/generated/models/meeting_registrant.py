from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

custom_question_answer = lazy_import('msgraph.generated.models.custom_question_answer')
meeting_registrant_base = lazy_import('msgraph.generated.models.meeting_registrant_base')
meeting_registrant_status = lazy_import('msgraph.generated.models.meeting_registrant_status')

class MeetingRegistrant(meeting_registrant_base.MeetingRegistrantBase):
    def __init__(self,) -> None:
        """
        Instantiates a new MeetingRegistrant and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.meetingRegistrant"
        # The registrant's answer to custom questions.
        self._custom_question_answers: Optional[List[custom_question_answer.CustomQuestionAnswer]] = None
        # The email address of the registrant.
        self._email: Optional[str] = None
        # The first name of the registrant.
        self._first_name: Optional[str] = None
        # The last name of the registrant.
        self._last_name: Optional[str] = None
        # Time in UTC when the registrant registers for the meeting. Read-only.
        self._registration_date_time: Optional[datetime] = None
        # The registration status of the registrant. Read-only.
        self._status: Optional[meeting_registrant_status.MeetingRegistrantStatus] = None
    
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
    
    @property
    def custom_question_answers(self,) -> Optional[List[custom_question_answer.CustomQuestionAnswer]]:
        """
        Gets the customQuestionAnswers property value. The registrant's answer to custom questions.
        Returns: Optional[List[custom_question_answer.CustomQuestionAnswer]]
        """
        return self._custom_question_answers
    
    @custom_question_answers.setter
    def custom_question_answers(self,value: Optional[List[custom_question_answer.CustomQuestionAnswer]] = None) -> None:
        """
        Sets the customQuestionAnswers property value. The registrant's answer to custom questions.
        Args:
            value: Value to set for the customQuestionAnswers property.
        """
        self._custom_question_answers = value
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. The email address of the registrant.
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. The email address of the registrant.
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    @property
    def first_name(self,) -> Optional[str]:
        """
        Gets the firstName property value. The first name of the registrant.
        Returns: Optional[str]
        """
        return self._first_name
    
    @first_name.setter
    def first_name(self,value: Optional[str] = None) -> None:
        """
        Sets the firstName property value. The first name of the registrant.
        Args:
            value: Value to set for the firstName property.
        """
        self._first_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "custom_question_answers": lambda n : setattr(self, 'custom_question_answers', n.get_collection_of_object_values(custom_question_answer.CustomQuestionAnswer)),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "first_name": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "last_name": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "registration_date_time": lambda n : setattr(self, 'registration_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(meeting_registrant_status.MeetingRegistrantStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_name(self,) -> Optional[str]:
        """
        Gets the lastName property value. The last name of the registrant.
        Returns: Optional[str]
        """
        return self._last_name
    
    @last_name.setter
    def last_name(self,value: Optional[str] = None) -> None:
        """
        Sets the lastName property value. The last name of the registrant.
        Args:
            value: Value to set for the lastName property.
        """
        self._last_name = value
    
    @property
    def registration_date_time(self,) -> Optional[datetime]:
        """
        Gets the registrationDateTime property value. Time in UTC when the registrant registers for the meeting. Read-only.
        Returns: Optional[datetime]
        """
        return self._registration_date_time
    
    @registration_date_time.setter
    def registration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the registrationDateTime property value. Time in UTC when the registrant registers for the meeting. Read-only.
        Args:
            value: Value to set for the registrationDateTime property.
        """
        self._registration_date_time = value
    
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
    
    @property
    def status(self,) -> Optional[meeting_registrant_status.MeetingRegistrantStatus]:
        """
        Gets the status property value. The registration status of the registrant. Read-only.
        Returns: Optional[meeting_registrant_status.MeetingRegistrantStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[meeting_registrant_status.MeetingRegistrantStatus] = None) -> None:
        """
        Sets the status property value. The registration status of the registrant. Read-only.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

