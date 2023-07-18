from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.invitation_participant_info import InvitationParticipantInfo

@dataclass
class InvitePostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The clientContext property
    client_context: Optional[str] = None
    # The participants property
    participants: Optional[List[InvitationParticipantInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InvitePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvitePostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InvitePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......models.invitation_participant_info import InvitationParticipantInfo

        from ......models.invitation_participant_info import InvitationParticipantInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "clientContext": lambda n : setattr(self, 'client_context', n.get_str_value()),
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(InvitationParticipantInfo)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("clientContext", self.client_context)
        writer.write_collection_of_object_values("participants", self.participants)
        writer.write_additional_data_value(self.additional_data)
    

