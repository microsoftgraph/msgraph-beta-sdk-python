from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class NumberRange(AdditionalDataHolder, Parsable):
    """
    Number Range definition.
    """
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new numberRange and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Lower number.
        self._lower_number: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Upper number.
        self._upper_number: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NumberRange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NumberRange
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return NumberRange()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "lower_number": lambda n : setattr(self, 'lower_number', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "upper_number": lambda n : setattr(self, 'upper_number', n.get_int_value()),
        }
        return fields
    
    @property
    def lower_number(self,) -> Optional[int]:
        """
        Gets the lowerNumber property value. Lower number.
        Returns: Optional[int]
        """
        return self._lower_number
    
    @lower_number.setter
    def lower_number(self,value: Optional[int] = None) -> None:
        """
        Sets the lowerNumber property value. Lower number.
        Args:
            value: Value to set for the lowerNumber property.
        """
        self._lower_number = value
    
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
        writer.write_int_value("lowerNumber", self.lower_number)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("upperNumber", self.upper_number)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def upper_number(self,) -> Optional[int]:
        """
        Gets the upperNumber property value. Upper number.
        Returns: Optional[int]
        """
        return self._upper_number
    
    @upper_number.setter
    def upper_number(self,value: Optional[int] = None) -> None:
        """
        Sets the upperNumber property value. Upper number.
        Args:
            value: Value to set for the upperNumber property.
        """
        self._upper_number = value
    

