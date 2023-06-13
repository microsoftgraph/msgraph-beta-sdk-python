from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import content_alignment, information_protection_action

from . import information_protection_action

@dataclass
class AddContentHeaderAction(information_protection_action.InformationProtectionAction):
    odata_type = "#microsoft.graph.addContentHeaderAction"
    # The alignment property
    alignment: Optional[content_alignment.ContentAlignment] = None
    # Color of the font to use for the header.
    font_color: Optional[str] = None
    # Name of the font to use for the header.
    font_name: Optional[str] = None
    # Font size to use for the header.
    font_size: Optional[int] = None
    # The margin of the header from the top of the document.
    margin: Optional[int] = None
    # The contents of the header itself.
    text: Optional[str] = None
    # The name of the UI element where the header should be placed.
    ui_element_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddContentHeaderAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AddContentHeaderAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AddContentHeaderAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import content_alignment, information_protection_action

        fields: Dict[str, Callable[[Any], None]] = {
            "alignment": lambda n : setattr(self, 'alignment', n.get_enum_value(content_alignment.ContentAlignment)),
            "fontColor": lambda n : setattr(self, 'font_color', n.get_str_value()),
            "fontName": lambda n : setattr(self, 'font_name', n.get_str_value()),
            "fontSize": lambda n : setattr(self, 'font_size', n.get_int_value()),
            "margin": lambda n : setattr(self, 'margin', n.get_int_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "uiElementName": lambda n : setattr(self, 'ui_element_name', n.get_str_value()),
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
        writer.write_str_value("fontColor", self.font_color)
        writer.write_str_value("fontName", self.font_name)
        writer.write_int_value("fontSize", self.font_size)
        writer.write_int_value("margin", self.margin)
        writer.write_str_value("text", self.text)
        writer.write_str_value("uiElementName", self.ui_element_name)
    

