from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

information_protection_action = lazy_import('msgraph.generated.models.information_protection_action')
watermark_layout = lazy_import('msgraph.generated.models.watermark_layout')

class AddWatermarkAction(information_protection_action.InformationProtectionAction):
    def __init__(self,) -> None:
        """
        Instantiates a new AddWatermarkAction and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.addWatermarkAction"
        # Color of the font to use for the watermark.
        self._font_color: Optional[str] = None
        # Name of the font to use for the watermark.
        self._font_name: Optional[str] = None
        # Font size to use for the watermark.
        self._font_size: Optional[int] = None
        # The layout property
        self._layout: Optional[watermark_layout.WatermarkLayout] = None
        # The contents of the watermark itself.
        self._text: Optional[str] = None
        # The name of the UI element where the watermark should be placed.
        self._ui_element_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddWatermarkAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AddWatermarkAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AddWatermarkAction()
    
    @property
    def font_color(self,) -> Optional[str]:
        """
        Gets the fontColor property value. Color of the font to use for the watermark.
        Returns: Optional[str]
        """
        return self._font_color
    
    @font_color.setter
    def font_color(self,value: Optional[str] = None) -> None:
        """
        Sets the fontColor property value. Color of the font to use for the watermark.
        Args:
            value: Value to set for the fontColor property.
        """
        self._font_color = value
    
    @property
    def font_name(self,) -> Optional[str]:
        """
        Gets the fontName property value. Name of the font to use for the watermark.
        Returns: Optional[str]
        """
        return self._font_name
    
    @font_name.setter
    def font_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fontName property value. Name of the font to use for the watermark.
        Args:
            value: Value to set for the fontName property.
        """
        self._font_name = value
    
    @property
    def font_size(self,) -> Optional[int]:
        """
        Gets the fontSize property value. Font size to use for the watermark.
        Returns: Optional[int]
        """
        return self._font_size
    
    @font_size.setter
    def font_size(self,value: Optional[int] = None) -> None:
        """
        Sets the fontSize property value. Font size to use for the watermark.
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
            "font_name": lambda n : setattr(self, 'font_name', n.get_str_value()),
            "font_size": lambda n : setattr(self, 'font_size', n.get_int_value()),
            "layout": lambda n : setattr(self, 'layout', n.get_enum_value(watermark_layout.WatermarkLayout)),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "ui_element_name": lambda n : setattr(self, 'ui_element_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def layout(self,) -> Optional[watermark_layout.WatermarkLayout]:
        """
        Gets the layout property value. The layout property
        Returns: Optional[watermark_layout.WatermarkLayout]
        """
        return self._layout
    
    @layout.setter
    def layout(self,value: Optional[watermark_layout.WatermarkLayout] = None) -> None:
        """
        Sets the layout property value. The layout property
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
        writer.write_str_value("fontColor", self.font_color)
        writer.write_str_value("fontName", self.font_name)
        writer.write_int_value("fontSize", self.font_size)
        writer.write_enum_value("layout", self.layout)
        writer.write_str_value("text", self.text)
        writer.write_str_value("uiElementName", self.ui_element_name)
    
    @property
    def text(self,) -> Optional[str]:
        """
        Gets the text property value. The contents of the watermark itself.
        Returns: Optional[str]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[str] = None) -> None:
        """
        Sets the text property value. The contents of the watermark itself.
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    
    @property
    def ui_element_name(self,) -> Optional[str]:
        """
        Gets the uiElementName property value. The name of the UI element where the watermark should be placed.
        Returns: Optional[str]
        """
        return self._ui_element_name
    
    @ui_element_name.setter
    def ui_element_name(self,value: Optional[str] = None) -> None:
        """
        Sets the uiElementName property value. The name of the UI element where the watermark should be placed.
        Args:
            value: Value to set for the uiElementName property.
        """
        self._ui_element_name = value
    

