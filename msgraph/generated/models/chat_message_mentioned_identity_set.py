from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_set, teamwork_conversation_identity, teamwork_tag_identity

from . import identity_set

@dataclass
class ChatMessageMentionedIdentitySet(identity_set.IdentitySet):
    odata_type = "#microsoft.graph.chatMessageMentionedIdentitySet"
    # If present, represents a conversation (for example, team or channel) @mentioned in a message.
    conversation: Optional[teamwork_conversation_identity.TeamworkConversationIdentity] = None
    # If present, represents a tag @mentioned in a team message.
    tag: Optional[teamwork_tag_identity.TeamworkTagIdentity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatMessageMentionedIdentitySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessageMentionedIdentitySet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChatMessageMentionedIdentitySet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_set, teamwork_conversation_identity, teamwork_tag_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "conversation": lambda n : setattr(self, 'conversation', n.get_object_value(teamwork_conversation_identity.TeamworkConversationIdentity)),
            "tag": lambda n : setattr(self, 'tag', n.get_object_value(teamwork_tag_identity.TeamworkTagIdentity)),
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
        writer.write_object_value("conversation", self.conversation)
        writer.write_object_value("tag", self.tag)
    

