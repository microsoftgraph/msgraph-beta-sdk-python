from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

team = lazy_import('msgraph.generated.models.team')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
all_channels_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.all_channels.all_channels_request_builder')
channel_item_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.all_channels.item.channel_item_request_builder')
archive_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.archive.archive_request_builder')
channels_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.channels.channels_request_builder')
channel_item_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.channels.item.channel_item_request_builder')
clone_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.clone.clone_request_builder')
complete_migration_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.complete_migration.complete_migration_request_builder')
group_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.group.group_request_builder')
incoming_channels_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.incoming_channels.incoming_channels_request_builder')
channel_item_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.incoming_channels.item.channel_item_request_builder')
installed_apps_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.installed_apps.installed_apps_request_builder')
teams_app_installation_item_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.installed_apps.item.teams_app_installation_item_request_builder')
members_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.members.members_request_builder')
conversation_member_item_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.members.item.conversation_member_item_request_builder')
operations_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.operations.operations_request_builder')
teams_async_operation_item_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.operations.item.teams_async_operation_item_request_builder')
owners_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.owners.owners_request_builder')
user_item_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.owners.item.user_item_request_builder')
permission_grants_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.permission_grants.permission_grants_request_builder')
resource_specific_permission_grant_item_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.permission_grants.item.resource_specific_permission_grant_item_request_builder')
photo_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.photo.photo_request_builder')
primary_channel_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.primary_channel.primary_channel_request_builder')
schedule_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.schedule.schedule_request_builder')
send_activity_notification_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.send_activity_notification.send_activity_notification_request_builder')
tags_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.tags.tags_request_builder')
teamwork_tag_item_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.tags.item.teamwork_tag_item_request_builder')
template_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.template.template_request_builder')
template_definition_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.template_definition.template_definition_request_builder')
unarchive_request_builder = lazy_import('msgraph.generated.team_template_definition.item.team_definition.unarchive.unarchive_request_builder')

