from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import chat_message, chat_message_info, chat_type, chat_viewpoint, conversation_member, entity, pinned_chat_message_info, resource_specific_permission_grant, teams_app_installation, teams_async_operation, teams_tab, teamwork_online_meeting_info

from . import entity

class Chat(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new chat and sets the default values.
        """
        super().__init__()
        # The chatType property
        self._chat_type: Optional[chat_type.ChatType] = None
        # Date and time at which the chat was created. Read-only.
        self._created_date_time: Optional[datetime] = None
        # A collection of all the apps in the chat. Nullable.
        self._installed_apps: Optional[List[teams_app_installation.TeamsAppInstallation]] = None
        # Preview of the last message sent in the chat. Null if no messages have been sent in the chat. Currently, only the list chats operation supports this property.
        self._last_message_preview: Optional[chat_message_info.ChatMessageInfo] = None
        # Date and time at which the chat was renamed or list of members were last changed. Read-only.
        self._last_updated_date_time: Optional[datetime] = None
        # A collection of all the members in the chat. Nullable.
        self._members: Optional[List[conversation_member.ConversationMember]] = None
        # A collection of all the messages in the chat. Nullable.
        self._messages: Optional[List[chat_message.ChatMessage]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents details about an online meeting. If the chat isn't associated with an online meeting, the property is empty. Read-only.
        self._online_meeting_info: Optional[teamwork_online_meeting_info.TeamworkOnlineMeetingInfo] = None
        # A collection of all the Teams async operations that ran or are running on the chat. Nullable.
        self._operations: Optional[List[teams_async_operation.TeamsAsyncOperation]] = None
        # A collection of permissions granted to apps for the chat.
        self._permission_grants: Optional[List[resource_specific_permission_grant.ResourceSpecificPermissionGrant]] = None
        # A collection of all the pinned messages in the chat. Nullable.
        self._pinned_messages: Optional[List[pinned_chat_message_info.PinnedChatMessageInfo]] = None
        # A collection of all the tabs in the chat. Nullable.
        self._tabs: Optional[List[teams_tab.TeamsTab]] = None
        # The identifier of the tenant in which the chat was created. Read-only.
        self._tenant_id: Optional[str] = None
        # (Optional) Subject or topic for the chat. Only available for group chats.
        self._topic: Optional[str] = None
        # Represents caller-specific information about the chat, such as last message read date and time. This property is populated only when the request is made in a delegated context.
        self._viewpoint: Optional[chat_viewpoint.ChatViewpoint] = None
        # The URL for the chat in Microsoft Teams. The URL should be treated as an opaque blob, and not parsed. Read-only.
        self._web_url: Optional[str] = None
    
    @property
    def chat_type(self,) -> Optional[chat_type.ChatType]:
        """
        Gets the chatType property value. The chatType property
        Returns: Optional[chat_type.ChatType]
        """
        return self._chat_type
    
    @chat_type.setter
    def chat_type(self,value: Optional[chat_type.ChatType] = None) -> None:
        """
        Sets the chatType property value. The chatType property
        Args:
            value: Value to set for the chat_type property.
        """
        self._chat_type = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date and time at which the chat was created. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date and time at which the chat was created. Read-only.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Chat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Chat
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Chat()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import chat_message, chat_message_info, chat_type, chat_viewpoint, conversation_member, entity, pinned_chat_message_info, resource_specific_permission_grant, teams_app_installation, teams_async_operation, teams_tab, teamwork_online_meeting_info

        fields: Dict[str, Callable[[Any], None]] = {
            "chatType": lambda n : setattr(self, 'chat_type', n.get_enum_value(chat_type.ChatType)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "installedApps": lambda n : setattr(self, 'installed_apps', n.get_collection_of_object_values(teams_app_installation.TeamsAppInstallation)),
            "lastMessagePreview": lambda n : setattr(self, 'last_message_preview', n.get_object_value(chat_message_info.ChatMessageInfo)),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(conversation_member.ConversationMember)),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(chat_message.ChatMessage)),
            "onlineMeetingInfo": lambda n : setattr(self, 'online_meeting_info', n.get_object_value(teamwork_online_meeting_info.TeamworkOnlineMeetingInfo)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(teams_async_operation.TeamsAsyncOperation)),
            "permissionGrants": lambda n : setattr(self, 'permission_grants', n.get_collection_of_object_values(resource_specific_permission_grant.ResourceSpecificPermissionGrant)),
            "pinnedMessages": lambda n : setattr(self, 'pinned_messages', n.get_collection_of_object_values(pinned_chat_message_info.PinnedChatMessageInfo)),
            "tabs": lambda n : setattr(self, 'tabs', n.get_collection_of_object_values(teams_tab.TeamsTab)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "topic": lambda n : setattr(self, 'topic', n.get_str_value()),
            "viewpoint": lambda n : setattr(self, 'viewpoint', n.get_object_value(chat_viewpoint.ChatViewpoint)),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def installed_apps(self,) -> Optional[List[teams_app_installation.TeamsAppInstallation]]:
        """
        Gets the installedApps property value. A collection of all the apps in the chat. Nullable.
        Returns: Optional[List[teams_app_installation.TeamsAppInstallation]]
        """
        return self._installed_apps
    
    @installed_apps.setter
    def installed_apps(self,value: Optional[List[teams_app_installation.TeamsAppInstallation]] = None) -> None:
        """
        Sets the installedApps property value. A collection of all the apps in the chat. Nullable.
        Args:
            value: Value to set for the installed_apps property.
        """
        self._installed_apps = value
    
    @property
    def last_message_preview(self,) -> Optional[chat_message_info.ChatMessageInfo]:
        """
        Gets the lastMessagePreview property value. Preview of the last message sent in the chat. Null if no messages have been sent in the chat. Currently, only the list chats operation supports this property.
        Returns: Optional[chat_message_info.ChatMessageInfo]
        """
        return self._last_message_preview
    
    @last_message_preview.setter
    def last_message_preview(self,value: Optional[chat_message_info.ChatMessageInfo] = None) -> None:
        """
        Sets the lastMessagePreview property value. Preview of the last message sent in the chat. Null if no messages have been sent in the chat. Currently, only the list chats operation supports this property.
        Args:
            value: Value to set for the last_message_preview property.
        """
        self._last_message_preview = value
    
    @property
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. Date and time at which the chat was renamed or list of members were last changed. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. Date and time at which the chat was renamed or list of members were last changed. Read-only.
        Args:
            value: Value to set for the last_updated_date_time property.
        """
        self._last_updated_date_time = value
    
    @property
    def members(self,) -> Optional[List[conversation_member.ConversationMember]]:
        """
        Gets the members property value. A collection of all the members in the chat. Nullable.
        Returns: Optional[List[conversation_member.ConversationMember]]
        """
        return self._members
    
    @members.setter
    def members(self,value: Optional[List[conversation_member.ConversationMember]] = None) -> None:
        """
        Sets the members property value. A collection of all the members in the chat. Nullable.
        Args:
            value: Value to set for the members property.
        """
        self._members = value
    
    @property
    def messages(self,) -> Optional[List[chat_message.ChatMessage]]:
        """
        Gets the messages property value. A collection of all the messages in the chat. Nullable.
        Returns: Optional[List[chat_message.ChatMessage]]
        """
        return self._messages
    
    @messages.setter
    def messages(self,value: Optional[List[chat_message.ChatMessage]] = None) -> None:
        """
        Sets the messages property value. A collection of all the messages in the chat. Nullable.
        Args:
            value: Value to set for the messages property.
        """
        self._messages = value
    
    @property
    def online_meeting_info(self,) -> Optional[teamwork_online_meeting_info.TeamworkOnlineMeetingInfo]:
        """
        Gets the onlineMeetingInfo property value. Represents details about an online meeting. If the chat isn't associated with an online meeting, the property is empty. Read-only.
        Returns: Optional[teamwork_online_meeting_info.TeamworkOnlineMeetingInfo]
        """
        return self._online_meeting_info
    
    @online_meeting_info.setter
    def online_meeting_info(self,value: Optional[teamwork_online_meeting_info.TeamworkOnlineMeetingInfo] = None) -> None:
        """
        Sets the onlineMeetingInfo property value. Represents details about an online meeting. If the chat isn't associated with an online meeting, the property is empty. Read-only.
        Args:
            value: Value to set for the online_meeting_info property.
        """
        self._online_meeting_info = value
    
    @property
    def operations(self,) -> Optional[List[teams_async_operation.TeamsAsyncOperation]]:
        """
        Gets the operations property value. A collection of all the Teams async operations that ran or are running on the chat. Nullable.
        Returns: Optional[List[teams_async_operation.TeamsAsyncOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[teams_async_operation.TeamsAsyncOperation]] = None) -> None:
        """
        Sets the operations property value. A collection of all the Teams async operations that ran or are running on the chat. Nullable.
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def permission_grants(self,) -> Optional[List[resource_specific_permission_grant.ResourceSpecificPermissionGrant]]:
        """
        Gets the permissionGrants property value. A collection of permissions granted to apps for the chat.
        Returns: Optional[List[resource_specific_permission_grant.ResourceSpecificPermissionGrant]]
        """
        return self._permission_grants
    
    @permission_grants.setter
    def permission_grants(self,value: Optional[List[resource_specific_permission_grant.ResourceSpecificPermissionGrant]] = None) -> None:
        """
        Sets the permissionGrants property value. A collection of permissions granted to apps for the chat.
        Args:
            value: Value to set for the permission_grants property.
        """
        self._permission_grants = value
    
    @property
    def pinned_messages(self,) -> Optional[List[pinned_chat_message_info.PinnedChatMessageInfo]]:
        """
        Gets the pinnedMessages property value. A collection of all the pinned messages in the chat. Nullable.
        Returns: Optional[List[pinned_chat_message_info.PinnedChatMessageInfo]]
        """
        return self._pinned_messages
    
    @pinned_messages.setter
    def pinned_messages(self,value: Optional[List[pinned_chat_message_info.PinnedChatMessageInfo]] = None) -> None:
        """
        Sets the pinnedMessages property value. A collection of all the pinned messages in the chat. Nullable.
        Args:
            value: Value to set for the pinned_messages property.
        """
        self._pinned_messages = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("chatType", self.chat_type)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("installedApps", self.installed_apps)
        writer.write_object_value("lastMessagePreview", self.last_message_preview)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_object_value("onlineMeetingInfo", self.online_meeting_info)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("permissionGrants", self.permission_grants)
        writer.write_collection_of_object_values("pinnedMessages", self.pinned_messages)
        writer.write_collection_of_object_values("tabs", self.tabs)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("topic", self.topic)
        writer.write_object_value("viewpoint", self.viewpoint)
        writer.write_str_value("webUrl", self.web_url)
    
    @property
    def tabs(self,) -> Optional[List[teams_tab.TeamsTab]]:
        """
        Gets the tabs property value. A collection of all the tabs in the chat. Nullable.
        Returns: Optional[List[teams_tab.TeamsTab]]
        """
        return self._tabs
    
    @tabs.setter
    def tabs(self,value: Optional[List[teams_tab.TeamsTab]] = None) -> None:
        """
        Sets the tabs property value. A collection of all the tabs in the chat. Nullable.
        Args:
            value: Value to set for the tabs property.
        """
        self._tabs = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The identifier of the tenant in which the chat was created. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The identifier of the tenant in which the chat was created. Read-only.
        Args:
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    
    @property
    def topic(self,) -> Optional[str]:
        """
        Gets the topic property value. (Optional) Subject or topic for the chat. Only available for group chats.
        Returns: Optional[str]
        """
        return self._topic
    
    @topic.setter
    def topic(self,value: Optional[str] = None) -> None:
        """
        Sets the topic property value. (Optional) Subject or topic for the chat. Only available for group chats.
        Args:
            value: Value to set for the topic property.
        """
        self._topic = value
    
    @property
    def viewpoint(self,) -> Optional[chat_viewpoint.ChatViewpoint]:
        """
        Gets the viewpoint property value. Represents caller-specific information about the chat, such as last message read date and time. This property is populated only when the request is made in a delegated context.
        Returns: Optional[chat_viewpoint.ChatViewpoint]
        """
        return self._viewpoint
    
    @viewpoint.setter
    def viewpoint(self,value: Optional[chat_viewpoint.ChatViewpoint] = None) -> None:
        """
        Sets the viewpoint property value. Represents caller-specific information about the chat, such as last message read date and time. This property is populated only when the request is made in a delegated context.
        Args:
            value: Value to set for the viewpoint property.
        """
        self._viewpoint = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. The URL for the chat in Microsoft Teams. The URL should be treated as an opaque blob, and not parsed. Read-only.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. The URL for the chat in Microsoft Teams. The URL should be treated as an opaque blob, and not parsed. Read-only.
        Args:
            value: Value to set for the web_url property.
        """
        self._web_url = value
    

