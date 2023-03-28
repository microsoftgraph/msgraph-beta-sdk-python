from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class CalculatedColumn(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new calculatedColumn and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # For dateTime output types, the format of the value. Must be one of dateOnly or dateTime.
        self._format: Optional[str] = None
        # The formula used to compute the value for this column.
        self._formula: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The output type used to format values in this column. Must be one of boolean, currency, dateTime, number, or text.
        self._output_type: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CalculatedColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CalculatedColumn
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CalculatedColumn()
    
    @property
    def format(self,) -> Optional[str]:
        """
        Gets the format property value. For dateTime output types, the format of the value. Must be one of dateOnly or dateTime.
        Returns: Optional[str]
        """
        return self._format
    
    @format.setter
    def format(self,value: Optional[str] = None) -> None:
        """
        Sets the format property value. For dateTime output types, the format of the value. Must be one of dateOnly or dateTime.
        Args:
            value: Value to set for the format property.
        """
        self._format = value
    
    @property
    def formula(self,) -> Optional[str]:
        """
        Gets the formula property value. The formula used to compute the value for this column.
        Returns: Optional[str]
        """
        return self._formula
    
    @formula.setter
    def formula(self,value: Optional[str] = None) -> None:
        """
        Sets the formula property value. The formula used to compute the value for this column.
        Args:
            value: Value to set for the formula property.
        """
        self._formula = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_str_value()),
            "formula": lambda n : setattr(self, 'formula', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "outputType": lambda n : setattr(self, 'output_type', n.get_str_value()),
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
    def output_type(self,) -> Optional[str]:
        """
        Gets the outputType property value. The output type used to format values in this column. Must be one of boolean, currency, dateTime, number, or text.
        Returns: Optional[str]
        """
        return self._output_type
    
    @output_type.setter
    def output_type(self,value: Optional[str] = None) -> None:
        """
        Sets the outputType property value. The output type used to format values in this column. Must be one of boolean, currency, dateTime, number, or text.
        Args:
            value: Value to set for the output_type property.
        """
        self._output_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("format", self.format)
        writer.write_str_value("formula", self.formula)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("outputType", self.output_type)
        writer.write_additional_data_value(self.additional_data)
    