class TeamDefinitionRequestBuilder():
    """
    Provides operations to manage the teamDefinition property of the microsoft.graph.teamTemplateDefinition entity.
    """
    @property
    def all_channels(self) -> all_channels_request_builder.AllChannelsRequestBuilder:
        """
        Provides operations to manage the allChannels property of the microsoft.graph.team entity.
        """
        return all_channels_request_builder.AllChannelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def archive(self) -> archive_request_builder.ArchiveRequestBuilder:
        """
        Provides operations to call the archive method.
        """
        return archive_request_builder.ArchiveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def channels(self) -> channels_request_builder.ChannelsRequestBuilder:
        """
        Provides operations to manage the channels property of the microsoft.graph.team entity.
        """
        return channels_request_builder.ChannelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clone(self) -> clone_request_builder.CloneRequestBuilder:
        """
        Provides operations to call the clone method.
        """
        return clone_request_builder.CloneRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def complete_migration(self) -> complete_migration_request_builder.CompleteMigrationRequestBuilder:
        """
        Provides operations to call the completeMigration method.
        """
        return complete_migration_request_builder.CompleteMigrationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group(self) -> group_request_builder.GroupRequestBuilder:
        """
        Provides operations to manage the group property of the microsoft.graph.team entity.
        """
        return group_request_builder.GroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def incoming_channels(self) -> incoming_channels_request_builder.IncomingChannelsRequestBuilder:
        """
        Provides operations to manage the incomingChannels property of the microsoft.graph.team entity.
        """
        return incoming_channels_request_builder.IncomingChannelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def installed_apps(self) -> installed_apps_request_builder.InstalledAppsRequestBuilder:
        """
        Provides operations to manage the installedApps property of the microsoft.graph.team entity.
        """
        return installed_apps_request_builder.InstalledAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> members_request_builder.MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.team entity.
        """
        return members_request_builder.MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.team entity.
        """
        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def owners(self) -> owners_request_builder.OwnersRequestBuilder:
        """
        Provides operations to manage the owners property of the microsoft.graph.team entity.
        """
        return owners_request_builder.OwnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission_grants(self) -> permission_grants_request_builder.PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the permissionGrants property of the microsoft.graph.team entity.
        """
        return permission_grants_request_builder.PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def photo(self) -> photo_request_builder.PhotoRequestBuilder:
        """
        Provides operations to manage the photo property of the microsoft.graph.team entity.
        """
        return photo_request_builder.PhotoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def primary_channel(self) -> primary_channel_request_builder.PrimaryChannelRequestBuilder:
        """
        Provides operations to manage the primaryChannel property of the microsoft.graph.team entity.
        """
        return primary_channel_request_builder.PrimaryChannelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schedule(self) -> schedule_request_builder.ScheduleRequestBuilder:
        """
        Provides operations to manage the schedule property of the microsoft.graph.team entity.
        """
        return schedule_request_builder.ScheduleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_activity_notification(self) -> send_activity_notification_request_builder.SendActivityNotificationRequestBuilder:
        """
        Provides operations to call the sendActivityNotification method.
        """
        return send_activity_notification_request_builder.SendActivityNotificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tags(self) -> tags_request_builder.TagsRequestBuilder:
        """
        Provides operations to manage the tags property of the microsoft.graph.team entity.
        """
        return tags_request_builder.TagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def template(self) -> template_request_builder.TemplateRequestBuilder:
        """
        Provides operations to manage the template property of the microsoft.graph.team entity.
        """
        return template_request_builder.TemplateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def template_definition(self) -> template_definition_request_builder.TemplateDefinitionRequestBuilder:
        """
        Provides operations to manage the templateDefinition property of the microsoft.graph.team entity.
        """
        return template_definition_request_builder.TemplateDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unarchive(self) -> unarchive_request_builder.UnarchiveRequestBuilder:
        """
        Provides operations to call the unarchive method.
        """
        return unarchive_request_builder.UnarchiveRequestBuilder(self.request_adapter, self.path_parameters)
    
    def all_channels_by_id(self,id: str) -> channel_item_request_builder.ChannelItemRequestBuilder:
        """
        Provides operations to manage the allChannels property of the microsoft.graph.team entity.
        Args:
            id: Unique identifier of the item
        Returns: channel_item_request_builder.ChannelItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["channel%2Did"] = id
        return channel_item_request_builder.ChannelItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def channels_by_id(self,id: str) -> channel_item_request_builder.ChannelItemRequestBuilder:
        """
        Provides operations to manage the channels property of the microsoft.graph.team entity.
        Args:
            id: Unique identifier of the item
        Returns: channel_item_request_builder.ChannelItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["channel%2Did"] = id
        return channel_item_request_builder.ChannelItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TeamDefinitionRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/teamTemplateDefinition/{teamTemplateDefinition%2Did}/teamDefinition{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[TeamDefinitionRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property teamDefinition for teamTemplateDefinition
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[TeamDefinitionRequestBuilderGetRequestConfiguration] = None) -> Optional[team.Team]:
        """
        Get the properties of the team associated with a teamTemplateDefinition object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[team.Team]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, team.Team, error_mapping)
    
    def incoming_channels_by_id(self,id: str) -> channel_item_request_builder.ChannelItemRequestBuilder:
        """
        Provides operations to manage the incomingChannels property of the microsoft.graph.team entity.
        Args:
            id: Unique identifier of the item
        Returns: channel_item_request_builder.ChannelItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["channel%2Did"] = id
        return channel_item_request_builder.ChannelItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def installed_apps_by_id(self,id: str) -> teams_app_installation_item_request_builder.TeamsAppInstallationItemRequestBuilder:
        """
        Provides operations to manage the installedApps property of the microsoft.graph.team entity.
        Args:
            id: Unique identifier of the item
        Returns: teams_app_installation_item_request_builder.TeamsAppInstallationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["teamsAppInstallation%2Did"] = id
        return teams_app_installation_item_request_builder.TeamsAppInstallationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def members_by_id(self,id: str) -> conversation_member_item_request_builder.ConversationMemberItemRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.team entity.
        Args:
            id: Unique identifier of the item
        Returns: conversation_member_item_request_builder.ConversationMemberItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["conversationMember%2Did"] = id
        return conversation_member_item_request_builder.ConversationMemberItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def operations_by_id(self,id: str) -> teams_async_operation_item_request_builder.TeamsAsyncOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.team entity.
        Args:
            id: Unique identifier of the item
        Returns: teams_async_operation_item_request_builder.TeamsAsyncOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["teamsAsyncOperation%2Did"] = id
        return teams_async_operation_item_request_builder.TeamsAsyncOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def owners_by_id(self,id: str) -> user_item_request_builder.UserItemRequestBuilder:
        """
        Provides operations to manage the owners property of the microsoft.graph.team entity.
        Args:
            id: Unique identifier of the item
        Returns: user_item_request_builder.UserItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["user%2Did"] = id
        return user_item_request_builder.UserItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[team.Team] = None, request_configuration: Optional[TeamDefinitionRequestBuilderPatchRequestConfiguration] = None) -> Optional[team.Team]:
        """
        Update the navigation property teamDefinition in teamTemplateDefinition
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[team.Team]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, team.Team, error_mapping)
    
    def permission_grants_by_id(self,id: str) -> resource_specific_permission_grant_item_request_builder.ResourceSpecificPermissionGrantItemRequestBuilder:
        """
        Provides operations to manage the permissionGrants property of the microsoft.graph.team entity.
        Args:
            id: Unique identifier of the item
        Returns: resource_specific_permission_grant_item_request_builder.ResourceSpecificPermissionGrantItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["resourceSpecificPermissionGrant%2Did"] = id
        return resource_specific_permission_grant_item_request_builder.ResourceSpecificPermissionGrantItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def tags_by_id(self,id: str) -> teamwork_tag_item_request_builder.TeamworkTagItemRequestBuilder:
        """
        Provides operations to manage the tags property of the microsoft.graph.team entity.
        Args:
            id: Unique identifier of the item
        Returns: teamwork_tag_item_request_builder.TeamworkTagItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["teamworkTag%2Did"] = id
        return teamwork_tag_item_request_builder.TeamworkTagItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[TeamDefinitionRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property teamDefinition for teamTemplateDefinition
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
    
    def to_get_request_information(self,request_configuration: Optional[TeamDefinitionRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the properties of the team associated with a teamTemplateDefinition object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[team.Team] = None, request_configuration: Optional[TeamDefinitionRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property teamDefinition in teamTemplateDefinition
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class TeamDefinitionRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class TeamDefinitionRequestBuilderGetQueryParameters():
        """
        Get the properties of the team associated with a teamTemplateDefinition object.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

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
        
    
    @dataclass
    class TeamDefinitionRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TeamDefinitionRequestBuilder.TeamDefinitionRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class TeamDefinitionRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

