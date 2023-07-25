from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...........models.json import Json

@dataclass
class SetPositionPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The endCell property
    end_cell: Optional[Json] = None
    # The startCell property
    start_cell: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SetPositionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SetPositionPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SetPositionPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...........models.json import Json

        from ...........models.json import Json

        fields: Dict[str, Callable[[Any], None]] = {
            "endCell": lambda n : setattr(self, 'end_cell', n.get_object_value(Json)),
            "startCell": lambda n : setattr(self, 'start_cell', n.get_object_value(Json)),
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
        writer.write_object_value("endCell", self.end_cell)
        writer.write_object_value("startCell", self.start_cell)
        writer.write_additional_data_value(self.additional_data)
    

