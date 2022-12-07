from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class Picture(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new picture and sets the default values.
        """
        super().__init__()
        # The content property
        self._content: Optional[bytes] = None
        # The contentType property
        self._content_type: Optional[str] = None
        # The height property
        self._height: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The width property
        self._width: Optional[int] = None
    
    @property
    def content(self,) -> Optional[bytes]:
        """
        Gets the content property value. The content property
        Returns: Optional[bytes]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the content property value. The content property
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @property
    def content_type(self,) -> Optional[str]:
        """
        Gets the contentType property value. The contentType property
        Returns: Optional[str]
        """
        return self._content_type
    
    @content_type.setter
    def content_type(self,value: Optional[str] = None) -> None:
        """
        Sets the contentType property value. The contentType property
        Args:
            value: Value to set for the contentType property.
        """
        self._content_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Picture:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Picture
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Picture()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "content_type": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def height(self,) -> Optional[int]:
        """
        Gets the height property value. The height property
        Returns: Optional[int]
        """
        return self._height
    
    @height.setter
    def height(self,value: Optional[int] = None) -> None:
        """
        Sets the height property value. The height property
        Args:
            value: Value to set for the height property.
        """
        self._height = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("content", self.content)
        writer.write_str_value("contentType", self.content_type)
        writer.write_int_value("height", self.height)
        writer.write_int_value("width", self.width)
    
    @property
    def width(self,) -> Optional[int]:
        """
        Gets the width property value. The width property
        Returns: Optional[int]
        """
        return self._width
    
    @width.setter
    def width(self,value: Optional[int] = None) -> None:
        """
        Sets the width property value. The width property
        Args:
            value: Value to set for the width property.
        """
        self._width = value
    

