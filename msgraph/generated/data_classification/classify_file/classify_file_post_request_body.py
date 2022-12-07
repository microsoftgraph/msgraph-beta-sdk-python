from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ClassifyFilePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the classifyFile method.
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
        Instantiates a new classifyFilePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The file property
        self._file: Optional[bytes] = None
        # The sensitiveTypeIds property
        self._sensitive_type_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ClassifyFilePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ClassifyFilePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ClassifyFilePostRequestBody()
    
    @property
    def file(self,) -> Optional[bytes]:
        """
        Gets the file property value. The file property
        Returns: Optional[bytes]
        """
        return self._file
    
    @file.setter
    def file(self,value: Optional[bytes] = None) -> None:
        """
        Sets the file property value. The file property
        Args:
            value: Value to set for the file property.
        """
        self._file = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "file": lambda n : setattr(self, 'file', n.get_bytes_value()),
            "sensitive_type_ids": lambda n : setattr(self, 'sensitive_type_ids', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def sensitive_type_ids(self,) -> Optional[List[str]]:
        """
        Gets the sensitiveTypeIds property value. The sensitiveTypeIds property
        Returns: Optional[List[str]]
        """
        return self._sensitive_type_ids
    
    @sensitive_type_ids.setter
    def sensitive_type_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the sensitiveTypeIds property value. The sensitiveTypeIds property
        Args:
            value: Value to set for the sensitiveTypeIds property.
        """
        self._sensitive_type_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("file", self.file)
        writer.write_collection_of_primitive_values("sensitiveTypeIds", self.sensitive_type_ids)
        writer.write_additional_data_value(self.additional_data)
    

