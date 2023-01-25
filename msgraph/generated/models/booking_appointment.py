from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

booking_customer_information_base = lazy_import('msgraph.generated.models.booking_customer_information_base')
booking_invoice_status = lazy_import('msgraph.generated.models.booking_invoice_status')
booking_price_type = lazy_import('msgraph.generated.models.booking_price_type')
booking_reminder = lazy_import('msgraph.generated.models.booking_reminder')
date_time_time_zone = lazy_import('msgraph.generated.models.date_time_time_zone')
entity = lazy_import('msgraph.generated.models.entity')
location = lazy_import('msgraph.generated.models.location')

class BookingAppointment(entity.Entity):
    """
    Represents a booked appointment of a service by a customer in a business.
    """
    @property
    def additional_information(self,) -> Optional[str]:
        """
        Gets the additionalInformation property value. Additional information that is sent to the customer when an appointment is confirmed.
        Returns: Optional[str]
        """
        return self._additional_information
    
    @additional_information.setter
    def additional_information(self,value: Optional[str] = None) -> None:
        """
        Sets the additionalInformation property value. Additional information that is sent to the customer when an appointment is confirmed.
        Args:
            value: Value to set for the additionalInformation property.
        """
        self._additional_information = value
    
    @property
    def anonymous_join_web_url(self,) -> Optional[str]:
        """
        Gets the anonymousJoinWebUrl property value. The URL of the meeting to join anonymously.
        Returns: Optional[str]
        """
        return self._anonymous_join_web_url
    
    @anonymous_join_web_url.setter
    def anonymous_join_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the anonymousJoinWebUrl property value. The URL of the meeting to join anonymously.
        Args:
            value: Value to set for the anonymousJoinWebUrl property.
        """
        self._anonymous_join_web_url = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new bookingAppointment and sets the default values.
        """
        super().__init__()
        # Additional information that is sent to the customer when an appointment is confirmed.
        self._additional_information: Optional[str] = None
        # The URL of the meeting to join anonymously.
        self._anonymous_join_web_url: Optional[str] = None
        # The SMTP address of the bookingCustomer who is booking the appointment.
        self._customer_email_address: Optional[str] = None
        # The ID of the bookingCustomer for this appointment. If no ID is specified when an appointment is created, then a new bookingCustomer object is created. Once set, you should consider the customerId immutable.
        self._customer_id: Optional[str] = None
        # Represents location information for the bookingCustomer who is booking the appointment.
        self._customer_location: Optional[location.Location] = None
        # The customer's name.
        self._customer_name: Optional[str] = None
        # Notes from the customer associated with this appointment. You can get the value only when reading this bookingAppointment by its ID.  You can set this property only when initially creating an appointment with a new customer. After that point, the value is computed from the customer represented by customerId.
        self._customer_notes: Optional[str] = None
        # The customer's phone number.
        self._customer_phone: Optional[str] = None
        # A collection of the customer properties for an appointment. An appointment will contain a list of customer information and each unit will indicate the properties of a customer who is part of that appointment. Optional.
        self._customers: Optional[List[booking_customer_information_base.BookingCustomerInformationBase]] = None
        # The time zone of the customer. For a list of possible values, see dateTimeTimeZone.
        self._customer_time_zone: Optional[str] = None
        # The length of the appointment, denoted in ISO8601 format.
        self._duration: Optional[Timedelta] = None
        # The end property
        self._end: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The current number of customers in the appointment.
        self._filled_attendees_count: Optional[int] = None
        # The billed amount on the invoice.
        self._invoice_amount: Optional[float] = None
        # The date, time, and time zone of the invoice for this appointment.
        self._invoice_date: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The ID of the invoice.
        self._invoice_id: Optional[str] = None
        # The invoiceStatus property
        self._invoice_status: Optional[booking_invoice_status.BookingInvoiceStatus] = None
        # The URL of the invoice in Microsoft Bookings.
        self._invoice_url: Optional[str] = None
        # True indicates that the appointment will be held online. Default value is false.
        self._is_location_online: Optional[bool] = None
        # The URL of the online meeting for the appointment.
        self._join_web_url: Optional[str] = None
        # The maximum number of customers allowed in an appointment. If maximumAttendeesCount of the service is greater than 1, pass valid customer IDs while creating or updating an appointment. To create a customer, use the Create bookingCustomer operation.
        self._maximum_attendees_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The onlineMeetingUrl property
        self._online_meeting_url: Optional[str] = None
        # True indicates that the bookingCustomer for this appointment does not wish to receive a confirmation for this appointment.
        self._opt_out_of_customer_email: Optional[bool] = None
        # The amount of time to reserve after the appointment ends, for cleaning up, as an example. The value is expressed in ISO8601 format.
        self._post_buffer: Optional[Timedelta] = None
        # The amount of time to reserve before the appointment begins, for preparation, as an example. The value is expressed in ISO8601 format.
        self._pre_buffer: Optional[Timedelta] = None
        # The regular price for an appointment for the specified bookingService.
        self._price: Optional[float] = None
        # Represents the type of pricing of a booking service.
        self._price_type: Optional[booking_price_type.BookingPriceType] = None
        # The collection of customer reminders sent for this appointment. The value of this property is available only when reading this bookingAppointment by its ID.
        self._reminders: Optional[List[booking_reminder.BookingReminder]] = None
        # An additional tracking ID for the appointment, if the appointment has been created directly by the customer on the scheduling page, as opposed to by a staff member on the behalf of the customer.
        self._self_service_appointment_id: Optional[str] = None
        # The ID of the bookingService associated with this appointment.
        self._service_id: Optional[str] = None
        # The location where the service is delivered.
        self._service_location: Optional[location.Location] = None
        # The name of the bookingService associated with this appointment.This property is optional when creating a new appointment. If not specified, it is computed from the service associated with the appointment by the serviceId property.
        self._service_name: Optional[str] = None
        # Notes from a bookingStaffMember. The value of this property is available only when reading this bookingAppointment by its ID.
        self._service_notes: Optional[str] = None
        # True indicates SMS notifications will be sent to the customers for the appointment. Default value is false.
        self._sms_notifications_enabled: Optional[bool] = None
        # The ID of each bookingStaffMember who is scheduled in this appointment.
        self._staff_member_ids: Optional[List[str]] = None
        # The start property
        self._start: Optional[date_time_time_zone.DateTimeTimeZone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingAppointment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingAppointment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BookingAppointment()
    
    @property
    def customer_email_address(self,) -> Optional[str]:
        """
        Gets the customerEmailAddress property value. The SMTP address of the bookingCustomer who is booking the appointment.
        Returns: Optional[str]
        """
        return self._customer_email_address
    
    @customer_email_address.setter
    def customer_email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the customerEmailAddress property value. The SMTP address of the bookingCustomer who is booking the appointment.
        Args:
            value: Value to set for the customerEmailAddress property.
        """
        self._customer_email_address = value
    
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
            value: Value to set for the customerId property.
        """
        self._customer_id = value
    
    @property
    def customer_location(self,) -> Optional[location.Location]:
        """
        Gets the customerLocation property value. Represents location information for the bookingCustomer who is booking the appointment.
        Returns: Optional[location.Location]
        """
        return self._customer_location
    
    @customer_location.setter
    def customer_location(self,value: Optional[location.Location] = None) -> None:
        """
        Sets the customerLocation property value. Represents location information for the bookingCustomer who is booking the appointment.
        Args:
            value: Value to set for the customerLocation property.
        """
        self._customer_location = value
    
    @property
    def customer_name(self,) -> Optional[str]:
        """
        Gets the customerName property value. The customer's name.
        Returns: Optional[str]
        """
        return self._customer_name
    
    @customer_name.setter
    def customer_name(self,value: Optional[str] = None) -> None:
        """
        Sets the customerName property value. The customer's name.
        Args:
            value: Value to set for the customerName property.
        """
        self._customer_name = value
    
    @property
    def customer_notes(self,) -> Optional[str]:
        """
        Gets the customerNotes property value. Notes from the customer associated with this appointment. You can get the value only when reading this bookingAppointment by its ID.  You can set this property only when initially creating an appointment with a new customer. After that point, the value is computed from the customer represented by customerId.
        Returns: Optional[str]
        """
        return self._customer_notes
    
    @customer_notes.setter
    def customer_notes(self,value: Optional[str] = None) -> None:
        """
        Sets the customerNotes property value. Notes from the customer associated with this appointment. You can get the value only when reading this bookingAppointment by its ID.  You can set this property only when initially creating an appointment with a new customer. After that point, the value is computed from the customer represented by customerId.
        Args:
            value: Value to set for the customerNotes property.
        """
        self._customer_notes = value
    
    @property
    def customer_phone(self,) -> Optional[str]:
        """
        Gets the customerPhone property value. The customer's phone number.
        Returns: Optional[str]
        """
        return self._customer_phone
    
    @customer_phone.setter
    def customer_phone(self,value: Optional[str] = None) -> None:
        """
        Sets the customerPhone property value. The customer's phone number.
        Args:
            value: Value to set for the customerPhone property.
        """
        self._customer_phone = value
    
    @property
    def customers(self,) -> Optional[List[booking_customer_information_base.BookingCustomerInformationBase]]:
        """
        Gets the customers property value. A collection of the customer properties for an appointment. An appointment will contain a list of customer information and each unit will indicate the properties of a customer who is part of that appointment. Optional.
        Returns: Optional[List[booking_customer_information_base.BookingCustomerInformationBase]]
        """
        return self._customers
    
    @customers.setter
    def customers(self,value: Optional[List[booking_customer_information_base.BookingCustomerInformationBase]] = None) -> None:
        """
        Sets the customers property value. A collection of the customer properties for an appointment. An appointment will contain a list of customer information and each unit will indicate the properties of a customer who is part of that appointment. Optional.
        Args:
            value: Value to set for the customers property.
        """
        self._customers = value
    
    @property
    def customer_time_zone(self,) -> Optional[str]:
        """
        Gets the customerTimeZone property value. The time zone of the customer. For a list of possible values, see dateTimeTimeZone.
        Returns: Optional[str]
        """
        return self._customer_time_zone
    
    @customer_time_zone.setter
    def customer_time_zone(self,value: Optional[str] = None) -> None:
        """
        Sets the customerTimeZone property value. The time zone of the customer. For a list of possible values, see dateTimeTimeZone.
        Args:
            value: Value to set for the customerTimeZone property.
        """
        self._customer_time_zone = value
    
    @property
    def duration(self,) -> Optional[Timedelta]:
        """
        Gets the duration property value. The length of the appointment, denoted in ISO8601 format.
        Returns: Optional[Timedelta]
        """
        return self._duration
    
    @duration.setter
    def duration(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the duration property value. The length of the appointment, denoted in ISO8601 format.
        Args:
            value: Value to set for the duration property.
        """
        self._duration = value
    
    @property
    def end(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the end property value. The end property
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._end
    
    @end.setter
    def end(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the end property value. The end property
        Args:
            value: Value to set for the end property.
        """
        self._end = value
    
    @property
    def filled_attendees_count(self,) -> Optional[int]:
        """
        Gets the filledAttendeesCount property value. The current number of customers in the appointment.
        Returns: Optional[int]
        """
        return self._filled_attendees_count
    
    @filled_attendees_count.setter
    def filled_attendees_count(self,value: Optional[int] = None) -> None:
        """
        Sets the filledAttendeesCount property value. The current number of customers in the appointment.
        Args:
            value: Value to set for the filledAttendeesCount property.
        """
        self._filled_attendees_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "additional_information": lambda n : setattr(self, 'additional_information', n.get_str_value()),
            "anonymous_join_web_url": lambda n : setattr(self, 'anonymous_join_web_url', n.get_str_value()),
            "customer_email_address": lambda n : setattr(self, 'customer_email_address', n.get_str_value()),
            "customer_id": lambda n : setattr(self, 'customer_id', n.get_str_value()),
            "customer_location": lambda n : setattr(self, 'customer_location', n.get_object_value(location.Location)),
            "customer_name": lambda n : setattr(self, 'customer_name', n.get_str_value()),
            "customer_notes": lambda n : setattr(self, 'customer_notes', n.get_str_value()),
            "customer_phone": lambda n : setattr(self, 'customer_phone', n.get_str_value()),
            "customers": lambda n : setattr(self, 'customers', n.get_collection_of_object_values(booking_customer_information_base.BookingCustomerInformationBase)),
            "customer_time_zone": lambda n : setattr(self, 'customer_time_zone', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_object_value(Timedelta)),
            "end": lambda n : setattr(self, 'end', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "filled_attendees_count": lambda n : setattr(self, 'filled_attendees_count', n.get_int_value()),
            "invoice_amount": lambda n : setattr(self, 'invoice_amount', n.get_float_value()),
            "invoice_date": lambda n : setattr(self, 'invoice_date', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "invoice_id": lambda n : setattr(self, 'invoice_id', n.get_str_value()),
            "invoice_status": lambda n : setattr(self, 'invoice_status', n.get_enum_value(booking_invoice_status.BookingInvoiceStatus)),
            "invoice_url": lambda n : setattr(self, 'invoice_url', n.get_str_value()),
            "is_location_online": lambda n : setattr(self, 'is_location_online', n.get_bool_value()),
            "join_web_url": lambda n : setattr(self, 'join_web_url', n.get_str_value()),
            "maximum_attendees_count": lambda n : setattr(self, 'maximum_attendees_count', n.get_int_value()),
            "online_meeting_url": lambda n : setattr(self, 'online_meeting_url', n.get_str_value()),
            "opt_out_of_customer_email": lambda n : setattr(self, 'opt_out_of_customer_email', n.get_bool_value()),
            "post_buffer": lambda n : setattr(self, 'post_buffer', n.get_object_value(Timedelta)),
            "pre_buffer": lambda n : setattr(self, 'pre_buffer', n.get_object_value(Timedelta)),
            "price": lambda n : setattr(self, 'price', n.get_float_value()),
            "price_type": lambda n : setattr(self, 'price_type', n.get_enum_value(booking_price_type.BookingPriceType)),
            "reminders": lambda n : setattr(self, 'reminders', n.get_collection_of_object_values(booking_reminder.BookingReminder)),
            "self_service_appointment_id": lambda n : setattr(self, 'self_service_appointment_id', n.get_str_value()),
            "service_id": lambda n : setattr(self, 'service_id', n.get_str_value()),
            "service_location": lambda n : setattr(self, 'service_location', n.get_object_value(location.Location)),
            "service_name": lambda n : setattr(self, 'service_name', n.get_str_value()),
            "service_notes": lambda n : setattr(self, 'service_notes', n.get_str_value()),
            "sms_notifications_enabled": lambda n : setattr(self, 'sms_notifications_enabled', n.get_bool_value()),
            "staff_member_ids": lambda n : setattr(self, 'staff_member_ids', n.get_collection_of_primitive_values(str)),
            "start": lambda n : setattr(self, 'start', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def invoice_amount(self,) -> Optional[float]:
        """
        Gets the invoiceAmount property value. The billed amount on the invoice.
        Returns: Optional[float]
        """
        return self._invoice_amount
    
    @invoice_amount.setter
    def invoice_amount(self,value: Optional[float] = None) -> None:
        """
        Sets the invoiceAmount property value. The billed amount on the invoice.
        Args:
            value: Value to set for the invoiceAmount property.
        """
        self._invoice_amount = value
    
    @property
    def invoice_date(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the invoiceDate property value. The date, time, and time zone of the invoice for this appointment.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._invoice_date
    
    @invoice_date.setter
    def invoice_date(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the invoiceDate property value. The date, time, and time zone of the invoice for this appointment.
        Args:
            value: Value to set for the invoiceDate property.
        """
        self._invoice_date = value
    
    @property
    def invoice_id(self,) -> Optional[str]:
        """
        Gets the invoiceId property value. The ID of the invoice.
        Returns: Optional[str]
        """
        return self._invoice_id
    
    @invoice_id.setter
    def invoice_id(self,value: Optional[str] = None) -> None:
        """
        Sets the invoiceId property value. The ID of the invoice.
        Args:
            value: Value to set for the invoiceId property.
        """
        self._invoice_id = value
    
    @property
    def invoice_status(self,) -> Optional[booking_invoice_status.BookingInvoiceStatus]:
        """
        Gets the invoiceStatus property value. The invoiceStatus property
        Returns: Optional[booking_invoice_status.BookingInvoiceStatus]
        """
        return self._invoice_status
    
    @invoice_status.setter
    def invoice_status(self,value: Optional[booking_invoice_status.BookingInvoiceStatus] = None) -> None:
        """
        Sets the invoiceStatus property value. The invoiceStatus property
        Args:
            value: Value to set for the invoiceStatus property.
        """
        self._invoice_status = value
    
    @property
    def invoice_url(self,) -> Optional[str]:
        """
        Gets the invoiceUrl property value. The URL of the invoice in Microsoft Bookings.
        Returns: Optional[str]
        """
        return self._invoice_url
    
    @invoice_url.setter
    def invoice_url(self,value: Optional[str] = None) -> None:
        """
        Sets the invoiceUrl property value. The URL of the invoice in Microsoft Bookings.
        Args:
            value: Value to set for the invoiceUrl property.
        """
        self._invoice_url = value
    
    @property
    def is_location_online(self,) -> Optional[bool]:
        """
        Gets the isLocationOnline property value. True indicates that the appointment will be held online. Default value is false.
        Returns: Optional[bool]
        """
        return self._is_location_online
    
    @is_location_online.setter
    def is_location_online(self,value: Optional[bool] = None) -> None:
        """
        Sets the isLocationOnline property value. True indicates that the appointment will be held online. Default value is false.
        Args:
            value: Value to set for the isLocationOnline property.
        """
        self._is_location_online = value
    
    @property
    def join_web_url(self,) -> Optional[str]:
        """
        Gets the joinWebUrl property value. The URL of the online meeting for the appointment.
        Returns: Optional[str]
        """
        return self._join_web_url
    
    @join_web_url.setter
    def join_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the joinWebUrl property value. The URL of the online meeting for the appointment.
        Args:
            value: Value to set for the joinWebUrl property.
        """
        self._join_web_url = value
    
    @property
    def maximum_attendees_count(self,) -> Optional[int]:
        """
        Gets the maximumAttendeesCount property value. The maximum number of customers allowed in an appointment. If maximumAttendeesCount of the service is greater than 1, pass valid customer IDs while creating or updating an appointment. To create a customer, use the Create bookingCustomer operation.
        Returns: Optional[int]
        """
        return self._maximum_attendees_count
    
    @maximum_attendees_count.setter
    def maximum_attendees_count(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumAttendeesCount property value. The maximum number of customers allowed in an appointment. If maximumAttendeesCount of the service is greater than 1, pass valid customer IDs while creating or updating an appointment. To create a customer, use the Create bookingCustomer operation.
        Args:
            value: Value to set for the maximumAttendeesCount property.
        """
        self._maximum_attendees_count = value
    
    @property
    def online_meeting_url(self,) -> Optional[str]:
        """
        Gets the onlineMeetingUrl property value. The onlineMeetingUrl property
        Returns: Optional[str]
        """
        return self._online_meeting_url
    
    @online_meeting_url.setter
    def online_meeting_url(self,value: Optional[str] = None) -> None:
        """
        Sets the onlineMeetingUrl property value. The onlineMeetingUrl property
        Args:
            value: Value to set for the onlineMeetingUrl property.
        """
        self._online_meeting_url = value
    
    @property
    def opt_out_of_customer_email(self,) -> Optional[bool]:
        """
        Gets the optOutOfCustomerEmail property value. True indicates that the bookingCustomer for this appointment does not wish to receive a confirmation for this appointment.
        Returns: Optional[bool]
        """
        return self._opt_out_of_customer_email
    
    @opt_out_of_customer_email.setter
    def opt_out_of_customer_email(self,value: Optional[bool] = None) -> None:
        """
        Sets the optOutOfCustomerEmail property value. True indicates that the bookingCustomer for this appointment does not wish to receive a confirmation for this appointment.
        Args:
            value: Value to set for the optOutOfCustomerEmail property.
        """
        self._opt_out_of_customer_email = value
    
    @property
    def post_buffer(self,) -> Optional[Timedelta]:
        """
        Gets the postBuffer property value. The amount of time to reserve after the appointment ends, for cleaning up, as an example. The value is expressed in ISO8601 format.
        Returns: Optional[Timedelta]
        """
        return self._post_buffer
    
    @post_buffer.setter
    def post_buffer(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the postBuffer property value. The amount of time to reserve after the appointment ends, for cleaning up, as an example. The value is expressed in ISO8601 format.
        Args:
            value: Value to set for the postBuffer property.
        """
        self._post_buffer = value
    
    @property
    def pre_buffer(self,) -> Optional[Timedelta]:
        """
        Gets the preBuffer property value. The amount of time to reserve before the appointment begins, for preparation, as an example. The value is expressed in ISO8601 format.
        Returns: Optional[Timedelta]
        """
        return self._pre_buffer
    
    @pre_buffer.setter
    def pre_buffer(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the preBuffer property value. The amount of time to reserve before the appointment begins, for preparation, as an example. The value is expressed in ISO8601 format.
        Args:
            value: Value to set for the preBuffer property.
        """
        self._pre_buffer = value
    
    @property
    def price(self,) -> Optional[float]:
        """
        Gets the price property value. The regular price for an appointment for the specified bookingService.
        Returns: Optional[float]
        """
        return self._price
    
    @price.setter
    def price(self,value: Optional[float] = None) -> None:
        """
        Sets the price property value. The regular price for an appointment for the specified bookingService.
        Args:
            value: Value to set for the price property.
        """
        self._price = value
    
    @property
    def price_type(self,) -> Optional[booking_price_type.BookingPriceType]:
        """
        Gets the priceType property value. Represents the type of pricing of a booking service.
        Returns: Optional[booking_price_type.BookingPriceType]
        """
        return self._price_type
    
    @price_type.setter
    def price_type(self,value: Optional[booking_price_type.BookingPriceType] = None) -> None:
        """
        Sets the priceType property value. Represents the type of pricing of a booking service.
        Args:
            value: Value to set for the priceType property.
        """
        self._price_type = value
    
    @property
    def reminders(self,) -> Optional[List[booking_reminder.BookingReminder]]:
        """
        Gets the reminders property value. The collection of customer reminders sent for this appointment. The value of this property is available only when reading this bookingAppointment by its ID.
        Returns: Optional[List[booking_reminder.BookingReminder]]
        """
        return self._reminders
    
    @reminders.setter
    def reminders(self,value: Optional[List[booking_reminder.BookingReminder]] = None) -> None:
        """
        Sets the reminders property value. The collection of customer reminders sent for this appointment. The value of this property is available only when reading this bookingAppointment by its ID.
        Args:
            value: Value to set for the reminders property.
        """
        self._reminders = value
    
    @property
    def self_service_appointment_id(self,) -> Optional[str]:
        """
        Gets the selfServiceAppointmentId property value. An additional tracking ID for the appointment, if the appointment has been created directly by the customer on the scheduling page, as opposed to by a staff member on the behalf of the customer.
        Returns: Optional[str]
        """
        return self._self_service_appointment_id
    
    @self_service_appointment_id.setter
    def self_service_appointment_id(self,value: Optional[str] = None) -> None:
        """
        Sets the selfServiceAppointmentId property value. An additional tracking ID for the appointment, if the appointment has been created directly by the customer on the scheduling page, as opposed to by a staff member on the behalf of the customer.
        Args:
            value: Value to set for the selfServiceAppointmentId property.
        """
        self._self_service_appointment_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("additionalInformation", self.additional_information)
        writer.write_str_value("anonymousJoinWebUrl", self.anonymous_join_web_url)
        writer.write_str_value("customerEmailAddress", self.customer_email_address)
        writer.write_str_value("customerId", self.customer_id)
        writer.write_object_value("customerLocation", self.customer_location)
        writer.write_str_value("customerName", self.customer_name)
        writer.write_str_value("customerNotes", self.customer_notes)
        writer.write_str_value("customerPhone", self.customer_phone)
        writer.write_collection_of_object_values("customers", self.customers)
        writer.write_str_value("customerTimeZone", self.customer_time_zone)
        writer.write_object_value("end", self.end)
        writer.write_float_value("invoiceAmount", self.invoice_amount)
        writer.write_object_value("invoiceDate", self.invoice_date)
        writer.write_str_value("invoiceId", self.invoice_id)
        writer.write_enum_value("invoiceStatus", self.invoice_status)
        writer.write_str_value("invoiceUrl", self.invoice_url)
        writer.write_bool_value("isLocationOnline", self.is_location_online)
        writer.write_str_value("joinWebUrl", self.join_web_url)
        writer.write_int_value("maximumAttendeesCount", self.maximum_attendees_count)
        writer.write_str_value("onlineMeetingUrl", self.online_meeting_url)
        writer.write_bool_value("optOutOfCustomerEmail", self.opt_out_of_customer_email)
        writer.write_object_value("postBuffer", self.post_buffer)
        writer.write_object_value("preBuffer", self.pre_buffer)
        writer.write_float_value("price", self.price)
        writer.write_enum_value("priceType", self.price_type)
        writer.write_collection_of_object_values("reminders", self.reminders)
        writer.write_str_value("selfServiceAppointmentId", self.self_service_appointment_id)
        writer.write_str_value("serviceId", self.service_id)
        writer.write_object_value("serviceLocation", self.service_location)
        writer.write_str_value("serviceName", self.service_name)
        writer.write_str_value("serviceNotes", self.service_notes)
        writer.write_bool_value("smsNotificationsEnabled", self.sms_notifications_enabled)
        writer.write_collection_of_primitive_values("staffMemberIds", self.staff_member_ids)
        writer.write_object_value("start", self.start)
    
    @property
    def service_id(self,) -> Optional[str]:
        """
        Gets the serviceId property value. The ID of the bookingService associated with this appointment.
        Returns: Optional[str]
        """
        return self._service_id
    
    @service_id.setter
    def service_id(self,value: Optional[str] = None) -> None:
        """
        Sets the serviceId property value. The ID of the bookingService associated with this appointment.
        Args:
            value: Value to set for the serviceId property.
        """
        self._service_id = value
    
    @property
    def service_location(self,) -> Optional[location.Location]:
        """
        Gets the serviceLocation property value. The location where the service is delivered.
        Returns: Optional[location.Location]
        """
        return self._service_location
    
    @service_location.setter
    def service_location(self,value: Optional[location.Location] = None) -> None:
        """
        Sets the serviceLocation property value. The location where the service is delivered.
        Args:
            value: Value to set for the serviceLocation property.
        """
        self._service_location = value
    
    @property
    def service_name(self,) -> Optional[str]:
        """
        Gets the serviceName property value. The name of the bookingService associated with this appointment.This property is optional when creating a new appointment. If not specified, it is computed from the service associated with the appointment by the serviceId property.
        Returns: Optional[str]
        """
        return self._service_name
    
    @service_name.setter
    def service_name(self,value: Optional[str] = None) -> None:
        """
        Sets the serviceName property value. The name of the bookingService associated with this appointment.This property is optional when creating a new appointment. If not specified, it is computed from the service associated with the appointment by the serviceId property.
        Args:
            value: Value to set for the serviceName property.
        """
        self._service_name = value
    
    @property
    def service_notes(self,) -> Optional[str]:
        """
        Gets the serviceNotes property value. Notes from a bookingStaffMember. The value of this property is available only when reading this bookingAppointment by its ID.
        Returns: Optional[str]
        """
        return self._service_notes
    
    @service_notes.setter
    def service_notes(self,value: Optional[str] = None) -> None:
        """
        Sets the serviceNotes property value. Notes from a bookingStaffMember. The value of this property is available only when reading this bookingAppointment by its ID.
        Args:
            value: Value to set for the serviceNotes property.
        """
        self._service_notes = value
    
    @property
    def sms_notifications_enabled(self,) -> Optional[bool]:
        """
        Gets the smsNotificationsEnabled property value. True indicates SMS notifications will be sent to the customers for the appointment. Default value is false.
        Returns: Optional[bool]
        """
        return self._sms_notifications_enabled
    
    @sms_notifications_enabled.setter
    def sms_notifications_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the smsNotificationsEnabled property value. True indicates SMS notifications will be sent to the customers for the appointment. Default value is false.
        Args:
            value: Value to set for the smsNotificationsEnabled property.
        """
        self._sms_notifications_enabled = value
    
    @property
    def staff_member_ids(self,) -> Optional[List[str]]:
        """
        Gets the staffMemberIds property value. The ID of each bookingStaffMember who is scheduled in this appointment.
        Returns: Optional[List[str]]
        """
        return self._staff_member_ids
    
    @staff_member_ids.setter
    def staff_member_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the staffMemberIds property value. The ID of each bookingStaffMember who is scheduled in this appointment.
        Args:
            value: Value to set for the staffMemberIds property.
        """
        self._staff_member_ids = value
    
    @property
    def start(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the start property value. The start property
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._start
    
    @start.setter
    def start(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the start property value. The start property
        Args:
            value: Value to set for the start property.
        """
        self._start = value
    

