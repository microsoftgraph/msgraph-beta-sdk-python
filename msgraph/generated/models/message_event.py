from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
message_event_type = lazy_import('msgraph.generated.models.message_event_type')

class MessageEvent(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new MessageEvent and sets the default values.
        """
        super().__init__()
        # The dateTime property
        self._date_time: Optional[datetime] = None
        # The description property
        self._description: Optional[str] = None
        # The eventType property
        self._event_type: Optional[message_event_type.MessageEventType] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
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
    
    @property
    def date_time(self,) -> Optional[datetime]:
        """
        Gets the dateTime property value. The dateTime property
        Returns: Optional[datetime]
        """
        return self._date_time
    
    @date_time.setter
    def date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the dateTime property value. The dateTime property
        Args:
            value: Value to set for the dateTime property.
        """
        self._date_time = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def event_type(self,) -> Optional[message_event_type.MessageEventType]:
        """
        Gets the eventType property value. The eventType property
        Returns: Optional[message_event_type.MessageEventType]
        """
        return self._event_type
    
    @event_type.setter
    def event_type(self,value: Optional[message_event_type.MessageEventType] = None) -> None:
        """
        Sets the eventType property value. The eventType property
        Args:
            value: Value to set for the eventType property.
        """
        self._event_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "date_time": lambda n : setattr(self, 'date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "event_type": lambda n : setattr(self, 'event_type', n.get_enum_value(message_event_type.MessageEventType)),
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
    

