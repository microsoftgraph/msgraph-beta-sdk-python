from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class UnsetReactionPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the unsetReaction method.
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new unsetReactionPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The reactionType property
        self._reaction_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnsetReactionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnsetReactionPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnsetReactionPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "reaction_type": lambda n : setattr(self, 'reaction_type', n.get_str_value()),
        }
        return fields
    
    @property
    def reaction_type(self,) -> Optional[str]:
        """
        Gets the reactionType property value. The reactionType property
        Returns: Optional[str]
        """
        return self._reaction_type
    
    @reaction_type.setter
    def reaction_type(self,value: Optional[str] = None) -> None:
        """
        Sets the reactionType property value. The reactionType property
        Args:
            value: Value to set for the reactionType property.
        """
        self._reaction_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("reactionType", self.reaction_type)
        writer.write_additional_data_value(self.additional_data)
    

