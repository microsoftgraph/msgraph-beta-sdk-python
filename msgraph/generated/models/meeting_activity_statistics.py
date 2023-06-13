from __future__ import annotations
from dataclasses import dataclass, field
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import activity_statistics

from . import activity_statistics

@dataclass
class MeetingActivityStatistics(activity_statistics.ActivityStatistics):
    odata_type = "#microsoft.graph.meetingActivityStatistics"
    # Time spent on meetings outside of working hours, which is based on the user's Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
    after_hours: Optional[timedelta] = None
    # Time spent in conflicting meetings (meetings that overlap with other meetings that the person accepted and where the person’s status is set to Busy). The value is represented in ISO 8601 format for durations.
    conflicting: Optional[timedelta] = None
    # Time spent in long meetings (more than an hour in duration). The value is represented in ISO 8601 format for durations.
    long: Optional[timedelta] = None
    # Time spent in meetings where the person was multitasking (read/sent more than a minimum number of emails and/or sent more than a minimum number of messages in Teams or in Skype for Business). The value is represented in ISO 8601 format for durations.
    multitasking: Optional[timedelta] = None
    # Time spent in meetings organized by the user. The value is represented in ISO 8601 format for durations.
    organized: Optional[timedelta] = None
    # Time spent on recurring meetings. The value is represented in ISO 8601 format for durations.
    recurring: Optional[timedelta] = None
    
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
    

