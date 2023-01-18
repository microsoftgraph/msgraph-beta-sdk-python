from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
message_recipient = lazy_import('msgraph.generated.models.message_recipient')

class MessageTrace(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new MessageTrace and sets the default values.
        """
        super().__init__()
        # The destinationIPAddress property
        self._destination_i_p_address: Optional[str] = None
        # The messageId property
        self._message_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The receivedDateTime property
        self._received_date_time: Optional[datetime] = None
        # The recipients property
        self._recipients: Optional[List[message_recipient.MessageRecipient]] = None
        # The senderEmail property
        self._sender_email: Optional[str] = None
        # The size property
        self._size: Optional[int] = None
        # The sourceIPAddress property
        self._source_i_p_address: Optional[str] = None
        # The subject property
        self._subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MessageTrace:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MessageTrace
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MessageTrace()
    
    @property
    def destination_i_p_address(self,) -> Optional[str]:
        """
        Gets the destinationIPAddress property value. The destinationIPAddress property
        Returns: Optional[str]
        """
        return self._destination_i_p_address
    
    @destination_i_p_address.setter
    def destination_i_p_address(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationIPAddress property value. The destinationIPAddress property
        Args:
            value: Value to set for the destinationIPAddress property.
        """
        self._destination_i_p_address = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "destination_i_p_address": lambda n : setattr(self, 'destination_i_p_address', n.get_str_value()),
            "message_id": lambda n : setattr(self, 'message_id', n.get_str_value()),
            "received_date_time": lambda n : setattr(self, 'received_date_time', n.get_datetime_value()),
            "recipients": lambda n : setattr(self, 'recipients', n.get_collection_of_object_values(message_recipient.MessageRecipient)),
            "sender_email": lambda n : setattr(self, 'sender_email', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "source_i_p_address": lambda n : setattr(self, 'source_i_p_address', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def message_id(self,) -> Optional[str]:
        """
        Gets the messageId property value. The messageId property
        Returns: Optional[str]
        """
        return self._message_id
    
    @message_id.setter
    def message_id(self,value: Optional[str] = None) -> None:
        """
        Sets the messageId property value. The messageId property
        Args:
            value: Value to set for the messageId property.
        """
        self._message_id = value
    
    @property
    def received_date_time(self,) -> Optional[datetime]:
        """
        Gets the receivedDateTime property value. The receivedDateTime property
        Returns: Optional[datetime]
        """
        return self._received_date_time
    
    @received_date_time.setter
    def received_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the receivedDateTime property value. The receivedDateTime property
        Args:
            value: Value to set for the receivedDateTime property.
        """
        self._received_date_time = value
    
    @property
    def recipients(self,) -> Optional[List[message_recipient.MessageRecipient]]:
        """
        Gets the recipients property value. The recipients property
        Returns: Optional[List[message_recipient.MessageRecipient]]
        """
        return self._recipients
    
    @recipients.setter
    def recipients(self,value: Optional[List[message_recipient.MessageRecipient]] = None) -> None:
        """
        Sets the recipients property value. The recipients property
        Args:
            value: Value to set for the recipients property.
        """
        self._recipients = value
    
    @property
    def sender_email(self,) -> Optional[str]:
        """
        Gets the senderEmail property value. The senderEmail property
        Returns: Optional[str]
        """
        return self._sender_email
    
    @sender_email.setter
    def sender_email(self,value: Optional[str] = None) -> None:
        """
        Sets the senderEmail property value. The senderEmail property
        Args:
            value: Value to set for the senderEmail property.
        """
        self._sender_email = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("destinationIPAddress", self.destination_i_p_address)
        writer.write_str_value("messageId", self.message_id)
        writer.write_datetime_value("receivedDateTime", self.received_date_time)
        writer.write_collection_of_object_values("recipients", self.recipients)
        writer.write_str_value("senderEmail", self.sender_email)
        writer.write_int_value("size", self.size)
        writer.write_str_value("sourceIPAddress", self.source_i_p_address)
        writer.write_str_value("subject", self.subject)
    
    @property
    def size(self,) -> Optional[int]:
        """
        Gets the size property value. The size property
        Returns: Optional[int]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[int] = None) -> None:
        """
        Sets the size property value. The size property
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    
    @property
    def source_i_p_address(self,) -> Optional[str]:
        """
        Gets the sourceIPAddress property value. The sourceIPAddress property
        Returns: Optional[str]
        """
        return self._source_i_p_address
    
    @source_i_p_address.setter
    def source_i_p_address(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceIPAddress property value. The sourceIPAddress property
        Args:
            value: Value to set for the sourceIPAddress property.
        """
        self._source_i_p_address = value
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. The subject property
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. The subject property
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    

