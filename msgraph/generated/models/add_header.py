from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alignment import Alignment
    from .mark_content import MarkContent

from .mark_content import MarkContent

@dataclass
class AddHeader(MarkContent):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.addHeader"
    # The alignment property
    alignment: Optional[Alignment] = None
    # The margin property
    margin: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddHeader:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AddHeader
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AddHeader()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alignment import Alignment
        from .mark_content import MarkContent

        from .alignment import Alignment
        from .mark_content import MarkContent

        fields: Dict[str, Callable[[Any], None]] = {
            "alignment": lambda n : setattr(self, 'alignment', n.get_enum_value(Alignment)),
            "margin": lambda n : setattr(self, 'margin', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("alignment", self.alignment)
        writer.write_int_value("margin", self.margin)
    

