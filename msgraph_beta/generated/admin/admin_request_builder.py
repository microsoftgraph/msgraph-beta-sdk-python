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
    from ..models.admin import Admin
    from ..models.o_data_errors.o_data_error import ODataError
    from .apps_and_services.apps_and_services_request_builder import AppsAndServicesRequestBuilder
    from .dynamics.dynamics_request_builder import DynamicsRequestBuilder
    from .edge.edge_request_builder import EdgeRequestBuilder
    from .forms.forms_request_builder import FormsRequestBuilder
    from .microsoft365_apps.microsoft365_apps_request_builder import Microsoft365AppsRequestBuilder
    from .people.people_request_builder import PeopleRequestBuilder
    from .report_settings.report_settings_request_builder import ReportSettingsRequestBuilder
    from .service_announcement.service_announcement_request_builder import ServiceAnnouncementRequestBuilder
    from .sharepoint.sharepoint_request_builder import SharepointRequestBuilder
    from .todo.todo_request_builder import TodoRequestBuilder
    from .windows.windows_request_builder import WindowsRequestBuilder

class AdminRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AdminRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/admin{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[AdminRequestBuilderGetRequestConfiguration] = None) -> Optional[Admin]:
        """
        Get admin
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Admin]
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
        from ..models.admin import Admin

        return await self.request_adapter.send_async(request_info, Admin, error_mapping)
    
    async def patch(self,body: Optional[Admin] = None, request_configuration: Optional[AdminRequestBuilderPatchRequestConfiguration] = None) -> Optional[Admin]:
        """
        Update admin
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Admin]
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
        from ..models.admin import Admin

        return await self.request_adapter.send_async(request_info, Admin, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[AdminRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get admin
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
    
    def to_patch_request_information(self,body: Optional[Admin] = None, request_configuration: Optional[AdminRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update admin
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
    
    def with_url(self,raw_url: Optional[str] = None) -> AdminRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AdminRequestBuilder
        """
        if not raw_url:
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
    class AdminRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AdminRequestBuilder.AdminRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AdminRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

