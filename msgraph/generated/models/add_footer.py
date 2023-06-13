from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alignment, mark_content

from . import mark_content

@dataclass
class AddFooter(mark_content.MarkContent):
    odata_type = "#microsoft.graph.addFooter"
    # The alignment property
    alignment: Optional[alignment.Alignment] = None
    # The margin property
    margin: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddFooter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AddFooter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AddFooter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alignment, mark_content

        fields: Dict[str, Callable[[Any], None]] = {
            "alignment": lambda n : setattr(self, 'alignment', n.get_enum_value(alignment.Alignment)),
            "margin": lambda n : setattr(self, 'margin', n.get_int_value()),
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
        writer.write_enum_value("alignment", self.alignment)
        writer.write_int_value("margin", self.margin)
    

