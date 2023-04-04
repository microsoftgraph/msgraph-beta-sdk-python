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
    from ......models import channel
    from ......models.o_data_errors import o_data_error
    from .complete_migration import complete_migration_request_builder
    from .does_user_have_accessuser_id_user_id_tenant_id_tenant_id_user_principal_name_user_principal_name import does_user_have_accessuser_id_user_id_tenant_id_tenant_id_user_principal_name_user_principal_name_request_builder
    from .files_folder import files_folder_request_builder
    from .members import members_request_builder
    from .members.item import conversation_member_item_request_builder
    from .messages import messages_request_builder
    from .messages.item import chat_message_item_request_builder
    from .provision_email import provision_email_request_builder
    from .remove_email import remove_email_request_builder
    from .shared_with_teams import shared_with_teams_request_builder
    from .shared_with_teams.item import shared_with_channel_team_info_item_request_builder
    from .tabs import tabs_request_builder
    from .tabs.item import teams_tab_item_request_builder

class ChannelItemRequestBuilder():
    """
    Provides operations to manage the channels property of the microsoft.graph.team entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ChannelItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}/team/channels/{channel%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ChannelItemRequestBuilderDeleteRequestConfiguration] = None) -> bytes:
        """
        Delete navigation property channels for groups
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    async def get(self,request_configuration: Optional[ChannelItemRequestBuilderGetRequestConfiguration] = None) -> Optional[channel.Channel]:
        """
        The collection of channels and messages associated with the team.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[channel.Channel]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import channel

        return await self.request_adapter.send_async(request_info, channel.Channel, error_mapping)
    
    def members_by_id(self,id: str) -> conversation_member_item_request_builder.ConversationMemberItemRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.channel entity.
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
        Provides operations to manage the messages property of the microsoft.graph.channel entity.
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
    
    async def patch(self,body: Optional[channel.Channel] = None, request_configuration: Optional[ChannelItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[channel.Channel]:
        """
        Update the navigation property channels in groups
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[channel.Channel]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import channel

        return await self.request_adapter.send_async(request_info, channel.Channel, error_mapping)
    
    def shared_with_teams_by_id(self,id: str) -> shared_with_channel_team_info_item_request_builder.SharedWithChannelTeamInfoItemRequestBuilder:
        """
        Provides operations to manage the sharedWithTeams property of the microsoft.graph.channel entity.
        Args:
            id: Unique identifier of the item
        Returns: shared_with_channel_team_info_item_request_builder.SharedWithChannelTeamInfoItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .shared_with_teams.item import shared_with_channel_team_info_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["sharedWithChannelTeamInfo%2Did"] = id
        return shared_with_channel_team_info_item_request_builder.SharedWithChannelTeamInfoItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def tabs_by_id(self,id: str) -> teams_tab_item_request_builder.TeamsTabItemRequestBuilder:
        """
        Provides operations to manage the tabs property of the microsoft.graph.channel entity.
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
    
    def to_delete_request_information(self,request_configuration: Optional[ChannelItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property channels for groups
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
    
    def to_get_request_information(self,request_configuration: Optional[ChannelItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The collection of channels and messages associated with the team.
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
    
    def to_patch_request_information(self,body: Optional[channel.Channel] = None, request_configuration: Optional[ChannelItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property channels in groups
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
    def complete_migration(self) -> complete_migration_request_builder.CompleteMigrationRequestBuilder:
        """
        Provides operations to call the completeMigration method.
        """
        from .complete_migration import complete_migration_request_builder

        return complete_migration_request_builder.CompleteMigrationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def does_user_have_accessuser_id_user_id_tenant_id_tenant_id_user_principal_name_user_principal_name(self) -> does_user_have_accessuser_id_user_id_tenant_id_tenant_id_user_principal_name_user_principal_name_request_builder.DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrincipalNameUserPrincipalNameRequestBuilder:
        """
        Provides operations to call the doesUserHaveAccess method.
        """
        from .does_user_have_accessuser_id_user_id_tenant_id_tenant_id_user_principal_name_user_principal_name import does_user_have_accessuser_id_user_id_tenant_id_tenant_id_user_principal_name_user_principal_name_request_builder

        return does_user_have_accessuser_id_user_id_tenant_id_tenant_id_user_principal_name_user_principal_name_request_builder.DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrincipalNameUserPrincipalNameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def files_folder(self) -> files_folder_request_builder.FilesFolderRequestBuilder:
        """
        Provides operations to manage the filesFolder property of the microsoft.graph.channel entity.
        """
        from .files_folder import files_folder_request_builder

        return files_folder_request_builder.FilesFolderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> members_request_builder.MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.channel entity.
        """
        from .members import members_request_builder

        return members_request_builder.MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def messages(self) -> messages_request_builder.MessagesRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.channel entity.
        """
        from .messages import messages_request_builder

        return messages_request_builder.MessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def provision_email(self) -> provision_email_request_builder.ProvisionEmailRequestBuilder:
        """
        Provides operations to call the provisionEmail method.
        """
        from .provision_email import provision_email_request_builder

        return provision_email_request_builder.ProvisionEmailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_email(self) -> remove_email_request_builder.RemoveEmailRequestBuilder:
        """
        Provides operations to call the removeEmail method.
        """
        from .remove_email import remove_email_request_builder

        return remove_email_request_builder.RemoveEmailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shared_with_teams(self) -> shared_with_teams_request_builder.SharedWithTeamsRequestBuilder:
        """
        Provides operations to manage the sharedWithTeams property of the microsoft.graph.channel entity.
        """
        from .shared_with_teams import shared_with_teams_request_builder

        return shared_with_teams_request_builder.SharedWithTeamsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tabs(self) -> tabs_request_builder.TabsRequestBuilder:
        """
        Provides operations to manage the tabs property of the microsoft.graph.channel entity.
        """
        from .tabs import tabs_request_builder

        return tabs_request_builder.TabsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ChannelItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ChannelItemRequestBuilderGetQueryParameters():
        """
        The collection of channels and messages associated with the team.
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
    class ChannelItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ChannelItemRequestBuilder.ChannelItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ChannelItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

