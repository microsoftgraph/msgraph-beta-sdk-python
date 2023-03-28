from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attendance_interval, entity, identity

from . import entity

class AttendanceRecord(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new attendanceRecord and sets the default values.
        """
        super().__init__()
        # List of time periods between joining and leaving a meeting.
        self._attendance_intervals: Optional[List[attendance_interval.AttendanceInterval]] = None
        # Email address of the user associated with this atttendance record.
        self._email_address: Optional[str] = None
        # Identity of the user associated with this atttendance record. The specific type will be one of the following derived types of identity, depending on the type of the user: communicationsUserIdentity, azureCommunicationServicesUserIdentity.
        self._identity: Optional[identity.Identity] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Unique identifier of a meetingRegistrant. Presents when the participant has registered for the meeting.
        self._registrant_id: Optional[str] = None
        # Role of the attendee. Possible values are: None, Attendee, Presenter, and Organizer.
        self._role: Optional[str] = None
        # Total duration of the attendances in seconds.
        self._total_attendance_in_seconds: Optional[int] = None
    
    @property
    def attendance_intervals(self,) -> Optional[List[attendance_interval.AttendanceInterval]]:
        """
        Gets the attendanceIntervals property value. List of time periods between joining and leaving a meeting.
        Returns: Optional[List[attendance_interval.AttendanceInterval]]
        """
        return self._attendance_intervals
    
    @attendance_intervals.setter
    def attendance_intervals(self,value: Optional[List[attendance_interval.AttendanceInterval]] = None) -> None:
        """
        Sets the attendanceIntervals property value. List of time periods between joining and leaving a meeting.
        Args:
            value: Value to set for the attendance_intervals property.
        """
        self._attendance_intervals = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttendanceRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttendanceRecord
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttendanceRecord()
    
    @property
    def email_address(self,) -> Optional[str]:
        """
        Gets the emailAddress property value. Email address of the user associated with this atttendance record.
        Returns: Optional[str]
        """
        return self._email_address
    
    @email_address.setter
    def email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the emailAddress property value. Email address of the user associated with this atttendance record.
        Args:
            value: Value to set for the email_address property.
        """
        self._email_address = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attendance_interval, entity, identity

        fields: Dict[str, Callable[[Any], None]] = {
            "attendanceIntervals": lambda n : setattr(self, 'attendance_intervals', n.get_collection_of_object_values(attendance_interval.AttendanceInterval)),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(identity.Identity)),
            "registrantId": lambda n : setattr(self, 'registrant_id', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_str_value()),
            "totalAttendanceInSeconds": lambda n : setattr(self, 'total_attendance_in_seconds', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity(self,) -> Optional[identity.Identity]:
        """
        Gets the identity property value. Identity of the user associated with this atttendance record. The specific type will be one of the following derived types of identity, depending on the type of the user: communicationsUserIdentity, azureCommunicationServicesUserIdentity.
        Returns: Optional[identity.Identity]
        """
        return self._identity
    
    @identity.setter
    def identity(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the identity property value. Identity of the user associated with this atttendance record. The specific type will be one of the following derived types of identity, depending on the type of the user: communicationsUserIdentity, azureCommunicationServicesUserIdentity.
        Args:
            value: Value to set for the identity property.
        """
        self._identity = value
    
    @property
    def registrant_id(self,) -> Optional[str]:
        """
        Gets the registrantId property value. Unique identifier of a meetingRegistrant. Presents when the participant has registered for the meeting.
        Returns: Optional[str]
        """
        return self._registrant_id
    
    @registrant_id.setter
    def registrant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the registrantId property value. Unique identifier of a meetingRegistrant. Presents when the participant has registered for the meeting.
        Args:
            value: Value to set for the registrant_id property.
        """
        self._registrant_id = value
    
    @property
    def role(self,) -> Optional[str]:
        """
        Gets the role property value. Role of the attendee. Possible values are: None, Attendee, Presenter, and Organizer.
        Returns: Optional[str]
        """
        return self._role
    
    @role.setter
    def role(self,value: Optional[str] = None) -> None:
        """
        Sets the role property value. Role of the attendee. Possible values are: None, Attendee, Presenter, and Organizer.
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
        writer.write_collection_of_object_values("attendanceIntervals", self.attendance_intervals)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_object_value("identity", self.identity)
        writer.write_str_value("registrantId", self.registrant_id)
        writer.write_str_value("role", self.role)
        writer.write_int_value("totalAttendanceInSeconds", self.total_attendance_in_seconds)
    
    @property
    def total_attendance_in_seconds(self,) -> Optional[int]:
        """
        Gets the totalAttendanceInSeconds property value. Total duration of the attendances in seconds.
        Returns: Optional[int]
        """
        return self._total_attendance_in_seconds
    
    @total_attendance_in_seconds.setter
    def total_attendance_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the totalAttendanceInSeconds property value. Total duration of the attendances in seconds.
        Args:
            value: Value to set for the total_attendance_in_seconds property.
        """
        self._total_attendance_in_seconds = value
    

