from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import join_meeting_id_meeting_info, organizer_meeting_info, token_meeting_info

@dataclass
class MeetingInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The allowConversationWithoutHost property
    allow_conversation_without_host: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.joinMeetingIdMeetingInfo".casefold():
            from . import join_meeting_id_meeting_info

            return join_meeting_id_meeting_info.JoinMeetingIdMeetingInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organizerMeetingInfo".casefold():
            from . import organizer_meeting_info

            return organizer_meeting_info.OrganizerMeetingInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tokenMeetingInfo".casefold():
            from . import token_meeting_info

            return token_meeting_info.TokenMeetingInfo()
        return MeetingInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import join_meeting_id_meeting_info, organizer_meeting_info, token_meeting_info

        from . import join_meeting_id_meeting_info, organizer_meeting_info, token_meeting_info

        fields: Dict[str, Callable[[Any], None]] = {
            "allowConversationWithoutHost": lambda n : setattr(self, 'allow_conversation_without_host', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("allowConversationWithoutHost", self.allow_conversation_without_host)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

