from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

filter_operand = lazy_import('msgraph.generated.models.filter_operand')

class FilterClause(AdditionalDataHolder, Parsable):
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
        Instantiates a new filterClause and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Name of the operator to be applied to the source and target operands. Must be one of the supported operators. Supported operators can be discovered.
        self._operator_name: Optional[str] = None
        # Name of source operand (the operand being tested). The source operand name must match one of the attribute names on the source object.
        self._source_operand_name: Optional[str] = None
        # Values that the source operand will be tested against.
        self._target_operand: Optional[filter_operand.FilterOperand] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FilterClause:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FilterClause
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FilterClause()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operator_name": lambda n : setattr(self, 'operator_name', n.get_str_value()),
            "source_operand_name": lambda n : setattr(self, 'source_operand_name', n.get_str_value()),
            "target_operand": lambda n : setattr(self, 'target_operand', n.get_object_value(filter_operand.FilterOperand)),
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def operator_name(self,) -> Optional[str]:
        """
        Gets the operatorName property value. Name of the operator to be applied to the source and target operands. Must be one of the supported operators. Supported operators can be discovered.
        Returns: Optional[str]
        """
        return self._operator_name
    
    @operator_name.setter
    def operator_name(self,value: Optional[str] = None) -> None:
        """
        Sets the operatorName property value. Name of the operator to be applied to the source and target operands. Must be one of the supported operators. Supported operators can be discovered.
        Args:
            value: Value to set for the operatorName property.
        """
        self._operator_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operatorName", self.operator_name)
        writer.write_str_value("sourceOperandName", self.source_operand_name)
        writer.write_object_value("targetOperand", self.target_operand)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_operand_name(self,) -> Optional[str]:
        """
        Gets the sourceOperandName property value. Name of source operand (the operand being tested). The source operand name must match one of the attribute names on the source object.
        Returns: Optional[str]
        """
        return self._source_operand_name
    
    @source_operand_name.setter
    def source_operand_name(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceOperandName property value. Name of source operand (the operand being tested). The source operand name must match one of the attribute names on the source object.
        Args:
            value: Value to set for the sourceOperandName property.
        """
        self._source_operand_name = value
    
    @property
    def target_operand(self,) -> Optional[filter_operand.FilterOperand]:
        """
        Gets the targetOperand property value. Values that the source operand will be tested against.
        Returns: Optional[filter_operand.FilterOperand]
        """
        return self._target_operand
    
    @target_operand.setter
    def target_operand(self,value: Optional[filter_operand.FilterOperand] = None) -> None:
        """
        Sets the targetOperand property value. Values that the source operand will be tested against.
        Args:
            value: Value to set for the targetOperand property.
        """
        self._target_operand = value
    

