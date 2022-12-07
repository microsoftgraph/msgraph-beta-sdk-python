from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

match_location = lazy_import('msgraph.generated.models.match_location')

class ContentClassification(AdditionalDataHolder, Parsable):
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
        Instantiates a new contentClassification and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The confidence property
        self._confidence: Optional[int] = None
        # The matches property
        self._matches: Optional[List[match_location.MatchLocation]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The sensitiveTypeId property
        self._sensitive_type_id: Optional[str] = None
        # The uniqueCount property
        self._unique_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ContentClassification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ContentClassification
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ContentClassification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "confidence": lambda n : setattr(self, 'confidence', n.get_int_value()),
            "matches": lambda n : setattr(self, 'matches', n.get_collection_of_object_values(match_location.MatchLocation)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sensitive_type_id": lambda n : setattr(self, 'sensitive_type_id', n.get_str_value()),
            "unique_count": lambda n : setattr(self, 'unique_count', n.get_int_value()),
        }
        return fields
    
    @property
    def matches(self,) -> Optional[List[match_location.MatchLocation]]:
        """
        Gets the matches property value. The matches property
        Returns: Optional[List[match_location.MatchLocation]]
        """
        return self._matches
    
    @matches.setter
    def matches(self,value: Optional[List[match_location.MatchLocation]] = None) -> None:
        """
        Sets the matches property value. The matches property
        Args:
            value: Value to set for the matches property.
        """
        self._matches = value
    
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
    def sensitive_type_id(self,) -> Optional[str]:
        """
        Gets the sensitiveTypeId property value. The sensitiveTypeId property
        Returns: Optional[str]
        """
        return self._sensitive_type_id
    
    @sensitive_type_id.setter
    def sensitive_type_id(self,value: Optional[str] = None) -> None:
        """
        Sets the sensitiveTypeId property value. The sensitiveTypeId property
        Args:
            value: Value to set for the sensitiveTypeId property.
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
        writer.write_int_value("confidence", self.confidence)
        writer.write_collection_of_object_values("matches", self.matches)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sensitiveTypeId", self.sensitive_type_id)
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
    

