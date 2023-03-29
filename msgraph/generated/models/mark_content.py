from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import add_footer, add_header, add_watermark, label_action_base

from . import label_action_base

class MarkContent(label_action_base.LabelActionBase):
    def __init__(self,) -> None:
        """
        Instantiates a new MarkContent and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.markContent"
        # The fontColor property
        self._font_color: Optional[str] = None
        # The fontSize property
        self._font_size: Optional[int] = None
        # The text property
        self._text: Optional[str] = None
    
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
    
    @property
    def font_color(self,) -> Optional[str]:
        """
        Gets the fontColor property value. The fontColor property
        Returns: Optional[str]
        """
        return self._font_color
    
    @font_color.setter
    def font_color(self,value: Optional[str] = None) -> None:
        """
        Sets the fontColor property value. The fontColor property
        Args:
            value: Value to set for the font_color property.
        """
        self._font_color = value
    
    @property
    def font_size(self,) -> Optional[int]:
        """
        Gets the fontSize property value. The fontSize property
        Returns: Optional[int]
        """
        return self._font_size
    
    @font_size.setter
    def font_size(self,value: Optional[int] = None) -> None:
        """
        Sets the fontSize property value. The fontSize property
        Args:
            value: Value to set for the font_size property.
        """
        self._font_size = value
    
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
    
    @property
    def text(self,) -> Optional[str]:
        """
        Gets the text property value. The text property
        Returns: Optional[str]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[str] = None) -> None:
        """
        Sets the text property value. The text property
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    

