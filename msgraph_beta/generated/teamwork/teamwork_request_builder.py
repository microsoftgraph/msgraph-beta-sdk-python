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
    from ..models.o_data_errors.o_data_error import ODataError
    from ..models.teamwork import Teamwork
    from .deleted_chats.deleted_chats_request_builder import DeletedChatsRequestBuilder
    from .deleted_teams.deleted_teams_request_builder import DeletedTeamsRequestBuilder
    from .devices.devices_request_builder import DevicesRequestBuilder
    from .send_activity_notification_to_recipients.send_activity_notification_to_recipients_request_builder import SendActivityNotificationToRecipientsRequestBuilder
    from .teams_app_settings.teams_app_settings_request_builder import TeamsAppSettingsRequestBuilder
    from .team_templates.team_templates_request_builder import TeamTemplatesRequestBuilder
    from .workforce_integrations.workforce_integrations_request_builder import WorkforceIntegrationsRequestBuilder

class TeamworkRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the teamwork singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TeamworkRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/teamwork{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[TeamworkRequestBuilderGetRequestConfiguration] = None) -> Optional[Teamwork]:
        """
        Get the properties and relationships of a teamwork object, such as the region of the organization and whether Microsoft Teams is enabled.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Teamwork]
        Find more info here: https://learn.microsoft.com/graph/api/teamwork-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.teamwork import Teamwork

        return await self.request_adapter.send_async(request_info, Teamwork, error_mapping)
    
    async def patch(self,body: Optional[Teamwork] = None, request_configuration: Optional[TeamworkRequestBuilderPatchRequestConfiguration] = None) -> Optional[Teamwork]:
        """
        Update teamwork
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Teamwork]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.teamwork import Teamwork

        return await self.request_adapter.send_async(request_info, Teamwork, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[TeamworkRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the properties and relationships of a teamwork object, such as the region of the organization and whether Microsoft Teams is enabled.
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
    
    def to_patch_request_information(self,body: Optional[Teamwork] = None, request_configuration: Optional[TeamworkRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update teamwork
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
    
    def with_url(self,raw_url: Optional[str] = None) -> TeamworkRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TeamworkRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return TeamworkRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def deleted_chats(self) -> DeletedChatsRequestBuilder:
        """
        Provides operations to manage the deletedChats property of the microsoft.graph.teamwork entity.
        """
        from .deleted_chats.deleted_chats_request_builder import DeletedChatsRequestBuilder

        return DeletedChatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deleted_teams(self) -> DeletedTeamsRequestBuilder:
        """
        Provides operations to manage the deletedTeams property of the microsoft.graph.teamwork entity.
        """
        from .deleted_teams.deleted_teams_request_builder import DeletedTeamsRequestBuilder

        return DeletedTeamsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def devices(self) -> DevicesRequestBuilder:
        """
        Provides operations to manage the devices property of the microsoft.graph.teamwork entity.
        """
        from .devices.devices_request_builder import DevicesRequestBuilder

        return DevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_activity_notification_to_recipients(self) -> SendActivityNotificationToRecipientsRequestBuilder:
        """
        Provides operations to call the sendActivityNotificationToRecipients method.
        """
        from .send_activity_notification_to_recipients.send_activity_notification_to_recipients_request_builder import SendActivityNotificationToRecipientsRequestBuilder

        return SendActivityNotificationToRecipientsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def team_templates(self) -> TeamTemplatesRequestBuilder:
        """
        Provides operations to manage the teamTemplates property of the microsoft.graph.teamwork entity.
        """
        from .team_templates.team_templates_request_builder import TeamTemplatesRequestBuilder

        return TeamTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def teams_app_settings(self) -> TeamsAppSettingsRequestBuilder:
        """
        Provides operations to manage the teamsAppSettings property of the microsoft.graph.teamwork entity.
        """
        from .teams_app_settings.teams_app_settings_request_builder import TeamsAppSettingsRequestBuilder

        return TeamsAppSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def workforce_integrations(self) -> WorkforceIntegrationsRequestBuilder:
        """
        Provides operations to manage the workforceIntegrations property of the microsoft.graph.teamwork entity.
        """
        from .workforce_integrations.workforce_integrations_request_builder import WorkforceIntegrationsRequestBuilder

        return WorkforceIntegrationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TeamworkRequestBuilderGetQueryParameters():
        """
        Get the properties and relationships of a teamwork object, such as the region of the organization and whether Microsoft Teams is enabled.
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
    class TeamworkRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[TeamworkRequestBuilder.TeamworkRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TeamworkRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

