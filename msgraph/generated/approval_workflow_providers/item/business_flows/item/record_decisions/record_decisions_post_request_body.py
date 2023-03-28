from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class RecordDecisionsPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new recordDecisionsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The justification property
        self._justification: Optional[str] = None
        # The reviewResult property
        self._review_result: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecordDecisionsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RecordDecisionsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RecordDecisionsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "reviewResult": lambda n : setattr(self, 'review_result', n.get_str_value()),
        }
        return fields
    
    @property
    def justification(self,) -> Optional[str]:
        """
        Gets the justification property value. The justification property
        Returns: Optional[str]
        """
        return self._justification
    
    @justification.setter
    def justification(self,value: Optional[str] = None) -> None:
        """
        Sets the justification property value. The justification property
        Args:
            value: Value to set for the justification property.
        """
        self._justification = value
    
    @property
    def review_result(self,) -> Optional[str]:
        """
        Gets the reviewResult property value. The reviewResult property
        Returns: Optional[str]
        """
        return self._review_result
    
    @review_result.setter
    def review_result(self,value: Optional[str] = None) -> None:
        """
        Sets the reviewResult property value. The reviewResult property
        Args:
            value: Value to set for the review_result property.
        """
        self._review_result = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("justification", self.justification)
        writer.write_str_value("reviewResult", self.review_result)
        writer.write_additional_data_value(self.additional_data)
    

