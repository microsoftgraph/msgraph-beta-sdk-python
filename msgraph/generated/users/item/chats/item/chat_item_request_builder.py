from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import chat
    from .....models.o_data_errors import o_data_error
    from .hide_for_user import hide_for_user_request_builder
    from .installed_apps import installed_apps_request_builder
    from .installed_apps.item import teams_app_installation_item_request_builder
    from .last_message_preview import last_message_preview_request_builder
    from .mark_chat_read_for_user import mark_chat_read_for_user_request_builder
    from .mark_chat_unread_for_user import mark_chat_unread_for_user_request_builder
    from .members import members_request_builder
    from .members.item import conversation_member_item_request_builder
    from .messages import messages_request_builder
    from .messages.item import chat_message_item_request_builder
    from .operations import operations_request_builder
    from .operations.item import teams_async_operation_item_request_builder
    from .permission_grants import permission_grants_request_builder
    from .permission_grants.item import resource_specific_permission_grant_item_request_builder
    from .pinned_messages import pinned_messages_request_builder
    from .pinned_messages.item import pinned_chat_message_info_item_request_builder
    from .send_activity_notification import send_activity_notification_request_builder
    from .tabs import tabs_request_builder
    from .tabs.item import teams_tab_item_request_builder
    from .unhide_for_user import unhide_for_user_request_builder

