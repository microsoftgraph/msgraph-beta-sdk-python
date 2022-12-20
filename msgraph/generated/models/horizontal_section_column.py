from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
web_part = lazy_import('msgraph.generated.models.web_part')

class HorizontalSectionColumn(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new horizontalSectionColumn and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The collection of WebParts in this column.
        self._webparts: Optional[List[web_part.WebPart]] = None
        # Width of the column. A horizontal section is divided into 12 grids. A column should have a value of 1-12 to represent its range spans. For example, there can be two columns both have a width of 6 in a section.
        self._width: Optional[int] = None
    
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
        fields = {
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
    
    @property
    def webparts(self,) -> Optional[List[web_part.WebPart]]:
        """
        Gets the webparts property value. The collection of WebParts in this column.
        Returns: Optional[List[web_part.WebPart]]
        """
        return self._webparts
    
    @webparts.setter
    def webparts(self,value: Optional[List[web_part.WebPart]] = None) -> None:
        """
        Sets the webparts property value. The collection of WebParts in this column.
        Args:
            value: Value to set for the webparts property.
        """
        self._webparts = value
    
    @property
    def width(self,) -> Optional[int]:
        """
        Gets the width property value. Width of the column. A horizontal section is divided into 12 grids. A column should have a value of 1-12 to represent its range spans. For example, there can be two columns both have a width of 6 in a section.
        Returns: Optional[int]
        """
        return self._width
    
    @width.setter
    def width(self,value: Optional[int] = None) -> None:
        """
        Sets the width property value. Width of the column. A horizontal section is divided into 12 grids. A column should have a value of 1-12 to represent its range spans. For example, there can be two columns both have a width of 6 in a section.
        Args:
            value: Value to set for the width property.
        """
        self._width = value
    

