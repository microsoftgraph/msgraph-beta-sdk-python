from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ..models.admin import Admin
    from ..models.o_data_errors.o_data_error import ODataError
    from .apps_and_services.apps_and_services_request_builder import AppsAndServicesRequestBuilder
    from .configuration_management.configuration_management_request_builder import ConfigurationManagementRequestBuilder
    from .dynamics.dynamics_request_builder import DynamicsRequestBuilder
    from .edge.edge_request_builder import EdgeRequestBuilder
    from .entra.entra_request_builder import EntraRequestBuilder
    from .exchange.exchange_request_builder import ExchangeRequestBuilder
    from .forms.forms_request_builder import FormsRequestBuilder
    from .microsoft365_apps.microsoft365_apps_request_builder import Microsoft365AppsRequestBuilder
    from .people.people_request_builder import PeopleRequestBuilder
    from .report_settings.report_settings_request_builder import ReportSettingsRequestBuilder
    from .service_announcement.service_announcement_request_builder import ServiceAnnouncementRequestBuilder
    from .sharepoint.sharepoint_request_builder import SharepointRequestBuilder
    from .teams.teams_request_builder import TeamsRequestBuilder
    from .todo.todo_request_builder import TodoRequestBuilder
    from .windows.windows_request_builder import WindowsRequestBuilder

class AdminRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AdminRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/admin{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AdminRequestBuilderGetQueryParameters]] = None) -> Optional[Admin]:
        """
        Get admin
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Admin]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.admin import Admin

        return await self.request_adapter.send_async(request_info, Admin, error_mapping)
    
    async def patch(self,body: Admin, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Admin]:
        """
        Update admin
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Admin]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.admin import Admin

        return await self.request_adapter.send_async(request_info, Admin, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AdminRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get admin
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Admin, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update admin
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> AdminRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AdminRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AdminRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def apps_and_services(self) -> AppsAndServicesRequestBuilder:
        """
        Provides operations to manage the appsAndServices property of the microsoft.graph.admin entity.
        """
        from .apps_and_services.apps_and_services_request_builder import AppsAndServicesRequestBuilder

        return AppsAndServicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def configuration_management(self) -> ConfigurationManagementRequestBuilder:
        """
        Provides operations to manage the configurationManagement property of the microsoft.graph.admin entity.
        """
        from .configuration_management.configuration_management_request_builder import ConfigurationManagementRequestBuilder

        return ConfigurationManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dynamics(self) -> DynamicsRequestBuilder:
        """
        Provides operations to manage the dynamics property of the microsoft.graph.admin entity.
        """
        from .dynamics.dynamics_request_builder import DynamicsRequestBuilder

        return DynamicsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def edge(self) -> EdgeRequestBuilder:
        """
        Provides operations to manage the edge property of the microsoft.graph.admin entity.
        """
        from .edge.edge_request_builder import EdgeRequestBuilder

        return EdgeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def entra(self) -> EntraRequestBuilder:
        """
        Provides operations to manage the entra property of the microsoft.graph.admin entity.
        """
        from .entra.entra_request_builder import EntraRequestBuilder

        return EntraRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exchange(self) -> ExchangeRequestBuilder:
        """
        Provides operations to manage the exchange property of the microsoft.graph.admin entity.
        """
        from .exchange.exchange_request_builder import ExchangeRequestBuilder

        return ExchangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def forms(self) -> FormsRequestBuilder:
        """
        Provides operations to manage the forms property of the microsoft.graph.admin entity.
        """
        from .forms.forms_request_builder import FormsRequestBuilder

        return FormsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft365_apps(self) -> Microsoft365AppsRequestBuilder:
        """
        Provides operations to manage the microsoft365Apps property of the microsoft.graph.admin entity.
        """
        from .microsoft365_apps.microsoft365_apps_request_builder import Microsoft365AppsRequestBuilder

        return Microsoft365AppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def people(self) -> PeopleRequestBuilder:
        """
        Provides operations to manage the people property of the microsoft.graph.admin entity.
        """
        from .people.people_request_builder import PeopleRequestBuilder

        return PeopleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def report_settings(self) -> ReportSettingsRequestBuilder:
        """
        Provides operations to manage the reportSettings property of the microsoft.graph.admin entity.
        """
        from .report_settings.report_settings_request_builder import ReportSettingsRequestBuilder

        return ReportSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_announcement(self) -> ServiceAnnouncementRequestBuilder:
        """
        Provides operations to manage the serviceAnnouncement property of the microsoft.graph.admin entity.
        """
        from .service_announcement.service_announcement_request_builder import ServiceAnnouncementRequestBuilder

        return ServiceAnnouncementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sharepoint(self) -> SharepointRequestBuilder:
        """
        Provides operations to manage the sharepoint property of the microsoft.graph.admin entity.
        """
        from .sharepoint.sharepoint_request_builder import SharepointRequestBuilder

        return SharepointRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def teams(self) -> TeamsRequestBuilder:
        """
        Provides operations to manage the teams property of the microsoft.graph.admin entity.
        """
        from .teams.teams_request_builder import TeamsRequestBuilder

        return TeamsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def todo(self) -> TodoRequestBuilder:
        """
        Provides operations to manage the todo property of the microsoft.graph.admin entity.
        """
        from .todo.todo_request_builder import TodoRequestBuilder

        return TodoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows(self) -> WindowsRequestBuilder:
        """
        Provides operations to manage the windows property of the microsoft.graph.admin entity.
        """
        from .windows.windows_request_builder import WindowsRequestBuilder

        return WindowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AdminRequestBuilderGetQueryParameters():
        """
        Get admin
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class AdminRequestBuilderGetRequestConfiguration(RequestConfiguration[AdminRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AdminRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

