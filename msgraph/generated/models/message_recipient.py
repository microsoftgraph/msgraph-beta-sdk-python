from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
message_event = lazy_import('msgraph.generated.models.message_event')
message_status = lazy_import('msgraph.generated.models.message_status')

class MessageRecipient(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new MessageRecipient and sets the default values.
        """
        super().__init__()
        # The deliveryStatus property
        self._delivery_status: Optional[message_status.MessageStatus] = None
        # The events property
        self._events: Optional[List[message_event.MessageEvent]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The recipientEmail property
        self._recipient_email: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MessageRecipient:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MessageRecipient
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MessageRecipient()
    
    @property
    def delivery_status(self,) -> Optional[message_status.MessageStatus]:
        """
        Gets the deliveryStatus property value. The deliveryStatus property
        Returns: Optional[message_status.MessageStatus]
        """
        return self._delivery_status
    
    @delivery_status.setter
    def delivery_status(self,value: Optional[message_status.MessageStatus] = None) -> None:
        """
        Sets the deliveryStatus property value. The deliveryStatus property
        Args:
            value: Value to set for the deliveryStatus property.
        """
        self._delivery_status = value
    
    @property
    def events(self,) -> Optional[List[message_event.MessageEvent]]:
        """
        Gets the events property value. The events property
        Returns: Optional[List[message_event.MessageEvent]]
        """
        return self._events
    
    @events.setter
    def events(self,value: Optional[List[message_event.MessageEvent]] = None) -> None:
        """
        Sets the events property value. The events property
        Args:
            value: Value to set for the events property.
        """
        self._events = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "delivery_status": lambda n : setattr(self, 'delivery_status', n.get_enum_value(message_status.MessageStatus)),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(message_event.MessageEvent)),
            "recipient_email": lambda n : setattr(self, 'recipient_email', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def recipient_email(self,) -> Optional[str]:
        """
        Gets the recipientEmail property value. The recipientEmail property
        Returns: Optional[str]
        """
        return self._recipient_email
    
    @recipient_email.setter
    def recipient_email(self,value: Optional[str] = None) -> None:
        """
        Sets the recipientEmail property value. The recipientEmail property
        Args:
            value: Value to set for the recipientEmail property.
        """
        self._recipient_email = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("deliveryStatus", self.delivery_status)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_str_value("recipientEmail", self.recipient_email)
    

