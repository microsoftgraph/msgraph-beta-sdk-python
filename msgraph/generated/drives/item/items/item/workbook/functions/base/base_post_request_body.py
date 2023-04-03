from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class BasePostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new basePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The minLength property
        self._min_length: Optional[json.Json] = None
        # The number property
        self._number: Optional[json.Json] = None
        # The radix property
        self._radix: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BasePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BasePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BasePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "minLength": lambda n : setattr(self, 'min_length', n.get_object_value(json.Json)),
            "number": lambda n : setattr(self, 'number', n.get_object_value(json.Json)),
            "radix": lambda n : setattr(self, 'radix', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def min_length(self,) -> Optional[json.Json]:
        """
        Gets the minLength property value. The minLength property
        Returns: Optional[json.Json]
        """
        return self._min_length
    
    @min_length.setter
    def min_length(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the minLength property value. The minLength property
        Args:
            value: Value to set for the min_length property.
        """
        self._min_length = value
    
    @property
    def number(self,) -> Optional[json.Json]:
        """
        Gets the number property value. The number property
        Returns: Optional[json.Json]
        """
        return self._number
    
    @number.setter
    def number(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the number property value. The number property
        Args:
            value: Value to set for the number property.
        """
        self._number = value
    
    @property
    def radix(self,) -> Optional[json.Json]:
        """
        Gets the radix property value. The radix property
        Returns: Optional[json.Json]
        """
        return self._radix
    
    @radix.setter
    def radix(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the radix property value. The radix property
        Args:
            value: Value to set for the radix property.
        """
        self._radix = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("minLength", self.min_length)
        writer.write_object_value("number", self.number)
        writer.write_object_value("radix", self.radix)
        writer.write_additional_data_value(self.additional_data)
    
