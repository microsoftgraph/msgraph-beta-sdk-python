from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

activity_statistics = lazy_import('msgraph.generated.models.activity_statistics')

class EmailActivityStatistics(activity_statistics.ActivityStatistics):
    @property
    def after_hours(self,) -> Optional[Timedelta]:
        """
        Gets the afterHours property value. Total hours spent on email outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        Returns: Optional[Timedelta]
        """
        return self._after_hours
    
    @after_hours.setter
    def after_hours(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the afterHours property value. Total hours spent on email outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the afterHours property.
        """
        self._after_hours = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new EmailActivityStatistics and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.emailActivityStatistics"
        # Total hours spent on email outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        self._after_hours: Optional[Timedelta] = None
        # Total hours spent reading email. The value is represented in ISO 8601 format for durations.
        self._read_email: Optional[Timedelta] = None
        # Total hours spent writing and sending email. The value is represented in ISO 8601 format for durations.
        self._sent_email: Optional[Timedelta] = None
    
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
        fields = {
            "after_hours": lambda n : setattr(self, 'after_hours', n.get_object_value(Timedelta)),
            "read_email": lambda n : setattr(self, 'read_email', n.get_object_value(Timedelta)),
            "sent_email": lambda n : setattr(self, 'sent_email', n.get_object_value(Timedelta)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def read_email(self,) -> Optional[Timedelta]:
        """
        Gets the readEmail property value. Total hours spent reading email. The value is represented in ISO 8601 format for durations.
        Returns: Optional[Timedelta]
        """
        return self._read_email
    
    @read_email.setter
    def read_email(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the readEmail property value. Total hours spent reading email. The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the readEmail property.
        """
        self._read_email = value
    
    @property
    def sent_email(self,) -> Optional[Timedelta]:
        """
        Gets the sentEmail property value. Total hours spent writing and sending email. The value is represented in ISO 8601 format for durations.
        Returns: Optional[Timedelta]
        """
        return self._sent_email
    
    @sent_email.setter
    def sent_email(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the sentEmail property value. Total hours spent writing and sending email. The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the sentEmail property.
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
        writer.write_object_value("afterHours", self.after_hours)
        writer.write_object_value("readEmail", self.read_email)
        writer.write_object_value("sentEmail", self.sent_email)
    

