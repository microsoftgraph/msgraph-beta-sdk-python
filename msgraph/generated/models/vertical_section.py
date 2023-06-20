from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, section_emphasis_type, web_part

from . import entity

@dataclass
class VerticalSection(entity.Entity):
    # Enumeration value that indicates the emphasis of the section background. The possible values are: none, netural, soft, strong, unknownFutureValue.
    emphasis: Optional[section_emphasis_type.SectionEmphasisType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The set of web parts in this section.
    webparts: Optional[List[web_part.WebPart]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VerticalSection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VerticalSection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VerticalSection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, section_emphasis_type, web_part

        from . import entity, section_emphasis_type, web_part

        fields: Dict[str, Callable[[Any], None]] = {
            "emphasis": lambda n : setattr(self, 'emphasis', n.get_enum_value(section_emphasis_type.SectionEmphasisType)),
            "webparts": lambda n : setattr(self, 'webparts', n.get_collection_of_object_values(web_part.WebPart)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("emphasis", self.emphasis)
        writer.write_collection_of_object_values("webparts", self.webparts)
    

