from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

activity_statistics = lazy_import('msgraph.generated.models.activity_statistics')

class MeetingActivityStatistics(activity_statistics.ActivityStatistics):
    @property
    def after_hours(self,) -> Optional[Timedelta]:
        """
        Gets the afterHours property value. Time spent on meetings outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        Returns: Optional[Timedelta]
        """
        return self._after_hours
    
    @after_hours.setter
    def after_hours(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the afterHours property value. Time spent on meetings outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the afterHours property.
        """
        self._after_hours = value
    
    @property
    def conflicting(self,) -> Optional[Timedelta]:
        """
        Gets the conflicting property value. Time spent in conflicting meetings (meetings that overlap with other meetings that the person accepted and where the person’s status is set to Busy). The value is represented in ISO 8601 format for durations.
        Returns: Optional[Timedelta]
        """
        return self._conflicting
    
    @conflicting.setter
    def conflicting(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the conflicting property value. Time spent in conflicting meetings (meetings that overlap with other meetings that the person accepted and where the person’s status is set to Busy). The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the conflicting property.
        """
        self._conflicting = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new MeetingActivityStatistics and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.meetingActivityStatistics"
        # Time spent on meetings outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        self._after_hours: Optional[Timedelta] = None
        # Time spent in conflicting meetings (meetings that overlap with other meetings that the person accepted and where the person’s status is set to Busy). The value is represented in ISO 8601 format for durations.
        self._conflicting: Optional[Timedelta] = None
        # Time spent in long meetings (more than an hour in duration). The value is represented in ISO 8601 format for durations.
        self._long: Optional[Timedelta] = None
        # Time spent in meetings where the person was multitasking (read/sent more than a minimum number of emails and/or sent more than a minimum number of messages in Teams or in Skype for Business). The value is represented in ISO 8601 format for durations.
        self._multitasking: Optional[Timedelta] = None
        # Time spent in meetings organized by the user. The value is represented in ISO 8601 format for durations.
        self._organized: Optional[Timedelta] = None
        # Time spent on recurring meetings. The value is represented in ISO 8601 format for durations.
        self._recurring: Optional[Timedelta] = None
    
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
        fields = {
            "after_hours": lambda n : setattr(self, 'after_hours', n.get_object_value(Timedelta)),
            "conflicting": lambda n : setattr(self, 'conflicting', n.get_object_value(Timedelta)),
            "long": lambda n : setattr(self, 'long', n.get_object_value(Timedelta)),
            "multitasking": lambda n : setattr(self, 'multitasking', n.get_object_value(Timedelta)),
            "organized": lambda n : setattr(self, 'organized', n.get_object_value(Timedelta)),
            "recurring": lambda n : setattr(self, 'recurring', n.get_object_value(Timedelta)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def long(self,) -> Optional[Timedelta]:
        """
        Gets the long property value. Time spent in long meetings (more than an hour in duration). The value is represented in ISO 8601 format for durations.
        Returns: Optional[Timedelta]
        """
        return self._long
    
    @long.setter
    def long(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the long property value. Time spent in long meetings (more than an hour in duration). The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the long property.
        """
        self._long = value
    
    @property
    def multitasking(self,) -> Optional[Timedelta]:
        """
        Gets the multitasking property value. Time spent in meetings where the person was multitasking (read/sent more than a minimum number of emails and/or sent more than a minimum number of messages in Teams or in Skype for Business). The value is represented in ISO 8601 format for durations.
        Returns: Optional[Timedelta]
        """
        return self._multitasking
    
    @multitasking.setter
    def multitasking(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the multitasking property value. Time spent in meetings where the person was multitasking (read/sent more than a minimum number of emails and/or sent more than a minimum number of messages in Teams or in Skype for Business). The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the multitasking property.
        """
        self._multitasking = value
    
    @property
    def organized(self,) -> Optional[Timedelta]:
        """
        Gets the organized property value. Time spent in meetings organized by the user. The value is represented in ISO 8601 format for durations.
        Returns: Optional[Timedelta]
        """
        return self._organized
    
    @organized.setter
    def organized(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the organized property value. Time spent in meetings organized by the user. The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the organized property.
        """
        self._organized = value
    
    @property
    def recurring(self,) -> Optional[Timedelta]:
        """
        Gets the recurring property value. Time spent on recurring meetings. The value is represented in ISO 8601 format for durations.
        Returns: Optional[Timedelta]
        """
        return self._recurring
    
    @recurring.setter
    def recurring(self,value: Optional[Timedelta] = None) -> None:
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
        writer.write_object_value("afterHours", self.after_hours)
        writer.write_object_value("conflicting", self.conflicting)
        writer.write_object_value("long", self.long)
        writer.write_object_value("multitasking", self.multitasking)
        writer.write_object_value("organized", self.organized)
        writer.write_object_value("recurring", self.recurring)
    

