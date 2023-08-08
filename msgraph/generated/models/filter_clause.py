from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filter_operand import FilterOperand

@dataclass
class FilterClause(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Name of the operator to be applied to the source and target operands. Must be one of the supported operators. Supported operators can be discovered.
    operator_name: Optional[str] = None
    # Name of source operand (the operand being tested). The source operand name must match one of the attribute names on the source object.
    source_operand_name: Optional[str] = None
    # Values that the source operand will be tested against.
    target_operand: Optional[FilterOperand] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FilterClause:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilterClause
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return FilterClause()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .filter_operand import FilterOperand

        from .filter_operand import FilterOperand

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operatorName": lambda n : setattr(self, 'operator_name', n.get_str_value()),
            "sourceOperandName": lambda n : setattr(self, 'source_operand_name', n.get_str_value()),
            "targetOperand": lambda n : setattr(self, 'target_operand', n.get_object_value(FilterOperand)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operatorName", self.operator_name)
        writer.write_str_value("sourceOperandName", self.source_operand_name)
        writer.write_object_value("targetOperand", self.target_operand)
        writer.write_additional_data_value(self.additional_data)
    

