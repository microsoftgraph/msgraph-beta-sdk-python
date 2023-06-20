from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import event_message_detail, identity_set, teamwork_user_identity

from . import event_message_detail

@dataclass
class MembersJoinedEventMessageDetail(event_message_detail.EventMessageDetail):
    odata_type = "#microsoft.graph.membersJoinedEventMessageDetail"
    # Initiator of the event.
    initiator: Optional[identity_set.IdentitySet] = None
    # List of members who joined the chat.
    members: Optional[List[teamwork_user_identity.TeamworkUserIdentity]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MembersJoinedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MembersJoinedEventMessageDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MembersJoinedEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import event_message_detail, identity_set, teamwork_user_identity

        from . import event_message_detail, identity_set, teamwork_user_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(teamwork_user_identity.TeamworkUserIdentity)),
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
        writer.write_object_value("initiator", self.initiator)
        writer.write_collection_of_object_values("members", self.members)
    

