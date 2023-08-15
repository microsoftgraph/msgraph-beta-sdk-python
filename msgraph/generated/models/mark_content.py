from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .add_footer import AddFooter
    from .add_header import AddHeader
    from .add_watermark import AddWatermark
    from .label_action_base import LabelActionBase

from .label_action_base import LabelActionBase

@dataclass
class MarkContent(LabelActionBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.markContent"
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
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MarkContent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addFooter".casefold():
            from .add_footer import AddFooter

            return AddFooter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addHeader".casefold():
            from .add_header import AddHeader

            return AddHeader()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addWatermark".casefold():
            from .add_watermark import AddWatermark

            return AddWatermark()
        return MarkContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .add_footer import AddFooter
        from .add_header import AddHeader
        from .add_watermark import AddWatermark
        from .label_action_base import LabelActionBase

        from .add_footer import AddFooter
        from .add_header import AddHeader
        from .add_watermark import AddWatermark
        from .label_action_base import LabelActionBase

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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("fontColor", self.font_color)
        writer.write_int_value("fontSize", self.font_size)
        writer.write_str_value("text", self.text)
    

