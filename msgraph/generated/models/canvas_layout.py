from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
horizontal_section = lazy_import('msgraph.generated.models.horizontal_section')
vertical_section = lazy_import('msgraph.generated.models.vertical_section')

class CanvasLayout(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new canvasLayout and sets the default values.
        """
        super().__init__()
        # Collection of horizontal sections on the SharePoint page.
        self._horizontal_sections: Optional[List[horizontal_section.HorizontalSection]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Vertical section on the SharePoint page.
        self._vertical_section: Optional[vertical_section.VerticalSection] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CanvasLayout:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CanvasLayout
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CanvasLayout()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "horizontal_sections": lambda n : setattr(self, 'horizontal_sections', n.get_collection_of_object_values(horizontal_section.HorizontalSection)),
            "vertical_section": lambda n : setattr(self, 'vertical_section', n.get_object_value(vertical_section.VerticalSection)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def horizontal_sections(self,) -> Optional[List[horizontal_section.HorizontalSection]]:
        """
        Gets the horizontalSections property value. Collection of horizontal sections on the SharePoint page.
        Returns: Optional[List[horizontal_section.HorizontalSection]]
        """
        return self._horizontal_sections
    
    @horizontal_sections.setter
    def horizontal_sections(self,value: Optional[List[horizontal_section.HorizontalSection]] = None) -> None:
        """
        Sets the horizontalSections property value. Collection of horizontal sections on the SharePoint page.
        Args:
            value: Value to set for the horizontalSections property.
        """
        self._horizontal_sections = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("horizontalSections", self.horizontal_sections)
        writer.write_object_value("verticalSection", self.vertical_section)
    
    @property
    def vertical_section(self,) -> Optional[vertical_section.VerticalSection]:
        """
        Gets the verticalSection property value. Vertical section on the SharePoint page.
        Returns: Optional[vertical_section.VerticalSection]
        """
        return self._vertical_section
    
    @vertical_section.setter
    def vertical_section(self,value: Optional[vertical_section.VerticalSection] = None) -> None:
        """
        Sets the verticalSection property value. Vertical section on the SharePoint page.
        Args:
            value: Value to set for the verticalSection property.
        """
        self._vertical_section = value
    

