from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
horizontal_section_column = lazy_import('msgraph.generated.models.horizontal_section_column')
horizontal_section_layout_type = lazy_import('msgraph.generated.models.horizontal_section_layout_type')
section_emphasis_type = lazy_import('msgraph.generated.models.section_emphasis_type')

class HorizontalSection(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def columns(self,) -> Optional[List[horizontal_section_column.HorizontalSectionColumn]]:
        """
        Gets the columns property value. The set of vertical columns in this section.
        Returns: Optional[List[horizontal_section_column.HorizontalSectionColumn]]
        """
        return self._columns
    
    @columns.setter
    def columns(self,value: Optional[List[horizontal_section_column.HorizontalSectionColumn]] = None) -> None:
        """
        Sets the columns property value. The set of vertical columns in this section.
        Args:
            value: Value to set for the columns property.
        """
        self._columns = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new horizontalSection and sets the default values.
        """
        super().__init__()
        # The set of vertical columns in this section.
        self._columns: Optional[List[horizontal_section_column.HorizontalSectionColumn]] = None
        # Enumeration value that indicates the emphasis of the section background. The possible values are: none, netural, soft, strong, unknownFutureValue.
        self._emphasis: Optional[section_emphasis_type.SectionEmphasisType] = None
        # Layout type of the section. The possible values are: none, oneColumn, twoColumns, threeColumns, oneThirdLeftColumn, oneThirdRightColumn, fullWidth, unknownFutureValue.
        self._layout: Optional[horizontal_section_layout_type.HorizontalSectionLayoutType] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HorizontalSection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HorizontalSection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return HorizontalSection()
    
    @property
    def emphasis(self,) -> Optional[section_emphasis_type.SectionEmphasisType]:
        """
        Gets the emphasis property value. Enumeration value that indicates the emphasis of the section background. The possible values are: none, netural, soft, strong, unknownFutureValue.
        Returns: Optional[section_emphasis_type.SectionEmphasisType]
        """
        return self._emphasis
    
    @emphasis.setter
    def emphasis(self,value: Optional[section_emphasis_type.SectionEmphasisType] = None) -> None:
        """
        Sets the emphasis property value. Enumeration value that indicates the emphasis of the section background. The possible values are: none, netural, soft, strong, unknownFutureValue.
        Args:
            value: Value to set for the emphasis property.
        """
        self._emphasis = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(horizontal_section_column.HorizontalSectionColumn)),
            "emphasis": lambda n : setattr(self, 'emphasis', n.get_enum_value(section_emphasis_type.SectionEmphasisType)),
            "layout": lambda n : setattr(self, 'layout', n.get_enum_value(horizontal_section_layout_type.HorizontalSectionLayoutType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def layout(self,) -> Optional[horizontal_section_layout_type.HorizontalSectionLayoutType]:
        """
        Gets the layout property value. Layout type of the section. The possible values are: none, oneColumn, twoColumns, threeColumns, oneThirdLeftColumn, oneThirdRightColumn, fullWidth, unknownFutureValue.
        Returns: Optional[horizontal_section_layout_type.HorizontalSectionLayoutType]
        """
        return self._layout
    
    @layout.setter
    def layout(self,value: Optional[horizontal_section_layout_type.HorizontalSectionLayoutType] = None) -> None:
        """
        Sets the layout property value. Layout type of the section. The possible values are: none, oneColumn, twoColumns, threeColumns, oneThirdLeftColumn, oneThirdRightColumn, fullWidth, unknownFutureValue.
        Args:
            value: Value to set for the layout property.
        """
        self._layout = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("columns", self.columns)
        writer.write_enum_value("emphasis", self.emphasis)
        writer.write_enum_value("layout", self.layout)
    

