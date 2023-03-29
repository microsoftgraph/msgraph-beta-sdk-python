from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import document_comment, entity

from . import entity

class Presentation(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Presentation and sets the default values.
        """
        super().__init__()
        # The comments property
        self._comments: Optional[List[document_comment.DocumentComment]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def comments(self,) -> Optional[List[document_comment.DocumentComment]]:
        """
        Gets the comments property value. The comments property
        Returns: Optional[List[document_comment.DocumentComment]]
        """
        return self._comments
    
    @comments.setter
    def comments(self,value: Optional[List[document_comment.DocumentComment]] = None) -> None:
        """
        Sets the comments property value. The comments property
        Args:
            value: Value to set for the comments property.
        """
        self._comments = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Presentation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Presentation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Presentation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import document_comment, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "comments": lambda n : setattr(self, 'comments', n.get_collection_of_object_values(document_comment.DocumentComment)),
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
        writer.write_collection_of_object_values("comments", self.comments)
    

