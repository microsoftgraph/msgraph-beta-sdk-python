from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

document_comment_reply = lazy_import('msgraph.generated.models.document_comment_reply')
entity = lazy_import('msgraph.generated.models.entity')

class DocumentComment(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new DocumentComment and sets the default values.
        """
        super().__init__()
        # The content property
        self._content: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The replies property
        self._replies: Optional[List[document_comment_reply.DocumentCommentReply]] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DocumentComment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DocumentComment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DocumentComment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "replies": lambda n : setattr(self, 'replies', n.get_collection_of_object_values(document_comment_reply.DocumentCommentReply)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def replies(self,) -> Optional[List[document_comment_reply.DocumentCommentReply]]:
        """
        Gets the replies property value. The replies property
        Returns: Optional[List[document_comment_reply.DocumentCommentReply]]
        """
        return self._replies
    
    @replies.setter
    def replies(self,value: Optional[List[document_comment_reply.DocumentCommentReply]] = None) -> None:
        """
        Sets the replies property value. The replies property
        Args:
            value: Value to set for the replies property.
        """
        self._replies = value
    
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
        writer.write_collection_of_object_values("replies", self.replies)
    

