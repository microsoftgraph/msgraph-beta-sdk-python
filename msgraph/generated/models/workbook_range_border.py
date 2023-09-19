from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class WorkbookRangeBorder(Entity):
    # HTML color code representing the color of the border line, of the form #RRGGBB (for example 'FFA500') or as a named HTML color (for example 'orange').
    color: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Constant value that indicates the specific side of the border. Possible values are: EdgeTop, EdgeBottom, EdgeLeft, EdgeRight, InsideVertical, InsideHorizontal, DiagonalDown, DiagonalUp. Read-only.
    side_index: Optional[str] = None
    # One of the constants of line style specifying the line style for the border. Possible values are: None, Continuous, Dash, DashDot, DashDotDot, Dot, Double, SlantDashDot.
    style: Optional[str] = None
    # Specifies the weight of the border around a range. Possible values are: Hairline, Thin, Medium, Thick.
    weight: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookRangeBorder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookRangeBorder
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WorkbookRangeBorder()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "sideIndex": lambda n : setattr(self, 'side_index', n.get_str_value()),
            "style": lambda n : setattr(self, 'style', n.get_str_value()),
            "weight": lambda n : setattr(self, 'weight', n.get_str_value()),
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
        writer.write_str_value("color", self.color)
        writer.write_str_value("sideIndex", self.side_index)
        writer.write_str_value("style", self.style)
        writer.write_str_value("weight", self.weight)
    

