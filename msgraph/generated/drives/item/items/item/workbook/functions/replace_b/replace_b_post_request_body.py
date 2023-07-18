from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.json import Json

@dataclass
class ReplaceBPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The newText property
    new_text: Optional[Json] = None
    # The numBytes property
    num_bytes: Optional[Json] = None
    # The oldText property
    old_text: Optional[Json] = None
    # The startNum property
    start_num: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReplaceBPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReplaceBPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ReplaceBPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.json import Json

        from ........models.json import Json

        fields: Dict[str, Callable[[Any], None]] = {
            "newText": lambda n : setattr(self, 'new_text', n.get_object_value(Json)),
            "numBytes": lambda n : setattr(self, 'num_bytes', n.get_object_value(Json)),
            "oldText": lambda n : setattr(self, 'old_text', n.get_object_value(Json)),
            "startNum": lambda n : setattr(self, 'start_num', n.get_object_value(Json)),
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
        writer.write_object_value("newText", self.new_text)
        writer.write_object_value("numBytes", self.num_bytes)
        writer.write_object_value("oldText", self.old_text)
        writer.write_object_value("startNum", self.start_num)
        writer.write_additional_data_value(self.additional_data)
    

