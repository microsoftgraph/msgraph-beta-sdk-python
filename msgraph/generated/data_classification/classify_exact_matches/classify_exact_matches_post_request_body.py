from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

content_classification = lazy_import('msgraph.generated.models.content_classification')

class ClassifyExactMatchesPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the classifyExactMatches method.
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
        Instantiates a new classifyExactMatchesPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The contentClassifications property
        self._content_classifications: Optional[List[content_classification.ContentClassification]] = None
        # The sensitiveTypeIds property
        self._sensitive_type_ids: Optional[List[str]] = None
        # The text property
        self._text: Optional[str] = None
        # The timeoutInMs property
        self._timeout_in_ms: Optional[str] = None
    
    @property
    def content_classifications(self,) -> Optional[List[content_classification.ContentClassification]]:
        """
        Gets the contentClassifications property value. The contentClassifications property
        Returns: Optional[List[content_classification.ContentClassification]]
        """
        return self._content_classifications
    
    @content_classifications.setter
    def content_classifications(self,value: Optional[List[content_classification.ContentClassification]] = None) -> None:
        """
        Sets the contentClassifications property value. The contentClassifications property
        Args:
            value: Value to set for the contentClassifications property.
        """
        self._content_classifications = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ClassifyExactMatchesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ClassifyExactMatchesPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ClassifyExactMatchesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content_classifications": lambda n : setattr(self, 'content_classifications', n.get_collection_of_object_values(content_classification.ContentClassification)),
            "sensitive_type_ids": lambda n : setattr(self, 'sensitive_type_ids', n.get_collection_of_primitive_values(str)),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "timeout_in_ms": lambda n : setattr(self, 'timeout_in_ms', n.get_str_value()),
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
        writer.write_collection_of_object_values("contentClassifications", self.content_classifications)
        writer.write_collection_of_primitive_values("sensitiveTypeIds", self.sensitive_type_ids)
        writer.write_str_value("text", self.text)
        writer.write_str_value("timeoutInMs", self.timeout_in_ms)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def text(self,) -> Optional[str]:
        """
        Gets the text property value. The text property
        Returns: Optional[str]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[str] = None) -> None:
        """
        Sets the text property value. The text property
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    
    @property
    def timeout_in_ms(self,) -> Optional[str]:
        """
        Gets the timeoutInMs property value. The timeoutInMs property
        Returns: Optional[str]
        """
        return self._timeout_in_ms
    
    @timeout_in_ms.setter
    def timeout_in_ms(self,value: Optional[str] = None) -> None:
        """
        Sets the timeoutInMs property value. The timeoutInMs property
        Args:
            value: Value to set for the timeoutInMs property.
        """
        self._timeout_in_ms = value
    

