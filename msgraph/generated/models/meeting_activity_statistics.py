from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import activity_statistics

from . import activity_statistics

class MeetingActivityStatistics(activity_statistics.ActivityStatistics):
    def __init__(self,) -> None:
        """
        Instantiates a new MeetingActivityStatistics and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.meetingActivityStatistics"
        # Time spent on meetings outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        self._after_hours: Optional[timedelta] = None
        # Time spent in conflicting meetings (meetings that overlap with other meetings that the person accepted and where the person’s status is set to Busy). The value is represented in ISO 8601 format for durations.
        self._conflicting: Optional[timedelta] = None
        # Time spent in long meetings (more than an hour in duration). The value is represented in ISO 8601 format for durations.
        self._long: Optional[timedelta] = None
        # Time spent in meetings where the person was multitasking (read/sent more than a minimum number of emails and/or sent more than a minimum number of messages in Teams or in Skype for Business). The value is represented in ISO 8601 format for durations.
        self._multitasking: Optional[timedelta] = None
        # Time spent in meetings organized by the user. The value is represented in ISO 8601 format for durations.
        self._organized: Optional[timedelta] = None
        # Time spent on recurring meetings. The value is represented in ISO 8601 format for durations.
        self._recurring: Optional[timedelta] = None
    
    @property
    def after_hours(self,) -> Optional[timedelta]:
        """
        Gets the afterHours property value. Time spent on meetings outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        Returns: Optional[timedelta]
        """
        return self._after_hours
    
    @after_hours.setter
    def after_hours(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the afterHours property value. Time spent on meetings outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the after_hours property.
        """
        self._after_hours = value
    
    @property
    def conflicting(self,) -> Optional[timedelta]:
        """
        Gets the conflicting property value. Time spent in conflicting meetings (meetings that overlap with other meetings that the person accepted and where the person’s status is set to Busy). The value is represented in ISO 8601 format for durations.
        Returns: Optional[timedelta]
        """
        return self._conflicting
    
    @conflicting.setter
    def conflicting(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the conflicting property value. Time spent in conflicting meetings (meetings that overlap with other meetings that the person accepted and where the person’s status is set to Busy). The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the conflicting property.
        """
        self._conflicting = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingActivityStatistics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingActivityStatistics
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MeetingActivityStatistics()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import activity_statistics

        fields: Dict[str, Callable[[Any], None]] = {
            "afterHours": lambda n : setattr(self, 'after_hours', n.get_timedelta_value()),
            "conflicting": lambda n : setattr(self, 'conflicting', n.get_timedelta_value()),
            "long": lambda n : setattr(self, 'long', n.get_timedelta_value()),
            "multitasking": lambda n : setattr(self, 'multitasking', n.get_timedelta_value()),
            "organized": lambda n : setattr(self, 'organized', n.get_timedelta_value()),
            "recurring": lambda n : setattr(self, 'recurring', n.get_timedelta_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def long(self,) -> Optional[timedelta]:
        """
        Gets the long property value. Time spent in long meetings (more than an hour in duration). The value is represented in ISO 8601 format for durations.
        Returns: Optional[timedelta]
        """
        return self._long
    
    @long.setter
    def long(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the long property value. Time spent in long meetings (more than an hour in duration). The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the long property.
        """
        self._long = value
    
    @property
    def multitasking(self,) -> Optional[timedelta]:
        """
        Gets the multitasking property value. Time spent in meetings where the person was multitasking (read/sent more than a minimum number of emails and/or sent more than a minimum number of messages in Teams or in Skype for Business). The value is represented in ISO 8601 format for durations.
        Returns: Optional[timedelta]
        """
        return self._multitasking
    
    @multitasking.setter
    def multitasking(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the multitasking property value. Time spent in meetings where the person was multitasking (read/sent more than a minimum number of emails and/or sent more than a minimum number of messages in Teams or in Skype for Business). The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the multitasking property.
        """
        self._multitasking = value
    
    @property
    def organized(self,) -> Optional[timedelta]:
        """
        Gets the organized property value. Time spent in meetings organized by the user. The value is represented in ISO 8601 format for durations.
        Returns: Optional[timedelta]
        """
        return self._organized
    
    @organized.setter
    def organized(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the organized property value. Time spent in meetings organized by the user. The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the organized property.
        """
        self._organized = value
    
    @property
    def recurring(self,) -> Optional[timedelta]:
        """
        Gets the recurring property value. Time spent on recurring meetings. The value is represented in ISO 8601 format for durations.
        Returns: Optional[timedelta]
        """
        return self._recurring
    
    @recurring.setter
    def recurring(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the recurring property value. Time spent on recurring meetings. The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the recurring property.
        """
        self._recurring = value
    
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
        writer.write_timedelta_value("conflicting", self.conflicting)
        writer.write_timedelta_value("long", self.long)
        writer.write_timedelta_value("multitasking", self.multitasking)
        writer.write_timedelta_value("organized", self.organized)
        writer.write_timedelta_value("recurring", self.recurring)
    

