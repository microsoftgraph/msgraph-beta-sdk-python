from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

detected_sensitive_content = lazy_import('msgraph.generated.models.detected_sensitive_content')
ml_classification_match_tolerance = lazy_import('msgraph.generated.models.ml_classification_match_tolerance')

class MachineLearningDetectedSensitiveContent(detected_sensitive_content.DetectedSensitiveContent):
    def __init__(self,) -> None:
        """
        Instantiates a new MachineLearningDetectedSensitiveContent and sets the default values.
        """
        super().__init__()
        # The matchTolerance property
        self._match_tolerance: Optional[ml_classification_match_tolerance.MlClassificationMatchTolerance] = None
        # The modelVersion property
        self._model_version: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MachineLearningDetectedSensitiveContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MachineLearningDetectedSensitiveContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MachineLearningDetectedSensitiveContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "match_tolerance": lambda n : setattr(self, 'match_tolerance', n.get_enum_value(ml_classification_match_tolerance.MlClassificationMatchTolerance)),
            "model_version": lambda n : setattr(self, 'model_version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def match_tolerance(self,) -> Optional[ml_classification_match_tolerance.MlClassificationMatchTolerance]:
        """
        Gets the matchTolerance property value. The matchTolerance property
        Returns: Optional[ml_classification_match_tolerance.MlClassificationMatchTolerance]
        """
        return self._match_tolerance
    
    @match_tolerance.setter
    def match_tolerance(self,value: Optional[ml_classification_match_tolerance.MlClassificationMatchTolerance] = None) -> None:
        """
        Sets the matchTolerance property value. The matchTolerance property
        Args:
            value: Value to set for the matchTolerance property.
        """
        self._match_tolerance = value
    
    @property
    def model_version(self,) -> Optional[str]:
        """
        Gets the modelVersion property value. The modelVersion property
        Returns: Optional[str]
        """
        return self._model_version
    
    @model_version.setter
    def model_version(self,value: Optional[str] = None) -> None:
        """
        Sets the modelVersion property value. The modelVersion property
        Args:
            value: Value to set for the modelVersion property.
        """
        self._model_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("matchTolerance", self.match_tolerance)
        writer.write_str_value("modelVersion", self.model_version)
    

