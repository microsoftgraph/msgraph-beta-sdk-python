from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, horizontal_section_column, horizontal_section_layout_type, section_emphasis_type

from . import entity

@dataclass
class HorizontalSection(entity.Entity):
    # The set of vertical columns in this section.
    columns: Optional[List[horizontal_section_column.HorizontalSectionColumn]] = None
    # Enumeration value that indicates the emphasis of the section background. The possible values are: none, netural, soft, strong, unknownFutureValue.
    emphasis: Optional[section_emphasis_type.SectionEmphasisType] = None
    # Layout type of the section. The possible values are: none, oneColumn, twoColumns, threeColumns, oneThirdLeftColumn, oneThirdRightColumn, fullWidth, unknownFutureValue.
    layout: Optional[horizontal_section_layout_type.HorizontalSectionLayoutType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HorizontalSection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HorizontalSection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return HorizontalSection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, horizontal_section_column, horizontal_section_layout_type, section_emphasis_type

        from . import entity, horizontal_section_column, horizontal_section_layout_type, section_emphasis_type

        fields: Dict[str, Callable[[Any], None]] = {
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(horizontal_section_column.HorizontalSectionColumn)),
            "emphasis": lambda n : setattr(self, 'emphasis', n.get_enum_value(section_emphasis_type.SectionEmphasisType)),
            "layout": lambda n : setattr(self, 'layout', n.get_enum_value(horizontal_section_layout_type.HorizontalSectionLayoutType)),
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
        writer.write_collection_of_object_values("columns", self.columns)
        writer.write_enum_value("emphasis", self.emphasis)
        writer.write_enum_value("layout", self.layout)
    

