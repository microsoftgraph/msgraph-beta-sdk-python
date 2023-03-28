from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity, teamwork_conversation_identity_type

from . import identity

class TeamworkConversationIdentity(identity.Identity):
    def __init__(self,) -> None:
        """
        Instantiates a new TeamworkConversationIdentity and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.teamworkConversationIdentity"
        # Type of conversation. Possible values are: team, channel, and chat.
        self._conversation_identity_type: Optional[teamwork_conversation_identity_type.TeamworkConversationIdentityType] = None
    
    @property
    def conversation_identity_type(self,) -> Optional[teamwork_conversation_identity_type.TeamworkConversationIdentityType]:
        """
        Gets the conversationIdentityType property value. Type of conversation. Possible values are: team, channel, and chat.
        Returns: Optional[teamwork_conversation_identity_type.TeamworkConversationIdentityType]
        """
        return self._conversation_identity_type
    
    @conversation_identity_type.setter
    def conversation_identity_type(self,value: Optional[teamwork_conversation_identity_type.TeamworkConversationIdentityType] = None) -> None:
        """
        Sets the conversationIdentityType property value. Type of conversation. Possible values are: team, channel, and chat.
        Args:
            value: Value to set for the conversation_identity_type property.
        """
        self._conversation_identity_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkConversationIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkConversationIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkConversationIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity, teamwork_conversation_identity_type

        fields: Dict[str, Callable[[Any], None]] = {
            "conversationIdentityType": lambda n : setattr(self, 'conversation_identity_type', n.get_enum_value(teamwork_conversation_identity_type.TeamworkConversationIdentityType)),
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
        writer.write_enum_value("conversationIdentityType", self.conversation_identity_type)
    

