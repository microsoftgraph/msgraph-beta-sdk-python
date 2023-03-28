from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import classification_attribute, classification_method, detected_sensitive_content_base, machine_learning_detected_sensitive_content, sensitive_content_location, sensitive_type_scope, sensitive_type_source

from . import detected_sensitive_content_base

class DetectedSensitiveContent(detected_sensitive_content_base.DetectedSensitiveContentBase):
    def __init__(self,) -> None:
        """
        Instantiates a new DetectedSensitiveContent and sets the default values.
        """
        super().__init__()
        # The classificationAttributes property
        self._classification_attributes: Optional[List[classification_attribute.ClassificationAttribute]] = None
        # The classificationMethod property
        self._classification_method: Optional[classification_method.ClassificationMethod] = None
        # The matches property
        self._matches: Optional[List[sensitive_content_location.SensitiveContentLocation]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The scope property
        self._scope: Optional[sensitive_type_scope.SensitiveTypeScope] = None
        # The sensitiveTypeSource property
        self._sensitive_type_source: Optional[sensitive_type_source.SensitiveTypeSource] = None
    
    @property
    def classification_attributes(self,) -> Optional[List[classification_attribute.ClassificationAttribute]]:
        """
        Gets the classificationAttributes property value. The classificationAttributes property
        Returns: Optional[List[classification_attribute.ClassificationAttribute]]
        """
        return self._classification_attributes
    
    @classification_attributes.setter
    def classification_attributes(self,value: Optional[List[classification_attribute.ClassificationAttribute]] = None) -> None:
        """
        Sets the classificationAttributes property value. The classificationAttributes property
        Args:
            value: Value to set for the classification_attributes property.
        """
        self._classification_attributes = value
    
    @property
    def classification_method(self,) -> Optional[classification_method.ClassificationMethod]:
        """
        Gets the classificationMethod property value. The classificationMethod property
        Returns: Optional[classification_method.ClassificationMethod]
        """
        return self._classification_method
    
    @classification_method.setter
    def classification_method(self,value: Optional[classification_method.ClassificationMethod] = None) -> None:
        """
        Sets the classificationMethod property value. The classificationMethod property
        Args:
            value: Value to set for the classification_method property.
        """
        self._classification_method = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DetectedSensitiveContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DetectedSensitiveContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.machineLearningDetectedSensitiveContent":
                from . import machine_learning_detected_sensitive_content

                return machine_learning_detected_sensitive_content.MachineLearningDetectedSensitiveContent()
        return DetectedSensitiveContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import classification_attribute, classification_method, detected_sensitive_content_base, machine_learning_detected_sensitive_content, sensitive_content_location, sensitive_type_scope, sensitive_type_source

        fields: Dict[str, Callable[[Any], None]] = {
            "classificationAttributes": lambda n : setattr(self, 'classification_attributes', n.get_collection_of_object_values(classification_attribute.ClassificationAttribute)),
            "classificationMethod": lambda n : setattr(self, 'classification_method', n.get_enum_value(classification_method.ClassificationMethod)),
            "matches": lambda n : setattr(self, 'matches', n.get_collection_of_object_values(sensitive_content_location.SensitiveContentLocation)),
            "scope": lambda n : setattr(self, 'scope', n.get_enum_value(sensitive_type_scope.SensitiveTypeScope)),
            "sensitiveTypeSource": lambda n : setattr(self, 'sensitive_type_source', n.get_enum_value(sensitive_type_source.SensitiveTypeSource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def matches(self,) -> Optional[List[sensitive_content_location.SensitiveContentLocation]]:
        """
        Gets the matches property value. The matches property
        Returns: Optional[List[sensitive_content_location.SensitiveContentLocation]]
        """
        return self._matches
    
    @matches.setter
    def matches(self,value: Optional[List[sensitive_content_location.SensitiveContentLocation]] = None) -> None:
        """
        Sets the matches property value. The matches property
        Args:
            value: Value to set for the matches property.
        """
        self._matches = value
    
    @property
    def scope(self,) -> Optional[sensitive_type_scope.SensitiveTypeScope]:
        """
        Gets the scope property value. The scope property
        Returns: Optional[sensitive_type_scope.SensitiveTypeScope]
        """
        return self._scope
    
    @scope.setter
    def scope(self,value: Optional[sensitive_type_scope.SensitiveTypeScope] = None) -> None:
        """
        Sets the scope property value. The scope property
        Args:
            value: Value to set for the scope property.
        """
        self._scope = value
    
    @property
    def sensitive_type_source(self,) -> Optional[sensitive_type_source.SensitiveTypeSource]:
        """
        Gets the sensitiveTypeSource property value. The sensitiveTypeSource property
        Returns: Optional[sensitive_type_source.SensitiveTypeSource]
        """
        return self._sensitive_type_source
    
    @sensitive_type_source.setter
    def sensitive_type_source(self,value: Optional[sensitive_type_source.SensitiveTypeSource] = None) -> None:
        """
        Sets the sensitiveTypeSource property value. The sensitiveTypeSource property
        Args:
            value: Value to set for the sensitive_type_source property.
        """
        self._sensitive_type_source = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("classificationAttributes", self.classification_attributes)
        writer.write_enum_value("classificationMethod", self.classification_method)
        writer.write_collection_of_object_values("matches", self.matches)
        writer.write_enum_value("scope", self.scope)
        writer.write_enum_value("sensitiveTypeSource", self.sensitive_type_source)
    

