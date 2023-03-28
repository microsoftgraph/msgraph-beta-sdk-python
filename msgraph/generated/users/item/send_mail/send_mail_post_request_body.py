from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import message

class SendMailPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new sendMailPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The Message property
        self._message: Optional[message.Message] = None
        # The SaveToSentItems property
        self._save_to_sent_items: Optional[bool] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SendMailPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SendMailPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SendMailPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models import message

        fields: Dict[str, Callable[[Any], None]] = {
            "Message": lambda n : setattr(self, 'message', n.get_object_value(message.Message)),
            "SaveToSentItems": lambda n : setattr(self, 'save_to_sent_items', n.get_bool_value()),
        }
        return fields
    
    @property
    def message(self,) -> Optional[message.Message]:
        """
        Gets the message property value. The Message property
        Returns: Optional[message.Message]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[message.Message] = None) -> None:
        """
        Sets the message property value. The Message property
        Args:
            value: Value to set for the Message property.
        """
        self._message = value
    
    @property
    def save_to_sent_items(self,) -> Optional[bool]:
        """
        Gets the saveToSentItems property value. The SaveToSentItems property
        Returns: Optional[bool]
        """
        return self._save_to_sent_items
    
    @save_to_sent_items.setter
    def save_to_sent_items(self,value: Optional[bool] = None) -> None:
        """
        Sets the saveToSentItems property value. The SaveToSentItems property
        Args:
            value: Value to set for the save_to_sent_items property.
        """
        self._save_to_sent_items = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("Message", self.message)
        writer.write_bool_value("SaveToSentItems", self.save_to_sent_items)
        writer.write_additional_data_value(self.additional_data)
    

