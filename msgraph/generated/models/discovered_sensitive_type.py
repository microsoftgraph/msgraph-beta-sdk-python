from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

classification_attribute = lazy_import('msgraph.generated.models.classification_attribute')

class DiscoveredSensitiveType(AdditionalDataHolder, Parsable):
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
            value: Value to set for the classificationAttributes property.
        """
        self._classification_attributes = value
    
    @property
    def confidence(self,) -> Optional[int]:
        """
        Gets the confidence property value. The confidence property
        Returns: Optional[int]
        """
        return self._confidence
    
    @confidence.setter
    def confidence(self,value: Optional[int] = None) -> None:
        """
        Sets the confidence property value. The confidence property
        Args:
            value: Value to set for the confidence property.
        """
        self._confidence = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new discoveredSensitiveType and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The classificationAttributes property
        self._classification_attributes: Optional[List[classification_attribute.ClassificationAttribute]] = None
        # The confidence property
        self._confidence: Optional[int] = None
        # The count property
        self._count: Optional[int] = None
        # The id property
        self._id: Optional[Guid] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def count(self,) -> Optional[int]:
        """
        Gets the count property value. The count property
        Returns: Optional[int]
        """
        return self._count
    
    @count.setter
    def count(self,value: Optional[int] = None) -> None:
        """
        Sets the count property value. The count property
        Args:
            value: Value to set for the count property.
        """
        self._count = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DiscoveredSensitiveType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DiscoveredSensitiveType
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DiscoveredSensitiveType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "classification_attributes": lambda n : setattr(self, 'classification_attributes', n.get_collection_of_object_values(classification_attribute.ClassificationAttribute)),
            "confidence": lambda n : setattr(self, 'confidence', n.get_int_value()),
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_object_value(Guid)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[Guid]:
        """
        Gets the id property value. The id property
        Returns: Optional[Guid]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the id property value. The id property
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
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
        writer.write_collection_of_object_values("classificationAttributes", self.classification_attributes)
        writer.write_int_value("confidence", self.confidence)
        writer.write_int_value("count", self.count)
        writer.write_object_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

