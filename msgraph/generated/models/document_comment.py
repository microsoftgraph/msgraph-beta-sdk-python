from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import document_comment_reply, entity

from . import entity

@dataclass
class DocumentComment(entity.Entity):
    # The content property
    content: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The replies property
    replies: Optional[List[document_comment_reply.DocumentCommentReply]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DocumentComment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
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
        from . import document_comment_reply, entity

        from . import document_comment_reply, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "replies": lambda n : setattr(self, 'replies', n.get_collection_of_object_values(document_comment_reply.DocumentCommentReply)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("content", self.content)
        writer.write_collection_of_object_values("replies", self.replies)
    

