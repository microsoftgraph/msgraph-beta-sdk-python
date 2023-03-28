from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class IntegerRange(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new integerRange and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The inclusive upper bound of the integer range.
        self._end: Optional[int] = None
        # The maximum property
        self._maximum: Optional[int] = None
        # The minimum property
        self._minimum: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The inclusive lower bound of the integer range.
        self._start: Optional[int] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IntegerRange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IntegerRange
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IntegerRange()
    
    @property
    def end(self,) -> Optional[int]:
        """
        Gets the end property value. The inclusive upper bound of the integer range.
        Returns: Optional[int]
        """
        return self._end
    
    @end.setter
    def end(self,value: Optional[int] = None) -> None:
        """
        Sets the end property value. The inclusive upper bound of the integer range.
        Args:
            value: Value to set for the end property.
        """
        self._end = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "end": lambda n : setattr(self, 'end', n.get_int_value()),
            "maximum": lambda n : setattr(self, 'maximum', n.get_int_value()),
            "minimum": lambda n : setattr(self, 'minimum', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "start": lambda n : setattr(self, 'start', n.get_int_value()),
        }
        return fields
    
    @property
    def maximum(self,) -> Optional[int]:
        """
        Gets the maximum property value. The maximum property
        Returns: Optional[int]
        """
        return self._maximum
    
    @maximum.setter
    def maximum(self,value: Optional[int] = None) -> None:
        """
        Sets the maximum property value. The maximum property
        Args:
            value: Value to set for the maximum property.
        """
        self._maximum = value
    
    @property
    def minimum(self,) -> Optional[int]:
        """
        Gets the minimum property value. The minimum property
        Returns: Optional[int]
        """
        return self._minimum
    
    @minimum.setter
    def minimum(self,value: Optional[int] = None) -> None:
        """
        Sets the minimum property value. The minimum property
        Args:
            value: Value to set for the minimum property.
        """
        self._minimum = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("end", self.end)
        writer.write_int_value("maximum", self.maximum)
        writer.write_int_value("minimum", self.minimum)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("start", self.start)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start(self,) -> Optional[int]:
        """
        Gets the start property value. The inclusive lower bound of the integer range.
        Returns: Optional[int]
        """
        return self._start
    
    @start.setter
    def start(self,value: Optional[int] = None) -> None:
        """
        Sets the start property value. The inclusive lower bound of the integer range.
        Args:
            value: Value to set for the start property.
        """
        self._start = value
    

