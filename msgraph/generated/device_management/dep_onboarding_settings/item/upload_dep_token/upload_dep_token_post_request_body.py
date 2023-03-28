from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class UploadDepTokenPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new uploadDepTokenPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The appleId property
        self._apple_id: Optional[str] = None
        # The depToken property
        self._dep_token: Optional[str] = None
    
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
    
    @property
    def apple_id(self,) -> Optional[str]:
        """
        Gets the appleId property value. The appleId property
        Returns: Optional[str]
        """
        return self._apple_id
    
    @apple_id.setter
    def apple_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appleId property value. The appleId property
        Args:
            value: Value to set for the apple_id property.
        """
        self._apple_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UploadDepTokenPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UploadDepTokenPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UploadDepTokenPostRequestBody()
    
    @property
    def dep_token(self,) -> Optional[str]:
        """
        Gets the depToken property value. The depToken property
        Returns: Optional[str]
        """
        return self._dep_token
    
    @dep_token.setter
    def dep_token(self,value: Optional[str] = None) -> None:
        """
        Sets the depToken property value. The depToken property
        Args:
            value: Value to set for the dep_token property.
        """
        self._dep_token = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "appleId": lambda n : setattr(self, 'apple_id', n.get_str_value()),
            "depToken": lambda n : setattr(self, 'dep_token', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("appleId", self.apple_id)
        writer.write_str_value("depToken", self.dep_token)
        writer.write_additional_data_value(self.additional_data)
    

