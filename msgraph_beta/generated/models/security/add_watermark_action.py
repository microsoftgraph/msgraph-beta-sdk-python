from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .information_protection_action import InformationProtectionAction
    from .watermark_layout import WatermarkLayout

from .information_protection_action import InformationProtectionAction

@dataclass
class AddWatermarkAction(InformationProtectionAction):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.addWatermarkAction"
    # Color of the font to use for the watermark.
    font_color: Optional[str] = None
    # Name of the font to use for the watermark.
    font_name: Optional[str] = None
    # Font size to use for the watermark.
    font_size: Optional[int] = None
    # The layout property
    layout: Optional[WatermarkLayout] = None
    # The contents of the watermark itself.
    text: Optional[str] = None
    # The name of the UI element where the watermark should be placed.
    ui_element_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AddWatermarkAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AddWatermarkAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AddWatermarkAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .information_protection_action import InformationProtectionAction
        from .watermark_layout import WatermarkLayout

        from .information_protection_action import InformationProtectionAction
        from .watermark_layout import WatermarkLayout

        fields: Dict[str, Callable[[Any], None]] = {
            "fontColor": lambda n : setattr(self, 'font_color', n.get_str_value()),
            "fontName": lambda n : setattr(self, 'font_name', n.get_str_value()),
            "fontSize": lambda n : setattr(self, 'font_size', n.get_int_value()),
            "layout": lambda n : setattr(self, 'layout', n.get_enum_value(WatermarkLayout)),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "uiElementName": lambda n : setattr(self, 'ui_element_name', n.get_str_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("fontColor", self.font_color)
        writer.write_str_value("fontName", self.font_name)
        writer.write_int_value("fontSize", self.font_size)
        writer.write_enum_value("layout", self.layout)
        writer.write_str_value("text", self.text)
        writer.write_str_value("uiElementName", self.ui_element_name)
    

