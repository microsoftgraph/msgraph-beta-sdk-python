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
    from ...models import user_teamwork
    from ...models.o_data_errors import o_data_error
    from .associated_teams import associated_teams_request_builder
    from .associated_teams.item import associated_team_info_item_request_builder
    from .installed_apps import installed_apps_request_builder
    from .installed_apps.item import user_scope_teams_app_installation_item_request_builder
    from .send_activity_notification import send_activity_notification_request_builder

class TeamworkRequestBuilder():
    """
    Provides operations to manage the teamwork property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TeamworkRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/teamwork{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def associated_teams_by_id(self,id: str) -> associated_team_info_item_request_builder.AssociatedTeamInfoItemRequestBuilder:
        """
        Provides operations to manage the associatedTeams property of the microsoft.graph.userTeamwork entity.
        Args:
            id: Unique identifier of the item
        Returns: associated_team_info_item_request_builder.AssociatedTeamInfoItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .associated_teams.item import associated_team_info_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["associatedTeamInfo%2Did"] = id
        return associated_team_info_item_request_builder.AssociatedTeamInfoItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[TeamworkRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property teamwork for me
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[TeamworkRequestBuilderGetRequestConfiguration] = None) -> Optional[user_teamwork.UserTeamwork]:
        """
        A container for Microsoft Teams features available for the user. Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[user_teamwork.UserTeamwork]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import user_teamwork

        return await self.request_adapter.send_async(request_info, user_teamwork.UserTeamwork, error_mapping)
    
    def installed_apps_by_id(self,id: str) -> user_scope_teams_app_installation_item_request_builder.UserScopeTeamsAppInstallationItemRequestBuilder:
        """
        Provides operations to manage the installedApps property of the microsoft.graph.userTeamwork entity.
        Args:
            id: Unique identifier of the item
        Returns: user_scope_teams_app_installation_item_request_builder.UserScopeTeamsAppInstallationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .installed_apps.item import user_scope_teams_app_installation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userScopeTeamsAppInstallation%2Did"] = id
        return user_scope_teams_app_installation_item_request_builder.UserScopeTeamsAppInstallationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[user_teamwork.UserTeamwork] = None, request_configuration: Optional[TeamworkRequestBuilderPatchRequestConfiguration] = None) -> Optional[user_teamwork.UserTeamwork]:
        """
        Update the navigation property teamwork in me
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[user_teamwork.UserTeamwork]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import user_teamwork

        return await self.request_adapter.send_async(request_info, user_teamwork.UserTeamwork, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[TeamworkRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property teamwork for me
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
    
    def to_get_request_information(self,request_configuration: Optional[TeamworkRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        A container for Microsoft Teams features available for the user. Read-only. Nullable.
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
    
    def to_patch_request_information(self,body: Optional[user_teamwork.UserTeamwork] = None, request_configuration: Optional[TeamworkRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property teamwork in me
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
    def associated_teams(self) -> associated_teams_request_builder.AssociatedTeamsRequestBuilder:
        """
        Provides operations to manage the associatedTeams property of the microsoft.graph.userTeamwork entity.
        """
        from .associated_teams import associated_teams_request_builder

        return associated_teams_request_builder.AssociatedTeamsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def installed_apps(self) -> installed_apps_request_builder.InstalledAppsRequestBuilder:
        """
        Provides operations to manage the installedApps property of the microsoft.graph.userTeamwork entity.
        """
        from .installed_apps import installed_apps_request_builder

        return installed_apps_request_builder.InstalledAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_activity_notification(self) -> send_activity_notification_request_builder.SendActivityNotificationRequestBuilder:
        """
        Provides operations to call the sendActivityNotification method.
        """
        from .send_activity_notification import send_activity_notification_request_builder

        return send_activity_notification_request_builder.SendActivityNotificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TeamworkRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class TeamworkRequestBuilderGetQueryParameters():
        """
        A container for Microsoft Teams features available for the user. Read-only. Nullable.
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
    class TeamworkRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TeamworkRequestBuilder.TeamworkRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class TeamworkRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

