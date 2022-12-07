from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

label_action_base = lazy_import('msgraph.generated.models.label_action_base')

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
            value: Value to set for the fontColor property.
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
            value: Value to set for the fontSize property.
        """
        self._font_size = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "font_color": lambda n : setattr(self, 'font_color', n.get_str_value()),
            "font_size": lambda n : setattr(self, 'font_size', n.get_int_value()),
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
    

