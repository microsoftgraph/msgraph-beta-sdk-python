from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ApplyCustomFilterPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The criteria1 property
    criteria1: Optional[str] = None
    # The criteria2 property
    criteria2: Optional[str] = None
    # The oper property
    oper: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplyCustomFilterPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplyCustomFilterPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ApplyCustomFilterPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "criteria1": lambda n : setattr(self, 'criteria1', n.get_str_value()),
            "criteria2": lambda n : setattr(self, 'criteria2', n.get_str_value()),
            "oper": lambda n : setattr(self, 'oper', n.get_str_value()),
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
        writer.write_str_value("criteria1", self.criteria1)
        writer.write_str_value("criteria2", self.criteria2)
        writer.write_str_value("oper", self.oper)
        writer.write_additional_data_value(self.additional_data)
    

