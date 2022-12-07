from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

classification_result = lazy_import('msgraph.generated.models.classification_result')
content_info = lazy_import('msgraph.generated.models.content_info')

class EvaluateClassificationResultsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the evaluateClassificationResults method.
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
    def classification_results(self,) -> Optional[List[classification_result.ClassificationResult]]:
        """
        Gets the classificationResults property value. The classificationResults property
        Returns: Optional[List[classification_result.ClassificationResult]]
        """
        return self._classification_results
    
    @classification_results.setter
    def classification_results(self,value: Optional[List[classification_result.ClassificationResult]] = None) -> None:
        """
        Sets the classificationResults property value. The classificationResults property
        Args:
            value: Value to set for the classificationResults property.
        """
        self._classification_results = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new evaluateClassificationResultsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The classificationResults property
        self._classification_results: Optional[List[classification_result.ClassificationResult]] = None
        # The contentInfo property
        self._content_info: Optional[content_info.ContentInfo] = None
    
    @property
    def content_info(self,) -> Optional[content_info.ContentInfo]:
        """
        Gets the contentInfo property value. The contentInfo property
        Returns: Optional[content_info.ContentInfo]
        """
        return self._content_info
    
    @content_info.setter
    def content_info(self,value: Optional[content_info.ContentInfo] = None) -> None:
        """
        Sets the contentInfo property value. The contentInfo property
        Args:
            value: Value to set for the contentInfo property.
        """
        self._content_info = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluateClassificationResultsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateClassificationResultsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EvaluateClassificationResultsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "classification_results": lambda n : setattr(self, 'classification_results', n.get_collection_of_object_values(classification_result.ClassificationResult)),
            "content_info": lambda n : setattr(self, 'content_info', n.get_object_value(content_info.ContentInfo)),
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
        writer.write_collection_of_object_values("classificationResults", self.classification_results)
        writer.write_object_value("contentInfo", self.content_info)
        writer.write_additional_data_value(self.additional_data)
    

