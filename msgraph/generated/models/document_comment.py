from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .document_comment_reply import DocumentCommentReply
    from .entity import Entity

from .entity import Entity

@dataclass
class DocumentComment(Entity):
    # The content property
    content: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The replies property
    replies: Optional[List[DocumentCommentReply]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DocumentComment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DocumentComment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DocumentComment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .document_comment_reply import DocumentCommentReply
        from .entity import Entity

        from .document_comment_reply import DocumentCommentReply
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "replies": lambda n : setattr(self, 'replies', n.get_collection_of_object_values(DocumentCommentReply)),
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
        writer.write_str_value("content", self.content)
        writer.write_collection_of_object_values("replies", self.replies)
    

