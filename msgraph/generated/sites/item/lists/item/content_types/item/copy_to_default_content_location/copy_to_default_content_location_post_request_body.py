from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.item_reference import ItemReference

@dataclass
class CopyToDefaultContentLocationPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The destinationFileName property
    destination_file_name: Optional[str] = None
    # The sourceFile property
    source_file: Optional[ItemReference] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CopyToDefaultContentLocationPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopyToDefaultContentLocationPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CopyToDefaultContentLocationPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.item_reference import ItemReference

        from ........models.item_reference import ItemReference

        fields: Dict[str, Callable[[Any], None]] = {
            "destinationFileName": lambda n : setattr(self, 'destination_file_name', n.get_str_value()),
            "sourceFile": lambda n : setattr(self, 'source_file', n.get_object_value(ItemReference)),
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
        writer.write_str_value("destinationFileName", self.destination_file_name)
        writer.write_object_value("sourceFile", self.source_file)
        writer.write_additional_data_value(self.additional_data)
    

