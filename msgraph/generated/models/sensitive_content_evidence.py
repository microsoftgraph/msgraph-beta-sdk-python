from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class SensitiveContentEvidence(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new sensitiveContentEvidence and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The length property
        self._length: Optional[int] = None
        # The match property
        self._match: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The offset property
        self._offset: Optional[int] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SensitiveContentEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SensitiveContentEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SensitiveContentEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "length": lambda n : setattr(self, 'length', n.get_int_value()),
            "match": lambda n : setattr(self, 'match', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offset": lambda n : setattr(self, 'offset', n.get_int_value()),
        }
        return fields
    
    @property
    def length(self,) -> Optional[int]:
        """
        Gets the length property value. The length property
        Returns: Optional[int]
        """
        return self._length
    
    @length.setter
    def length(self,value: Optional[int] = None) -> None:
        """
        Sets the length property value. The length property
        Args:
            value: Value to set for the length property.
        """
        self._length = value
    
    @property
    def match(self,) -> Optional[str]:
        """
        Gets the match property value. The match property
        Returns: Optional[str]
        """
        return self._match
    
    @match.setter
    def match(self,value: Optional[str] = None) -> None:
        """
        Sets the match property value. The match property
        Args:
            value: Value to set for the match property.
        """
        self._match = value
    
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
    def offset(self,) -> Optional[int]:
        """
        Gets the offset property value. The offset property
        Returns: Optional[int]
        """
        return self._offset
    
    @offset.setter
    def offset(self,value: Optional[int] = None) -> None:
        """
        Sets the offset property value. The offset property
        Args:
            value: Value to set for the offset property.
        """
        self._offset = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("length", self.length)
        writer.write_str_value("match", self.match)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("offset", self.offset)
        writer.write_additional_data_value(self.additional_data)
    

