from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .detected_sensitive_content import DetectedSensitiveContent
    from .exact_match_detected_sensitive_content import ExactMatchDetectedSensitiveContent
    from .machine_learning_detected_sensitive_content import MachineLearningDetectedSensitiveContent

@dataclass
class DetectedSensitiveContentBase(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The confidence property
    confidence: Optional[int] = None
    # The displayName property
    display_name: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recommendedConfidence property
    recommended_confidence: Optional[int] = None
    # The uniqueCount property
    unique_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DetectedSensitiveContentBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DetectedSensitiveContentBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.detectedSensitiveContent".casefold():
            from .detected_sensitive_content import DetectedSensitiveContent

            return DetectedSensitiveContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exactMatchDetectedSensitiveContent".casefold():
            from .exact_match_detected_sensitive_content import ExactMatchDetectedSensitiveContent

            return ExactMatchDetectedSensitiveContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.machineLearningDetectedSensitiveContent".casefold():
            from .machine_learning_detected_sensitive_content import MachineLearningDetectedSensitiveContent

            return MachineLearningDetectedSensitiveContent()
        return DetectedSensitiveContentBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .detected_sensitive_content import DetectedSensitiveContent
        from .exact_match_detected_sensitive_content import ExactMatchDetectedSensitiveContent
        from .machine_learning_detected_sensitive_content import MachineLearningDetectedSensitiveContent

        from .detected_sensitive_content import DetectedSensitiveContent
        from .exact_match_detected_sensitive_content import ExactMatchDetectedSensitiveContent
        from .machine_learning_detected_sensitive_content import MachineLearningDetectedSensitiveContent

        fields: Dict[str, Callable[[Any], None]] = {
            "confidence": lambda n : setattr(self, 'confidence', n.get_int_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recommendedConfidence": lambda n : setattr(self, 'recommended_confidence', n.get_int_value()),
            "uniqueCount": lambda n : setattr(self, 'unique_count', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("confidence", self.confidence)
        writer.write_str_value("displayName", self.display_name)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_int_value("recommendedConfidence", self.recommended_confidence)
        writer.write_int_value("uniqueCount", self.unique_count)
        writer.write_additional_data_value(self.additional_data)
    

