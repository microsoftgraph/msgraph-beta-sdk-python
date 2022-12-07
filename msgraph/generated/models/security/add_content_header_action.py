from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

content_alignment = lazy_import('msgraph.generated.models.security.content_alignment')
information_protection_action = lazy_import('msgraph.generated.models.security.information_protection_action')

class AddContentHeaderAction(information_protection_action.InformationProtectionAction):
    @property
    def alignment(self,) -> Optional[content_alignment.ContentAlignment]:
        """
        Gets the alignment property value. The alignment property
        Returns: Optional[content_alignment.ContentAlignment]
        """
        return self._alignment
    
    @alignment.setter
    def alignment(self,value: Optional[content_alignment.ContentAlignment] = None) -> None:
        """
        Sets the alignment property value. The alignment property
        Args:
            value: Value to set for the alignment property.
        """
        self._alignment = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AddContentHeaderAction and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.addContentHeaderAction"
        # The alignment property
        self._alignment: Optional[content_alignment.ContentAlignment] = None
        # Color of the font to use for the header.
        self._font_color: Optional[str] = None
        # Name of the font to use for the header.
        self._font_name: Optional[str] = None
        # Font size to use for the header.
        self._font_size: Optional[int] = None
        # The margin of the header from the top of the document.
        self._margin: Optional[int] = None
        # The contents of the header itself.
        self._text: Optional[str] = None
        # The name of the UI element where the header should be placed.
        self._ui_element_name: Optional[str] = None
    
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
    
    @property
    def font_color(self,) -> Optional[str]:
        """
        Gets the fontColor property value. Color of the font to use for the header.
        Returns: Optional[str]
        """
        return self._font_color
    
    @font_color.setter
    def font_color(self,value: Optional[str] = None) -> None:
        """
        Sets the fontColor property value. Color of the font to use for the header.
        Args:
            value: Value to set for the fontColor property.
        """
        self._font_color = value
    
    @property
    def font_name(self,) -> Optional[str]:
        """
        Gets the fontName property value. Name of the font to use for the header.
        Returns: Optional[str]
        """
        return self._font_name
    
    @font_name.setter
    def font_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fontName property value. Name of the font to use for the header.
        Args:
            value: Value to set for the fontName property.
        """
        self._font_name = value
    
    @property
    def font_size(self,) -> Optional[int]:
        """
        Gets the fontSize property value. Font size to use for the header.
        Returns: Optional[int]
        """
        return self._font_size
    
    @font_size.setter
    def font_size(self,value: Optional[int] = None) -> None:
        """
        Sets the fontSize property value. Font size to use for the header.
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
            "alignment": lambda n : setattr(self, 'alignment', n.get_enum_value(content_alignment.ContentAlignment)),
            "font_color": lambda n : setattr(self, 'font_color', n.get_str_value()),
            "font_name": lambda n : setattr(self, 'font_name', n.get_str_value()),
            "font_size": lambda n : setattr(self, 'font_size', n.get_int_value()),
            "margin": lambda n : setattr(self, 'margin', n.get_int_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "ui_element_name": lambda n : setattr(self, 'ui_element_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def margin(self,) -> Optional[int]:
        """
        Gets the margin property value. The margin of the header from the top of the document.
        Returns: Optional[int]
        """
        return self._margin
    
    @margin.setter
    def margin(self,value: Optional[int] = None) -> None:
        """
        Sets the margin property value. The margin of the header from the top of the document.
        Args:
            value: Value to set for the margin property.
        """
        self._margin = value
    
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
    
    @property
    def text(self,) -> Optional[str]:
        """
        Gets the text property value. The contents of the header itself.
        Returns: Optional[str]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[str] = None) -> None:
        """
        Sets the text property value. The contents of the header itself.
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    
    @property
    def ui_element_name(self,) -> Optional[str]:
        """
        Gets the uiElementName property value. The name of the UI element where the header should be placed.
        Returns: Optional[str]
        """
        return self._ui_element_name
    
    @ui_element_name.setter
    def ui_element_name(self,value: Optional[str] = None) -> None:
        """
        Sets the uiElementName property value. The name of the UI element where the header should be placed.
        Args:
            value: Value to set for the uiElementName property.
        """
        self._ui_element_name = value
    

