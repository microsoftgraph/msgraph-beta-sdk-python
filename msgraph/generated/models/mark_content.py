from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import add_footer, add_header, add_watermark, label_action_base

from . import label_action_base

@dataclass
class MarkContent(label_action_base.LabelActionBase):
    odata_type = "#microsoft.graph.markContent"
    # The fontColor property
    font_color: Optional[str] = None
    # The fontSize property
    font_size: Optional[int] = None
    # The text property
    text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MarkContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MarkContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.addFooter":
                from . import add_footer

                return add_footer.AddFooter()
            if mapping_value == "#microsoft.graph.addHeader":
                from . import add_header

                return add_header.AddHeader()
            if mapping_value == "#microsoft.graph.addWatermark":
                from . import add_watermark

                return add_watermark.AddWatermark()
        return MarkContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import add_footer, add_header, add_watermark, label_action_base

        fields: Dict[str, Callable[[Any], None]] = {
            "fontColor": lambda n : setattr(self, 'font_color', n.get_str_value()),
            "fontSize": lambda n : setattr(self, 'font_size', n.get_int_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_str_value("fontColor", self.font_color)
        writer.write_int_value("fontSize", self.font_size)
        writer.write_str_value("text", self.text)
    

