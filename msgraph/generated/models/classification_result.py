from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class ClassificationResult(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new classificationResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The confidence level, 0 to 100, of the result.
        self._confidence_level: Optional[int] = None
        # The number of instances of the specific information type in the input.
        self._count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The GUID of the discovered sensitive information type.
        self._sensitive_type_id: Optional[str] = None
    
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
    def confidence_level(self,) -> Optional[int]:
        """
        Gets the confidenceLevel property value. The confidence level, 0 to 100, of the result.
        Returns: Optional[int]
        """
        return self._confidence_level
    
    @confidence_level.setter
    def confidence_level(self,value: Optional[int] = None) -> None:
        """
        Sets the confidenceLevel property value. The confidence level, 0 to 100, of the result.
        Args:
            value: Value to set for the confidence_level property.
        """
        self._confidence_level = value
    
    @property
    def count(self,) -> Optional[int]:
        """
        Gets the count property value. The number of instances of the specific information type in the input.
        Returns: Optional[int]
        """
        return self._count
    
    @count.setter
    def count(self,value: Optional[int] = None) -> None:
        """
        Sets the count property value. The number of instances of the specific information type in the input.
        Args:
            value: Value to set for the count property.
        """
        self._count = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ClassificationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ClassificationResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ClassificationResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "confidenceLevel": lambda n : setattr(self, 'confidence_level', n.get_int_value()),
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sensitiveTypeId": lambda n : setattr(self, 'sensitive_type_id', n.get_str_value()),
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def sensitive_type_id(self,) -> Optional[str]:
        """
        Gets the sensitiveTypeId property value. The GUID of the discovered sensitive information type.
        Returns: Optional[str]
        """
        return self._sensitive_type_id
    
    @sensitive_type_id.setter
    def sensitive_type_id(self,value: Optional[str] = None) -> None:
        """
        Sets the sensitiveTypeId property value. The GUID of the discovered sensitive information type.
        Args:
            value: Value to set for the sensitive_type_id property.
        """
        self._sensitive_type_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("confidenceLevel", self.confidence_level)
        writer.write_int_value("count", self.count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sensitiveTypeId", self.sensitive_type_id)
        writer.write_additional_data_value(self.additional_data)
    

