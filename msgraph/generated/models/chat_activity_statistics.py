from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import activity_statistics

from . import activity_statistics

class ChatActivityStatistics(activity_statistics.ActivityStatistics):
    def __init__(self,) -> None:
        """
        Instantiates a new ChatActivityStatistics and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.chatActivityStatistics"
        # Time spent on chats outside of working hours, which is based on the user's Microsoft Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        self._after_hours: Optional[timedelta] = None
    
    @property
    def after_hours(self,) -> Optional[timedelta]:
        """
        Gets the afterHours property value. Time spent on chats outside of working hours, which is based on the user's Microsoft Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        Returns: Optional[timedelta]
        """
        return self._after_hours
    
    @after_hours.setter
    def after_hours(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the afterHours property value. Time spent on chats outside of working hours, which is based on the user's Microsoft Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
        Args:
            value: Value to set for the after_hours property.
        """
        self._after_hours = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatActivityStatistics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChatActivityStatistics
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChatActivityStatistics()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import activity_statistics

        fields: Dict[str, Callable[[Any], None]] = {
            "afterHours": lambda n : setattr(self, 'after_hours', n.get_timedelta_value()),
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
    

