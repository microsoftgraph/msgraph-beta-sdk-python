from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import activity_statistics

from . import activity_statistics

class EmailActivityStatistics(activity_statistics.ActivityStatistics):
    def __init__(self,) -> None:
        """
        Instantiates a new EmailActivityStatistics and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.emailActivityStatistics"
        # Total hours spent on email outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        self._after_hours: Optional[timedelta] = None
        # Total hours spent reading email. The value is represented in ISO 8601 format for durations.
        self._read_email: Optional[timedelta] = None
        # Total hours spent writing and sending email. The value is represented in ISO 8601 format for durations.
        self._sent_email: Optional[timedelta] = None
    
    @property
    def after_hours(self,) -> Optional[timedelta]:
        """
        Gets the afterHours property value. Total hours spent on email outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        Returns: Optional[timedelta]
        """
        return self._after_hours
    
    @after_hours.setter
    def after_hours(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the afterHours property value. Total hours spent on email outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the after_hours property.
        """
        self._after_hours = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmailActivityStatistics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmailActivityStatistics
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EmailActivityStatistics()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import activity_statistics

        fields: Dict[str, Callable[[Any], None]] = {
            "afterHours": lambda n : setattr(self, 'after_hours', n.get_timedelta_value()),
            "readEmail": lambda n : setattr(self, 'read_email', n.get_timedelta_value()),
            "sentEmail": lambda n : setattr(self, 'sent_email', n.get_timedelta_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def read_email(self,) -> Optional[timedelta]:
        """
        Gets the readEmail property value. Total hours spent reading email. The value is represented in ISO 8601 format for durations.
        Returns: Optional[timedelta]
        """
        return self._read_email
    
    @read_email.setter
    def read_email(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the readEmail property value. Total hours spent reading email. The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the read_email property.
        """
        self._read_email = value
    
    @property
    def sent_email(self,) -> Optional[timedelta]:
        """
        Gets the sentEmail property value. Total hours spent writing and sending email. The value is represented in ISO 8601 format for durations.
        Returns: Optional[timedelta]
        """
        return self._sent_email
    
    @sent_email.setter
    def sent_email(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the sentEmail property value. Total hours spent writing and sending email. The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the sent_email property.
        """
        self._sent_email = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_timedelta_value("afterHours", self.after_hours)
        writer.write_timedelta_value("readEmail", self.read_email)
        writer.write_timedelta_value("sentEmail", self.sent_email)
    

