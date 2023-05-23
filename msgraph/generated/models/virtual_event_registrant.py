from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, virtual_event_attendee_registration_status, virtual_event_registration_question_answer

from . import entity

class VirtualEventRegistrant(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new virtualEventRegistrant and sets the default values.
        """
        super().__init__()
        # The cancelationDateTime property
        self._cancelation_date_time: Optional[datetime] = None
        # The email property
        self._email: Optional[str] = None
        # The firstName property
        self._first_name: Optional[str] = None
        # The lastName property
        self._last_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The registrationDateTime property
        self._registration_date_time: Optional[datetime] = None
        # The registrationQuestionAnswers property
        self._registration_question_answers: Optional[List[virtual_event_registration_question_answer.VirtualEventRegistrationQuestionAnswer]] = None
        # The status property
        self._status: Optional[virtual_event_attendee_registration_status.VirtualEventAttendeeRegistrationStatus] = None
        # The userId property
        self._user_id: Optional[str] = None
    
    @property
    def cancelation_date_time(self,) -> Optional[datetime]:
        """
        Gets the cancelationDateTime property value. The cancelationDateTime property
        Returns: Optional[datetime]
        """
        return self._cancelation_date_time
    
    @cancelation_date_time.setter
    def cancelation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the cancelationDateTime property value. The cancelationDateTime property
        Args:
            value: Value to set for the cancelation_date_time property.
        """
        self._cancelation_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventRegistrant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventRegistrant
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VirtualEventRegistrant()
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. The email property
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. The email property
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    @property
    def first_name(self,) -> Optional[str]:
        """
        Gets the firstName property value. The firstName property
        Returns: Optional[str]
        """
        return self._first_name
    
    @first_name.setter
    def first_name(self,value: Optional[str] = None) -> None:
        """
        Sets the firstName property value. The firstName property
        Args:
            value: Value to set for the first_name property.
        """
        self._first_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def last_name(self,) -> Optional[str]:
        """
        Gets the lastName property value. The lastName property
        Returns: Optional[str]
        """
        return self._last_name
    
    @last_name.setter
    def last_name(self,value: Optional[str] = None) -> None:
        """
        Sets the lastName property value. The lastName property
        Args:
            value: Value to set for the last_name property.
        """
        self._last_name = value
    
    @property
    def registration_date_time(self,) -> Optional[datetime]:
        """
        Gets the registrationDateTime property value. The registrationDateTime property
        Returns: Optional[datetime]
        """
        return self._registration_date_time
    
    @registration_date_time.setter
    def registration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the registrationDateTime property value. The registrationDateTime property
        Args:
            value: Value to set for the registration_date_time property.
        """
        self._registration_date_time = value
    
    @property
    def registration_question_answers(self,) -> Optional[List[virtual_event_registration_question_answer.VirtualEventRegistrationQuestionAnswer]]:
        """
        Gets the registrationQuestionAnswers property value. The registrationQuestionAnswers property
        Returns: Optional[List[virtual_event_registration_question_answer.VirtualEventRegistrationQuestionAnswer]]
        """
        return self._registration_question_answers
    
    @registration_question_answers.setter
    def registration_question_answers(self,value: Optional[List[virtual_event_registration_question_answer.VirtualEventRegistrationQuestionAnswer]] = None) -> None:
        """
        Sets the registrationQuestionAnswers property value. The registrationQuestionAnswers property
        Args:
            value: Value to set for the registration_question_answers property.
        """
        self._registration_question_answers = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("cancelationDateTime", self.cancelation_date_time)
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("lastName", self.last_name)
        writer.write_datetime_value("registrationDateTime", self.registration_date_time)
        writer.write_collection_of_object_values("registrationQuestionAnswers", self.registration_question_answers)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("userId", self.user_id)
    
    @property
    def status(self,) -> Optional[virtual_event_attendee_registration_status.VirtualEventAttendeeRegistrationStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[virtual_event_attendee_registration_status.VirtualEventAttendeeRegistrationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[virtual_event_attendee_registration_status.VirtualEventAttendeeRegistrationStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The userId property
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The userId property
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    