class ChatItemRequestBuilder():
    """
    Provides operations to manage the chats property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ChatItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/chats/{chat%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ChatItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property chats for users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ChatItemRequestBuilderGetRequestConfiguration] = None) -> Optional[chat.Chat]:
        """
        Get chats from users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[chat.Chat]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import chat

        return await self.request_adapter.send_async(request_info, chat.Chat, error_mapping)
    
    def installed_apps_by_id(self,id: str) -> teams_app_installation_item_request_builder.TeamsAppInstallationItemRequestBuilder:
        """
        Provides operations to manage the installedApps property of the microsoft.graph.chat entity.
        Args:
            id: Unique identifier of the item
        Returns: teams_app_installation_item_request_builder.TeamsAppInstallationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .installed_apps.item import teams_app_installation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["teamsAppInstallation%2Did"] = id
        return teams_app_installation_item_request_builder.TeamsAppInstallationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def members_by_id(self,id: str) -> conversation_member_item_request_builder.ConversationMemberItemRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.chat entity.
        Args:
            id: Unique identifier of the item
        Returns: conversation_member_item_request_builder.ConversationMemberItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .members.item import conversation_member_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["conversationMember%2Did"] = id
        return conversation_member_item_request_builder.ConversationMemberItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def messages_by_id(self,id: str) -> chat_message_item_request_builder.ChatMessageItemRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.chat entity.
        Args:
            id: Unique identifier of the item
        Returns: chat_message_item_request_builder.ChatMessageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .messages.item import chat_message_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["chatMessage%2Did"] = id
        return chat_message_item_request_builder.ChatMessageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def operations_by_id(self,id: str) -> teams_async_operation_item_request_builder.TeamsAsyncOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.chat entity.
        Args:
            id: Unique identifier of the item
        Returns: teams_async_operation_item_request_builder.TeamsAsyncOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .operations.item import teams_async_operation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["teamsAsyncOperation%2Did"] = id
        return teams_async_operation_item_request_builder.TeamsAsyncOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[chat.Chat] = None, request_configuration: Optional[ChatItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[chat.Chat]:
        """
        Update the navigation property chats in users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[chat.Chat]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import chat

        return await self.request_adapter.send_async(request_info, chat.Chat, error_mapping)
    
    def permission_grants_by_id(self,id: str) -> resource_specific_permission_grant_item_request_builder.ResourceSpecificPermissionGrantItemRequestBuilder:
        """
        Provides operations to manage the permissionGrants property of the microsoft.graph.chat entity.
        Args:
            id: Unique identifier of the item
        Returns: resource_specific_permission_grant_item_request_builder.ResourceSpecificPermissionGrantItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .permission_grants.item import resource_specific_permission_grant_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["resourceSpecificPermissionGrant%2Did"] = id
        return resource_specific_permission_grant_item_request_builder.ResourceSpecificPermissionGrantItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def pinned_messages_by_id(self,id: str) -> pinned_chat_message_info_item_request_builder.PinnedChatMessageInfoItemRequestBuilder:
        """
        Provides operations to manage the pinnedMessages property of the microsoft.graph.chat entity.
        Args:
            id: Unique identifier of the item
        Returns: pinned_chat_message_info_item_request_builder.PinnedChatMessageInfoItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .pinned_messages.item import pinned_chat_message_info_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["pinnedChatMessageInfo%2Did"] = id
        return pinned_chat_message_info_item_request_builder.PinnedChatMessageInfoItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def tabs_by_id(self,id: str) -> teams_tab_item_request_builder.TeamsTabItemRequestBuilder:
        """
        Provides operations to manage the tabs property of the microsoft.graph.chat entity.
        Args:
            id: Unique identifier of the item
        Returns: teams_tab_item_request_builder.TeamsTabItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .tabs.item import teams_tab_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["teamsTab%2Did"] = id
        return teams_tab_item_request_builder.TeamsTabItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[ChatItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property chats for users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[ChatItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get chats from users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[chat.Chat] = None, request_configuration: Optional[ChatItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property chats in users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def hide_for_user(self) -> hide_for_user_request_builder.HideForUserRequestBuilder:
        """
        Provides operations to call the hideForUser method.
        """
        from .hide_for_user import hide_for_user_request_builder

        return hide_for_user_request_builder.HideForUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def installed_apps(self) -> installed_apps_request_builder.InstalledAppsRequestBuilder:
        """
        Provides operations to manage the installedApps property of the microsoft.graph.chat entity.
        """
        from .installed_apps import installed_apps_request_builder

        return installed_apps_request_builder.InstalledAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_message_preview(self) -> last_message_preview_request_builder.LastMessagePreviewRequestBuilder:
        """
        Provides operations to manage the lastMessagePreview property of the microsoft.graph.chat entity.
        """
        from .last_message_preview import last_message_preview_request_builder

        return last_message_preview_request_builder.LastMessagePreviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mark_chat_read_for_user(self) -> mark_chat_read_for_user_request_builder.MarkChatReadForUserRequestBuilder:
        """
        Provides operations to call the markChatReadForUser method.
        """
        from .mark_chat_read_for_user import mark_chat_read_for_user_request_builder

        return mark_chat_read_for_user_request_builder.MarkChatReadForUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mark_chat_unread_for_user(self) -> mark_chat_unread_for_user_request_builder.MarkChatUnreadForUserRequestBuilder:
        """
        Provides operations to call the markChatUnreadForUser method.
        """
        from .mark_chat_unread_for_user import mark_chat_unread_for_user_request_builder

        return mark_chat_unread_for_user_request_builder.MarkChatUnreadForUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> members_request_builder.MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.chat entity.
        """
        from .members import members_request_builder

        return members_request_builder.MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def messages(self) -> messages_request_builder.MessagesRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.chat entity.
        """
        from .messages import messages_request_builder

        return messages_request_builder.MessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.chat entity.
        """
        from .operations import operations_request_builder

        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission_grants(self) -> permission_grants_request_builder.PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the permissionGrants property of the microsoft.graph.chat entity.
        """
        from .permission_grants import permission_grants_request_builder

        return permission_grants_request_builder.PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pinned_messages(self) -> pinned_messages_request_builder.PinnedMessagesRequestBuilder:
        """
        Provides operations to manage the pinnedMessages property of the microsoft.graph.chat entity.
        """
        from .pinned_messages import pinned_messages_request_builder

        return pinned_messages_request_builder.PinnedMessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_activity_notification(self) -> send_activity_notification_request_builder.SendActivityNotificationRequestBuilder:
        """
        Provides operations to call the sendActivityNotification method.
        """
        from .send_activity_notification import send_activity_notification_request_builder

        return send_activity_notification_request_builder.SendActivityNotificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tabs(self) -> tabs_request_builder.TabsRequestBuilder:
        """
        Provides operations to manage the tabs property of the microsoft.graph.chat entity.
        """
        from .tabs import tabs_request_builder

        return tabs_request_builder.TabsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unhide_for_user(self) -> unhide_for_user_request_builder.UnhideForUserRequestBuilder:
        """
        Provides operations to call the unhideForUser method.
        """
        from .unhide_for_user import unhide_for_user_request_builder

        return unhide_for_user_request_builder.UnhideForUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ChatItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ChatItemRequestBuilderGetQueryParameters():
        """
        Get chats from users
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class ChatItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ChatItemRequestBuilder.ChatItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ChatItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

