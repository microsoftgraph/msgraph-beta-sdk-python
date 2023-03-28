from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import booking_customer_information_base, booking_question_answer, location

from . import booking_customer_information_base

class BookingCustomerInformation(booking_customer_information_base.BookingCustomerInformationBase):
    def __init__(self,) -> None:
        """
        Instantiates a new BookingCustomerInformation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.bookingCustomerInformation"
        # It consists of the list of custom questions and answers given by the customer as part of the appointment.
        self._custom_question_answers: Optional[List[booking_question_answer.BookingQuestionAnswer]] = None
        # The ID of the bookingCustomer for this appointment. If no ID is specified when an appointment is created, then a new bookingCustomer object is created. Once set, you should consider the customerId immutable.
        self._customer_id: Optional[str] = None
        # The SMTP address of the bookingCustomer who is booking the appointment.
        self._email_address: Optional[str] = None
        # Represents location information for the bookingCustomer who is booking the appointment.
        self._location: Optional[location.Location] = None
        # The customer's name.
        self._name: Optional[str] = None
        # Notes from the customer associated with this appointment. You can get the value only when reading this bookingAppointment by its ID. You can set this property only when initially creating an appointment with a new customer. After that point, the value is computed from the customer represented by the customerId.
        self._notes: Optional[str] = None
        # The customer's phone number.
        self._phone: Optional[str] = None
        # Indicates if the SMS notifications will be sent to the customer for the appointment
        self._sms_notifications_enabled: Optional[bool] = None
        # The time zone of the customer. For a list of possible values, see dateTimeTimeZone.
        self._time_zone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingCustomerInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingCustomerInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BookingCustomerInformation()
    
    @property
    def custom_question_answers(self,) -> Optional[List[booking_question_answer.BookingQuestionAnswer]]:
        """
        Gets the customQuestionAnswers property value. It consists of the list of custom questions and answers given by the customer as part of the appointment.
        Returns: Optional[List[booking_question_answer.BookingQuestionAnswer]]
        """
        return self._custom_question_answers
    
    @custom_question_answers.setter
    def custom_question_answers(self,value: Optional[List[booking_question_answer.BookingQuestionAnswer]] = None) -> None:
        """
        Sets the customQuestionAnswers property value. It consists of the list of custom questions and answers given by the customer as part of the appointment.
        Args:
            value: Value to set for the custom_question_answers property.
        """
        self._custom_question_answers = value
    
    @property
    def customer_id(self,) -> Optional[str]:
        """
        Gets the customerId property value. The ID of the bookingCustomer for this appointment. If no ID is specified when an appointment is created, then a new bookingCustomer object is created. Once set, you should consider the customerId immutable.
        Returns: Optional[str]
        """
        return self._customer_id
    
    @customer_id.setter
    def customer_id(self,value: Optional[str] = None) -> None:
        """
        Sets the customerId property value. The ID of the bookingCustomer for this appointment. If no ID is specified when an appointment is created, then a new bookingCustomer object is created. Once set, you should consider the customerId immutable.
        Args:
            value: Value to set for the customer_id property.
        """
        self._customer_id = value
    
    @property
    def email_address(self,) -> Optional[str]:
        """
        Gets the emailAddress property value. The SMTP address of the bookingCustomer who is booking the appointment.
        Returns: Optional[str]
        """
        return self._email_address
    
    @email_address.setter
    def email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the emailAddress property value. The SMTP address of the bookingCustomer who is booking the appointment.
        Args:
            value: Value to set for the email_address property.
        """
        self._email_address = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import booking_customer_information_base, booking_question_answer, location

        fields: Dict[str, Callable[[Any], None]] = {
            "customerId": lambda n : setattr(self, 'customer_id', n.get_str_value()),
            "customQuestionAnswers": lambda n : setattr(self, 'custom_question_answers', n.get_collection_of_object_values(booking_question_answer.BookingQuestionAnswer)),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(location.Location)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "smsNotificationsEnabled": lambda n : setattr(self, 'sms_notifications_enabled', n.get_bool_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def location(self,) -> Optional[location.Location]:
        """
        Gets the location property value. Represents location information for the bookingCustomer who is booking the appointment.
        Returns: Optional[location.Location]
        """
        return self._location
    
    @location.setter
    def location(self,value: Optional[location.Location] = None) -> None:
        """
        Sets the location property value. Represents location information for the bookingCustomer who is booking the appointment.
        Args:
            value: Value to set for the location property.
        """
        self._location = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The customer's name.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The customer's name.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def notes(self,) -> Optional[str]:
        """
        Gets the notes property value. Notes from the customer associated with this appointment. You can get the value only when reading this bookingAppointment by its ID. You can set this property only when initially creating an appointment with a new customer. After that point, the value is computed from the customer represented by the customerId.
        Returns: Optional[str]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[str] = None) -> None:
        """
        Sets the notes property value. Notes from the customer associated with this appointment. You can get the value only when reading this bookingAppointment by its ID. You can set this property only when initially creating an appointment with a new customer. After that point, the value is computed from the customer represented by the customerId.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def phone(self,) -> Optional[str]:
        """
        Gets the phone property value. The customer's phone number.
        Returns: Optional[str]
        """
        return self._phone
    
    @phone.setter
    def phone(self,value: Optional[str] = None) -> None:
        """
        Sets the phone property value. The customer's phone number.
        Args:
            value: Value to set for the phone property.
        """
        self._phone = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("customerId", self.customer_id)
        writer.write_collection_of_object_values("customQuestionAnswers", self.custom_question_answers)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_object_value("location", self.location)
        writer.write_str_value("name", self.name)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("phone", self.phone)
        writer.write_bool_value("smsNotificationsEnabled", self.sms_notifications_enabled)
        writer.write_str_value("timeZone", self.time_zone)
    
    @property
    def sms_notifications_enabled(self,) -> Optional[bool]:
        """
        Gets the smsNotificationsEnabled property value. Indicates if the SMS notifications will be sent to the customer for the appointment
        Returns: Optional[bool]
        """
        return self._sms_notifications_enabled
    
    @sms_notifications_enabled.setter
    def sms_notifications_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the smsNotificationsEnabled property value. Indicates if the SMS notifications will be sent to the customer for the appointment
        Args:
            value: Value to set for the sms_notifications_enabled property.
        """
        self._sms_notifications_enabled = value
    
    @property
    def time_zone(self,) -> Optional[str]:
        """
        Gets the timeZone property value. The time zone of the customer. For a list of possible values, see dateTimeTimeZone.
        Returns: Optional[str]
        """
        return self._time_zone
    
    @time_zone.setter
    def time_zone(self,value: Optional[str] = None) -> None:
        """
        Sets the timeZone property value. The time zone of the customer. For a list of possible values, see dateTimeTimeZone.
        Args:
            value: Value to set for the time_zone property.
        """
        self._time_zone = value
    

