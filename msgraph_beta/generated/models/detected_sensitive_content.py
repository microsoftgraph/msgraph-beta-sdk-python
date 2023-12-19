from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .classification_attribute import ClassificationAttribute
    from .detected_sensitive_content_base import DetectedSensitiveContentBase
    from .detected_sensitive_content_classification_method import DetectedSensitiveContent_classificationMethod
    from .detected_sensitive_content_scope import DetectedSensitiveContent_scope
    from .detected_sensitive_content_sensitive_type_source import DetectedSensitiveContent_sensitiveTypeSource
    from .machine_learning_detected_sensitive_content import MachineLearningDetectedSensitiveContent
    from .sensitive_content_location import SensitiveContentLocation

from .detected_sensitive_content_base import DetectedSensitiveContentBase

@dataclass
class DetectedSensitiveContent(DetectedSensitiveContentBase):
    # The classificationAttributes property
    classification_attributes: Optional[List[ClassificationAttribute]] = None
    # The classificationMethod property
    classification_method: Optional[DetectedSensitiveContent_classificationMethod] = None
    # The matches property
    matches: Optional[List[SensitiveContentLocation]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The scope property
    scope: Optional[DetectedSensitiveContent_scope] = None
    # The sensitiveTypeSource property
    sensitive_type_source: Optional[DetectedSensitiveContent_sensitiveTypeSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DetectedSensitiveContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DetectedSensitiveContent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.machineLearningDetectedSensitiveContent".casefold():
            from .machine_learning_detected_sensitive_content import MachineLearningDetectedSensitiveContent

            return MachineLearningDetectedSensitiveContent()
        return DetectedSensitiveContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .classification_attribute import ClassificationAttribute
        from .detected_sensitive_content_base import DetectedSensitiveContentBase
        from .detected_sensitive_content_classification_method import DetectedSensitiveContent_classificationMethod
        from .detected_sensitive_content_scope import DetectedSensitiveContent_scope
        from .detected_sensitive_content_sensitive_type_source import DetectedSensitiveContent_sensitiveTypeSource
        from .machine_learning_detected_sensitive_content import MachineLearningDetectedSensitiveContent
        from .sensitive_content_location import SensitiveContentLocation

        from .classification_attribute import ClassificationAttribute
        from .detected_sensitive_content_base import DetectedSensitiveContentBase
        from .detected_sensitive_content_classification_method import DetectedSensitiveContent_classificationMethod
        from .detected_sensitive_content_scope import DetectedSensitiveContent_scope
        from .detected_sensitive_content_sensitive_type_source import DetectedSensitiveContent_sensitiveTypeSource
        from .machine_learning_detected_sensitive_content import MachineLearningDetectedSensitiveContent
        from .sensitive_content_location import SensitiveContentLocation

        fields: Dict[str, Callable[[Any], None]] = {
            "classificationAttributes": lambda n : setattr(self, 'classification_attributes', n.get_collection_of_object_values(ClassificationAttribute)),
            "classificationMethod": lambda n : setattr(self, 'classification_method', n.get_enum_value(DetectedSensitiveContent_classificationMethod)),
            "matches": lambda n : setattr(self, 'matches', n.get_collection_of_object_values(SensitiveContentLocation)),
            "scope": lambda n : setattr(self, 'scope', n.get_enum_value(DetectedSensitiveContent_scope)),
            "sensitiveTypeSource": lambda n : setattr(self, 'sensitive_type_source', n.get_enum_value(DetectedSensitiveContent_sensitiveTypeSource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("classificationAttributes", self.classification_attributes)
        writer.write_enum_value("classificationMethod", self.classification_method)
        writer.write_collection_of_object_values("matches", self.matches)
        writer.write_enum_value("scope", self.scope)
        writer.write_enum_value("sensitiveTypeSource", self.sensitive_type_source)
    

