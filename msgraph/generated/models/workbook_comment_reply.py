from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class WorkbookCommentReply(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new workbookCommentReply and sets the default values.
        """
        super().__init__()
        # The content of replied comment.
        self._content: Optional[str] = None
        # Indicates the type for the replied comment.
        self._content_type: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def content(self,) -> Optional[str]:
        """
        Gets the content property value. The content of replied comment.
        Returns: Optional[str]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[str] = None) -> None:
        """
        Sets the content property value. The content of replied comment.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @property
    def content_type(self,) -> Optional[str]:
        """
        Gets the contentType property value. Indicates the type for the replied comment.
        Returns: Optional[str]
        """
        return self._content_type
    
    @content_type.setter
    def content_type(self,value: Optional[str] = None) -> None:
        """
        Sets the contentType property value. Indicates the type for the replied comment.
        Args:
            value: Value to set for the content_type property.
        """
        self._content_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookCommentReply:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookCommentReply
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookCommentReply()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
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
        writer.write_str_value("content", self.content)
        writer.write_str_value("contentType", self.content_type)
    

