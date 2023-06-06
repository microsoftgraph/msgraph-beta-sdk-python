from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_set

@dataclass
class CommentAction(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # If true, this activity was a reply to an existing comment thread.
    is_reply: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identity of the user who started the comment thread.
    parent_author: Optional[identity_set.IdentitySet] = None
    # The identities of the users participating in this comment thread.
    participants: Optional[List[identity_set.IdentitySet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CommentAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CommentAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CommentAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "isReply": lambda n : setattr(self, 'is_reply', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parentAuthor": lambda n : setattr(self, 'parent_author', n.get_object_value(identity_set.IdentitySet)),
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(identity_set.IdentitySet)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("isReply", self.is_reply)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("parentAuthor", self.parent_author)
        writer.write_collection_of_object_values("participants", self.participants)
        writer.write_additional_data_value(self.additional_data)
    

