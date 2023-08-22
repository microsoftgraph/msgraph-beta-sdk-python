from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity_statistics import ActivityStatistics

from .activity_statistics import ActivityStatistics

@dataclass
class ChatActivityStatistics(ActivityStatistics):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.chatActivityStatistics"
    # Time spent on chats outside of working hours, which is based on the user's Microsoft Outlook calendar setting for work hours. The value is represented in ISO 8601 format for durations.
    after_hours: Optional[datetime.timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatActivityStatistics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChatActivityStatistics
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ChatActivityStatistics()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .activity_statistics import ActivityStatistics

        from .activity_statistics import ActivityStatistics

        fields: Dict[str, Callable[[Any], None]] = {
            "afterHours": lambda n : setattr(self, 'after_hours', n.get_timedelta_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_timedelta_value("afterHours", self.after_hours)
    

