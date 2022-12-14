from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

booking_person = lazy_import('msgraph.generated.models.booking_person')
booking_staff_role = lazy_import('msgraph.generated.models.booking_staff_role')
booking_work_hours = lazy_import('msgraph.generated.models.booking_work_hours')

class BookingStaffMember(booking_person.BookingPerson):
    @property
    def availability_is_affected_by_personal_calendar(self,) -> Optional[bool]:
        """
        Gets the availabilityIsAffectedByPersonalCalendar property value. True means that if the staff member is a Microsoft 365 user, the Bookings API would verify the staff member's availability in their personal calendar in Microsoft 365, before making a booking.
        Returns: Optional[bool]
        """
        return self._availability_is_affected_by_personal_calendar
    
    @availability_is_affected_by_personal_calendar.setter
    def availability_is_affected_by_personal_calendar(self,value: Optional[bool] = None) -> None:
        """
        Sets the availabilityIsAffectedByPersonalCalendar property value. True means that if the staff member is a Microsoft 365 user, the Bookings API would verify the staff member's availability in their personal calendar in Microsoft 365, before making a booking.
        Args:
            value: Value to set for the availabilityIsAffectedByPersonalCalendar property.
        """
        self._availability_is_affected_by_personal_calendar = value
    
    @property
    def color_index(self,) -> Optional[int]:
        """
        Gets the colorIndex property value. Identifies a color to represent the staff member. The color corresponds to the color palette in the Staff details page in the Bookings app.
        Returns: Optional[int]
        """
        return self._color_index
    
    @color_index.setter
    def color_index(self,value: Optional[int] = None) -> None:
        """
        Sets the colorIndex property value. Identifies a color to represent the staff member. The color corresponds to the color palette in the Staff details page in the Bookings app.
        Args:
            value: Value to set for the colorIndex property.
        """
        self._color_index = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new BookingStaffMember and sets the default values.
        """
        super().__init__()
        # True means that if the staff member is a Microsoft 365 user, the Bookings API would verify the staff member's availability in their personal calendar in Microsoft 365, before making a booking.
        self._availability_is_affected_by_personal_calendar: Optional[bool] = None
        # Identifies a color to represent the staff member. The color corresponds to the color palette in the Staff details page in the Bookings app.
        self._color_index: Optional[int] = None
        # True indicates that a staff member will be notified via email when a booking assigned to them is created or changed.
        self._is_email_notification_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The role property
        self._role: Optional[booking_staff_role.BookingStaffRole] = None
        # The time zone of the staff member. For a list of possible values, see dateTimeTimeZone.
        self._time_zone: Optional[str] = None
        # True means the staff member's availability is as specified in the businessHours property of the business. False means the availability is determined by the staff member's workingHours property setting.
        self._use_business_hours: Optional[bool] = None
        # The range of hours each day of the week that the staff member is available for booking. By default, they are initialized to be the same as the businessHours property of the business.
        self._working_hours: Optional[List[booking_work_hours.BookingWorkHours]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingStaffMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingStaffMember
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BookingStaffMember()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "availability_is_affected_by_personal_calendar": lambda n : setattr(self, 'availability_is_affected_by_personal_calendar', n.get_bool_value()),
            "color_index": lambda n : setattr(self, 'color_index', n.get_int_value()),
            "is_email_notification_enabled": lambda n : setattr(self, 'is_email_notification_enabled', n.get_bool_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(booking_staff_role.BookingStaffRole)),
            "time_zone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
            "use_business_hours": lambda n : setattr(self, 'use_business_hours', n.get_bool_value()),
            "working_hours": lambda n : setattr(self, 'working_hours', n.get_collection_of_object_values(booking_work_hours.BookingWorkHours)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_email_notification_enabled(self,) -> Optional[bool]:
        """
        Gets the isEmailNotificationEnabled property value. True indicates that a staff member will be notified via email when a booking assigned to them is created or changed.
        Returns: Optional[bool]
        """
        return self._is_email_notification_enabled
    
    @is_email_notification_enabled.setter
    def is_email_notification_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEmailNotificationEnabled property value. True indicates that a staff member will be notified via email when a booking assigned to them is created or changed.
        Args:
            value: Value to set for the isEmailNotificationEnabled property.
        """
        self._is_email_notification_enabled = value
    
    @property
    def role(self,) -> Optional[booking_staff_role.BookingStaffRole]:
        """
        Gets the role property value. The role property
        Returns: Optional[booking_staff_role.BookingStaffRole]
        """
        return self._role
    
    @role.setter
    def role(self,value: Optional[booking_staff_role.BookingStaffRole] = None) -> None:
        """
        Sets the role property value. The role property
        Args:
            value: Value to set for the role property.
        """
        self._role = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("availabilityIsAffectedByPersonalCalendar", self.availability_is_affected_by_personal_calendar)
        writer.write_int_value("colorIndex", self.color_index)
        writer.write_bool_value("isEmailNotificationEnabled", self.is_email_notification_enabled)
        writer.write_enum_value("role", self.role)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_bool_value("useBusinessHours", self.use_business_hours)
        writer.write_collection_of_object_values("workingHours", self.working_hours)
    
    @property
    def time_zone(self,) -> Optional[str]:
        """
        Gets the timeZone property value. The time zone of the staff member. For a list of possible values, see dateTimeTimeZone.
        Returns: Optional[str]
        """
        return self._time_zone
    
    @time_zone.setter
    def time_zone(self,value: Optional[str] = None) -> None:
        """
        Sets the timeZone property value. The time zone of the staff member. For a list of possible values, see dateTimeTimeZone.
        Args:
            value: Value to set for the timeZone property.
        """
        self._time_zone = value
    
    @property
    def use_business_hours(self,) -> Optional[bool]:
        """
        Gets the useBusinessHours property value. True means the staff member's availability is as specified in the businessHours property of the business. False means the availability is determined by the staff member's workingHours property setting.
        Returns: Optional[bool]
        """
        return self._use_business_hours
    
    @use_business_hours.setter
    def use_business_hours(self,value: Optional[bool] = None) -> None:
        """
        Sets the useBusinessHours property value. True means the staff member's availability is as specified in the businessHours property of the business. False means the availability is determined by the staff member's workingHours property setting.
        Args:
            value: Value to set for the useBusinessHours property.
        """
        self._use_business_hours = value
    
    @property
    def working_hours(self,) -> Optional[List[booking_work_hours.BookingWorkHours]]:
        """
        Gets the workingHours property value. The range of hours each day of the week that the staff member is available for booking. By default, they are initialized to be the same as the businessHours property of the business.
        Returns: Optional[List[booking_work_hours.BookingWorkHours]]
        """
        return self._working_hours
    
    @working_hours.setter
    def working_hours(self,value: Optional[List[booking_work_hours.BookingWorkHours]] = None) -> None:
        """
        Sets the workingHours property value. The range of hours each day of the week that the staff member is available for booking. By default, they are initialized to be the same as the businessHours property of the business.
        Args:
            value: Value to set for the workingHours property.
        """
        self._working_hours = value
    

