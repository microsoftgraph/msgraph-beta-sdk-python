from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class MarkAsNotJunkPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new markAsNotJunkPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The moveToInbox property
        self._move_to_inbox: Optional[bool] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MarkAsNotJunkPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MarkAsNotJunkPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MarkAsNotJunkPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "moveToInbox": lambda n : setattr(self, 'move_to_inbox', n.get_bool_value()),
        }
        return fields
    
    @property
    def move_to_inbox(self,) -> Optional[bool]:
        """
        Gets the moveToInbox property value. The moveToInbox property
        Returns: Optional[bool]
        """
        return self._move_to_inbox
    
    @move_to_inbox.setter
    def move_to_inbox(self,value: Optional[bool] = None) -> None:
        """
        Sets the moveToInbox property value. The moveToInbox property
        Args:
            value: Value to set for the move_to_inbox property.
        """
        self._move_to_inbox = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("moveToInbox", self.move_to_inbox)
        writer.write_additional_data_value(self.additional_data)
    

