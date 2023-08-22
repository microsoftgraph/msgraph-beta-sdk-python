from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_set import IdentitySet
    from .teamwork_conversation_identity import TeamworkConversationIdentity
    from .teamwork_tag_identity import TeamworkTagIdentity

from .identity_set import IdentitySet

@dataclass
class ChatMessageMentionedIdentitySet(IdentitySet):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.chatMessageMentionedIdentitySet"
    # If present, represents a conversation (for example, team or channel) @mentioned in a message.
    conversation: Optional[TeamworkConversationIdentity] = None
    # If present, represents a tag @mentioned in a team message.
    tag: Optional[TeamworkTagIdentity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatMessageMentionedIdentitySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessageMentionedIdentitySet
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ChatMessageMentionedIdentitySet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .identity_set import IdentitySet
        from .teamwork_conversation_identity import TeamworkConversationIdentity
        from .teamwork_tag_identity import TeamworkTagIdentity

        from .identity_set import IdentitySet
        from .teamwork_conversation_identity import TeamworkConversationIdentity
        from .teamwork_tag_identity import TeamworkTagIdentity

        fields: Dict[str, Callable[[Any], None]] = {
            "conversation": lambda n : setattr(self, 'conversation', n.get_object_value(TeamworkConversationIdentity)),
            "tag": lambda n : setattr(self, 'tag', n.get_object_value(TeamworkTagIdentity)),
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
        writer.write_object_value("conversation", self.conversation)
        writer.write_object_value("tag", self.tag)
    

