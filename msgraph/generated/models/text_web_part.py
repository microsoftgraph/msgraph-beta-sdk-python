from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

web_part = lazy_import('msgraph.generated.models.web_part')

class TextWebPart(web_part.WebPart):
    def __init__(self,) -> None:
        """
        Instantiates a new TextWebPart and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.textWebPart"
        # The HTML string in text web part.
        self._inner_html: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TextWebPart:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TextWebPart
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TextWebPart()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "inner_html": lambda n : setattr(self, 'inner_html', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def inner_html(self,) -> Optional[str]:
        """
        Gets the innerHtml property value. The HTML string in text web part.
        Returns: Optional[str]
        """
        return self._inner_html
    
    @inner_html.setter
    def inner_html(self,value: Optional[str] = None) -> None:
        """
        Sets the innerHtml property value. The HTML string in text web part.
        Args:
            value: Value to set for the innerHtml property.
        """
        self._inner_html = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("innerHtml", self.inner_html)
    

