from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

classification_error = lazy_import('msgraph.generated.models.classification_error')
exact_match_detected_sensitive_content = lazy_import('msgraph.generated.models.exact_match_detected_sensitive_content')

class ExactMatchClassificationResult(AdditionalDataHolder, Parsable):
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
    def classification(self,) -> Optional[List[exact_match_detected_sensitive_content.ExactMatchDetectedSensitiveContent]]:
        """
        Gets the classification property value. The classification property
        Returns: Optional[List[exact_match_detected_sensitive_content.ExactMatchDetectedSensitiveContent]]
        """
        return self._classification
    
    @classification.setter
    def classification(self,value: Optional[List[exact_match_detected_sensitive_content.ExactMatchDetectedSensitiveContent]] = None) -> None:
        """
        Sets the classification property value. The classification property
        Args:
            value: Value to set for the classification property.
        """
        self._classification = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new exactMatchClassificationResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The classification property
        self._classification: Optional[List[exact_match_detected_sensitive_content.ExactMatchDetectedSensitiveContent]] = None
        # The errors property
        self._errors: Optional[List[classification_error.ClassificationError]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExactMatchClassificationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExactMatchClassificationResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExactMatchClassificationResult()
    
    @property
    def errors(self,) -> Optional[List[classification_error.ClassificationError]]:
        """
        Gets the errors property value. The errors property
        Returns: Optional[List[classification_error.ClassificationError]]
        """
        return self._errors
    
    @errors.setter
    def errors(self,value: Optional[List[classification_error.ClassificationError]] = None) -> None:
        """
        Sets the errors property value. The errors property
        Args:
            value: Value to set for the errors property.
        """
        self._errors = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "classification": lambda n : setattr(self, 'classification', n.get_collection_of_object_values(exact_match_detected_sensitive_content.ExactMatchDetectedSensitiveContent)),
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(classification_error.ClassificationError)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("classification", self.classification)
        writer.write_collection_of_object_values("errors", self.errors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

