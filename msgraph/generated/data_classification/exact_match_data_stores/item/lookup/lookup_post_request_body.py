from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class LookupPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the lookup method.
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
        Instantiates a new lookupPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The key property
        self._key: Optional[str] = None
        # The resultColumnNames property
        self._result_column_names: Optional[List[str]] = None
        # The values property
        self._values: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LookupPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LookupPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LookupPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "result_column_names": lambda n : setattr(self, 'result_column_names', n.get_collection_of_primitive_values(str)),
            "values": lambda n : setattr(self, 'values', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def key(self,) -> Optional[str]:
        """
        Gets the key property value. The key property
        Returns: Optional[str]
        """
        return self._key
    
    @key.setter
    def key(self,value: Optional[str] = None) -> None:
        """
        Sets the key property value. The key property
        Args:
            value: Value to set for the key property.
        """
        self._key = value
    
    @property
    def result_column_names(self,) -> Optional[List[str]]:
        """
        Gets the resultColumnNames property value. The resultColumnNames property
        Returns: Optional[List[str]]
        """
        return self._result_column_names
    
    @result_column_names.setter
    def result_column_names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the resultColumnNames property value. The resultColumnNames property
        Args:
            value: Value to set for the resultColumnNames property.
        """
        self._result_column_names = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("key", self.key)
        writer.write_collection_of_primitive_values("resultColumnNames", self.result_column_names)
        writer.write_collection_of_primitive_values("values", self.values)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def values(self,) -> Optional[List[str]]:
        """
        Gets the values property value. The values property
        Returns: Optional[List[str]]
        """
        return self._values
    
    @values.setter
    def values(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the values property value. The values property
        Args:
            value: Value to set for the values property.
        """
        self._values = value
    

