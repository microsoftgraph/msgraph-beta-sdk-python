from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class HasPayloadLinksPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new hasPayloadLinksPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The payloadIds property
        self._payload_ids: Optional[List[str]] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HasPayloadLinksPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HasPayloadLinksPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return HasPayloadLinksPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "payloadIds": lambda n : setattr(self, 'payload_ids', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def payload_ids(self,) -> Optional[List[str]]:
        """
        Gets the payloadIds property value. The payloadIds property
        Returns: Optional[List[str]]
        """
        return self._payload_ids
    
    @payload_ids.setter
    def payload_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the payloadIds property value. The payloadIds property
        Args:
            value: Value to set for the payload_ids property.
        """
        self._payload_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("payloadIds", self.payload_ids)
        writer.write_additional_data_value(self.additional_data)
    

