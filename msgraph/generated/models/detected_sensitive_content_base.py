from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DetectedSensitiveContentBase(AdditionalDataHolder, Parsable):
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
        Instantiates a new detectedSensitiveContentBase and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The confidence property
        self._confidence: Optional[int] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The id property
        self._id: Optional[Guid] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The recommendedConfidence property
        self._recommended_confidence: Optional[int] = None
        # The uniqueCount property
        self._unique_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DetectedSensitiveContentBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DetectedSensitiveContentBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DetectedSensitiveContentBase()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "confidence": lambda n : setattr(self, 'confidence', n.get_int_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_object_value(Guid)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recommended_confidence": lambda n : setattr(self, 'recommended_confidence', n.get_int_value()),
            "unique_count": lambda n : setattr(self, 'unique_count', n.get_int_value()),
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
    
    @property
    def recommended_confidence(self,) -> Optional[int]:
        """
        Gets the recommendedConfidence property value. The recommendedConfidence property
        Returns: Optional[int]
        """
        return self._recommended_confidence
    
    @recommended_confidence.setter
    def recommended_confidence(self,value: Optional[int] = None) -> None:
        """
        Sets the recommendedConfidence property value. The recommendedConfidence property
        Args:
            value: Value to set for the recommendedConfidence property.
        """
        self._recommended_confidence = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("confidence", self.confidence)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("recommendedConfidence", self.recommended_confidence)
        writer.write_int_value("uniqueCount", self.unique_count)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def unique_count(self,) -> Optional[int]:
        """
        Gets the uniqueCount property value. The uniqueCount property
        Returns: Optional[int]
        """
        return self._unique_count
    
    @unique_count.setter
    def unique_count(self,value: Optional[int] = None) -> None:
        """
        Sets the uniqueCount property value. The uniqueCount property
        Args:
            value: Value to set for the uniqueCount property.
        """
        self._unique_count = value
    

