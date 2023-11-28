from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.team import Team
    from .all_channels.all_channels_request_builder import AllChannelsRequestBuilder
    from .archive.archive_request_builder import ArchiveRequestBuilder
    from .channels.channels_request_builder import ChannelsRequestBuilder
    from .clone.clone_request_builder import CloneRequestBuilder
    from .complete_migration.complete_migration_request_builder import CompleteMigrationRequestBuilder
    from .group.group_request_builder import GroupRequestBuilder
    from .incoming_channels.incoming_channels_request_builder import IncomingChannelsRequestBuilder
    from .installed_apps.installed_apps_request_builder import InstalledAppsRequestBuilder
    from .members.members_request_builder import MembersRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .owners.owners_request_builder import OwnersRequestBuilder
    from .permission_grants.permission_grants_request_builder import PermissionGrantsRequestBuilder
    from .photo.photo_request_builder import PhotoRequestBuilder
    from .primary_channel.primary_channel_request_builder import PrimaryChannelRequestBuilder
    from .schedule.schedule_request_builder import ScheduleRequestBuilder
    from .send_activity_notification.send_activity_notification_request_builder import SendActivityNotificationRequestBuilder
    from .tags.tags_request_builder import TagsRequestBuilder
    from .template.template_request_builder import TemplateRequestBuilder
    from .template_definition.template_definition_request_builder import TemplateDefinitionRequestBuilder
    from .unarchive.unarchive_request_builder import UnarchiveRequestBuilder

class TeamItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of team entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TeamItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/teams/{team%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[TeamItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete entity from teams
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[TeamItemRequestBuilderGetRequestConfiguration] = None) -> Optional[Team]:
        """
        Retrieve the properties and relationships of the specified team.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Team]
        Find more info here: https://learn.microsoft.com/graph/api/team-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.team import Team

        return await self.request_adapter.send_async(request_info, Team, error_mapping)
    
    async def patch(self,body: Optional[Team] = None, request_configuration: Optional[TeamItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[Team]:
        """
        Update the properties of the specified team.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Team]
        Find more info here: https://learn.microsoft.com/graph/api/team-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.team import Team

        return await self.request_adapter.send_async(request_info, Team, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[TeamItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete entity from teams
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[TeamItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of the specified team.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[Team] = None, request_configuration: Optional[TeamItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of the specified team.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> TeamItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TeamItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return TeamItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def all_channels(self) -> AllChannelsRequestBuilder:
        """
        Provides operations to manage the allChannels property of the microsoft.graph.team entity.
        """
        from .all_channels.all_channels_request_builder import AllChannelsRequestBuilder

        return AllChannelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def archive(self) -> ArchiveRequestBuilder:
        """
        Provides operations to call the archive method.
        """
        from .archive.archive_request_builder import ArchiveRequestBuilder

        return ArchiveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def channels(self) -> ChannelsRequestBuilder:
        """
        Provides operations to manage the channels property of the microsoft.graph.team entity.
        """
        from .channels.channels_request_builder import ChannelsRequestBuilder

        return ChannelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clone(self) -> CloneRequestBuilder:
        """
        Provides operations to call the clone method.
        """
        from .clone.clone_request_builder import CloneRequestBuilder

        return CloneRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def complete_migration(self) -> CompleteMigrationRequestBuilder:
        """
        Provides operations to call the completeMigration method.
        """
        from .complete_migration.complete_migration_request_builder import CompleteMigrationRequestBuilder

        return CompleteMigrationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group(self) -> GroupRequestBuilder:
        """
        Provides operations to manage the group property of the microsoft.graph.team entity.
        """
        from .group.group_request_builder import GroupRequestBuilder

        return GroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def incoming_channels(self) -> IncomingChannelsRequestBuilder:
        """
        Provides operations to manage the incomingChannels property of the microsoft.graph.team entity.
        """
        from .incoming_channels.incoming_channels_request_builder import IncomingChannelsRequestBuilder

        return IncomingChannelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def installed_apps(self) -> InstalledAppsRequestBuilder:
        """
        Provides operations to manage the installedApps property of the microsoft.graph.team entity.
        """
        from .installed_apps.installed_apps_request_builder import InstalledAppsRequestBuilder

        return InstalledAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.team entity.
        """
        from .members.members_request_builder import MembersRequestBuilder

        return MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.team entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def owners(self) -> OwnersRequestBuilder:
        """
        Provides operations to manage the owners property of the microsoft.graph.team entity.
        """
        from .owners.owners_request_builder import OwnersRequestBuilder

        return OwnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission_grants(self) -> PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the permissionGrants property of the microsoft.graph.team entity.
        """
        from .permission_grants.permission_grants_request_builder import PermissionGrantsRequestBuilder

        return PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def photo(self) -> PhotoRequestBuilder:
        """
        Provides operations to manage the photo property of the microsoft.graph.team entity.
        """
        from .photo.photo_request_builder import PhotoRequestBuilder

        return PhotoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def primary_channel(self) -> PrimaryChannelRequestBuilder:
        """
        Provides operations to manage the primaryChannel property of the microsoft.graph.team entity.
        """
        from .primary_channel.primary_channel_request_builder import PrimaryChannelRequestBuilder

        return PrimaryChannelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schedule(self) -> ScheduleRequestBuilder:
        """
        Provides operations to manage the schedule property of the microsoft.graph.team entity.
        """
        from .schedule.schedule_request_builder import ScheduleRequestBuilder

        return ScheduleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_activity_notification(self) -> SendActivityNotificationRequestBuilder:
        """
        Provides operations to call the sendActivityNotification method.
        """
        from .send_activity_notification.send_activity_notification_request_builder import SendActivityNotificationRequestBuilder

        return SendActivityNotificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tags(self) -> TagsRequestBuilder:
        """
        Provides operations to manage the tags property of the microsoft.graph.team entity.
        """
        from .tags.tags_request_builder import TagsRequestBuilder

        return TagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def template(self) -> TemplateRequestBuilder:
        """
        Provides operations to manage the template property of the microsoft.graph.team entity.
        """
        from .template.template_request_builder import TemplateRequestBuilder

        return TemplateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def template_definition(self) -> TemplateDefinitionRequestBuilder:
        """
        Provides operations to manage the templateDefinition property of the microsoft.graph.team entity.
        """
        from .template_definition.template_definition_request_builder import TemplateDefinitionRequestBuilder

        return TemplateDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unarchive(self) -> UnarchiveRequestBuilder:
        """
        Provides operations to call the unarchive method.
        """
        from .unarchive.unarchive_request_builder import UnarchiveRequestBuilder

        return UnarchiveRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TeamItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class TeamItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of the specified team.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TeamItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[TeamItemRequestBuilder.TeamItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TeamItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

