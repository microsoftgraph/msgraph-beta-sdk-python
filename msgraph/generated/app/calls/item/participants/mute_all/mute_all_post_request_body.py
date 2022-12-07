from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class MuteAllPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the muteAll method.
    """
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
    def client_context(self,) -> Optional[str]:
        """
        Gets the clientContext property value. The clientContext property
        Returns: Optional[str]
        """
        return self._client_context
    
    @client_context.setter
    def client_context(self,value: Optional[str] = None) -> None:
        """
        Sets the clientContext property value. The clientContext property
        Args:
            value: Value to set for the clientContext property.
        """
        self._client_context = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new muteAllPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The clientContext property
        self._client_context: Optional[str] = None
        # The participants property
        self._participants: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MuteAllPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MuteAllPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MuteAllPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "client_context": lambda n : setattr(self, 'client_context', n.get_str_value()),
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def participants(self,) -> Optional[List[str]]:
        """
        Gets the participants property value. The participants property
        Returns: Optional[List[str]]
        """
        return self._participants
    
    @participants.setter
    def participants(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the participants property value. The participants property
        Args:
            value: Value to set for the participants property.
        """
        self._participants = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("clientContext", self.client_context)
        writer.write_collection_of_primitive_values("participants", self.participants)
        writer.write_additional_data_value(self.additional_data)
    

