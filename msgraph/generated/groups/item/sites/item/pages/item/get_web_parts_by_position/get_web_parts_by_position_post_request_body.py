from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class GetWebPartsByPositionPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The columnId property
    column_id: Optional[float] = None
    # The horizontalSectionId property
    horizontal_section_id: Optional[float] = None
    # The isInVerticalSection property
    is_in_vertical_section: Optional[bool] = None
    # The webPartIndex property
    web_part_index: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetWebPartsByPositionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetWebPartsByPositionPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GetWebPartsByPositionPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "columnId": lambda n : setattr(self, 'column_id', n.get_float_value()),
            "horizontalSectionId": lambda n : setattr(self, 'horizontal_section_id', n.get_float_value()),
            "isInVerticalSection": lambda n : setattr(self, 'is_in_vertical_section', n.get_bool_value()),
            "webPartIndex": lambda n : setattr(self, 'web_part_index', n.get_float_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_float_value("columnId", self.column_id)
        writer.write_float_value("horizontalSectionId", self.horizontal_section_id)
        writer.write_bool_value("isInVerticalSection", self.is_in_vertical_section)
        writer.write_float_value("webPartIndex", self.web_part_index)
        writer.write_additional_data_value(self.additional_data)
    

