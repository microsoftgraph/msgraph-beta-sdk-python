from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class DocumentCommentReply(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new documentCommentReply and sets the default values.
        """
        super().__init__()
        # The content property
        self._content: Optional[str] = None
        # The location property
        self._location: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def content(self,) -> Optional[str]:
        """
        Gets the content property value. The content property
        Returns: Optional[str]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[str] = None) -> None:
        """
        Sets the content property value. The content property
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DocumentCommentReply:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DocumentCommentReply
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DocumentCommentReply()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def location(self,) -> Optional[str]:
        """
        Gets the location property value. The location property
        Returns: Optional[str]
        """
        return self._location
    
    @location.setter
    def location(self,value: Optional[str] = None) -> None:
        """
        Sets the location property value. The location property
        Args:
            value: Value to set for the location property.
        """
        self._location = value
    
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
        writer.write_str_value("location", self.location)
    

