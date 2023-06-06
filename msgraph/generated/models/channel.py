from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import channel_membership_type, channel_moderation_settings, channel_summary, chat_message, conversation_member, drive_item, entity, shared_with_channel_team_info, teams_tab

from . import entity

@dataclass
class Channel(entity.Entity):
    # Read only. Timestamp at which the channel was created.
    created_date_time: Optional[datetime] = None
    # Optional textual description for the channel.
    description: Optional[str] = None
    # Channel name as it will appear to the user in Microsoft Teams. The maximum length is 50 characters.
    display_name: Optional[str] = None
    # The email address for sending messages to the channel. Read-only.
    email: Optional[str] = None
    # Metadata for the location where the channel's files are stored.
    files_folder: Optional[drive_item.DriveItem] = None
    # Indicates whether the channel should automatically be marked 'favorite' for all members of the team. Can only be set programmatically with Create team. Default: false.
    is_favorite_by_default: Optional[bool] = None
    # A collection of membership records associated with the channel.
    members: Optional[List[conversation_member.ConversationMember]] = None
    # The type of the channel. Can be set during creation and can't be changed. The possible values are: standard, private, unknownFutureValue, shared. The default value is standard. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value in this evolvable enum: shared.
    membership_type: Optional[channel_membership_type.ChannelMembershipType] = None
    # A collection of all the messages in the channel. A navigation property. Nullable.
    messages: Optional[List[chat_message.ChatMessage]] = None
    # Settings to configure channel moderation to control who can start new posts and reply to posts in that channel.
    moderation_settings: Optional[channel_moderation_settings.ChannelModerationSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of teams with which a channel is shared.
    shared_with_teams: Optional[List[shared_with_channel_team_info.SharedWithChannelTeamInfo]] = None
    # The summary property
    summary: Optional[channel_summary.ChannelSummary] = None
    # A collection of all the tabs in the channel. A navigation property.
    tabs: Optional[List[teams_tab.TeamsTab]] = None
    # The ID of the Azure Active Directory tenant.
    tenant_id: Optional[str] = None
    # A hyperlink that will go to the channel in Microsoft Teams. This is the URL that you get when you right-click a channel in Microsoft Teams and select Get link to channel. This URL should be treated as an opaque blob, and not parsed. Read-only.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Channel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Channel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Channel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import channel_membership_type, channel_moderation_settings, channel_summary, chat_message, conversation_member, drive_item, entity, shared_with_channel_team_info, teams_tab

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "filesFolder": lambda n : setattr(self, 'files_folder', n.get_object_value(drive_item.DriveItem)),
            "isFavoriteByDefault": lambda n : setattr(self, 'is_favorite_by_default', n.get_bool_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(conversation_member.ConversationMember)),
            "membershipType": lambda n : setattr(self, 'membership_type', n.get_enum_value(channel_membership_type.ChannelMembershipType)),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(chat_message.ChatMessage)),
            "moderationSettings": lambda n : setattr(self, 'moderation_settings', n.get_object_value(channel_moderation_settings.ChannelModerationSettings)),
            "sharedWithTeams": lambda n : setattr(self, 'shared_with_teams', n.get_collection_of_object_values(shared_with_channel_team_info.SharedWithChannelTeamInfo)),
            "summary": lambda n : setattr(self, 'summary', n.get_object_value(channel_summary.ChannelSummary)),
            "tabs": lambda n : setattr(self, 'tabs', n.get_collection_of_object_values(teams_tab.TeamsTab)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_object_value("filesFolder", self.files_folder)
        writer.write_bool_value("isFavoriteByDefault", self.is_favorite_by_default)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_enum_value("membershipType", self.membership_type)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_object_value("moderationSettings", self.moderation_settings)
        writer.write_collection_of_object_values("sharedWithTeams", self.shared_with_teams)
        writer.write_object_value("summary", self.summary)
        writer.write_collection_of_object_values("tabs", self.tabs)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("webUrl", self.web_url)
    

