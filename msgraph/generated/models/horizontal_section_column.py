from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, web_part

from . import entity

@dataclass
class HorizontalSectionColumn(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of WebParts in this column.
    webparts: Optional[List[web_part.WebPart]] = None
    # Width of the column. A horizontal section is divided into 12 grids. A column should have a value of 1-12 to represent its range spans. For example, there can be two columns both have a width of 6 in a section.
    width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HorizontalSectionColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HorizontalSectionColumn
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return HorizontalSectionColumn()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, web_part

        fields: Dict[str, Callable[[Any], None]] = {
            "webparts": lambda n : setattr(self, 'webparts', n.get_collection_of_object_values(web_part.WebPart)),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
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
        writer.write_collection_of_object_values("webparts", self.webparts)
        writer.write_int_value("width", self.width)
    

