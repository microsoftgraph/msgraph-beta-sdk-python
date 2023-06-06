from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import web_part, web_part_data

from . import web_part

@dataclass
class StandardWebPart(web_part.WebPart):
    odata_type = "#microsoft.graph.standardWebPart"
    # Data of the webPart.
    data: Optional[web_part_data.WebPartData] = None
    # A Guid which indicates the type of the webParts
    web_part_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> StandardWebPart:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: StandardWebPart
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return StandardWebPart()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import web_part, web_part_data

        fields: Dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(web_part_data.WebPartData)),
            "webPartType": lambda n : setattr(self, 'web_part_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("data", self.data)
        writer.write_str_value("webPartType", self.web_part_type)
    

