from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, message_event_type

from . import entity

@dataclass
class MessageEvent(entity.Entity):
    # The dateTime property
    date_time: Optional[datetime] = None
    # The description property
    description: Optional[str] = None
    # The eventType property
    event_type: Optional[message_event_type.MessageEventType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MessageEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MessageEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MessageEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, message_event_type

        fields: Dict[str, Callable[[Any], None]] = {
            "dateTime": lambda n : setattr(self, 'date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "eventType": lambda n : setattr(self, 'event_type', n.get_enum_value(message_event_type.MessageEventType)),
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
        writer.write_datetime_value("dateTime", self.date_time)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("eventType", self.event_type)
    

