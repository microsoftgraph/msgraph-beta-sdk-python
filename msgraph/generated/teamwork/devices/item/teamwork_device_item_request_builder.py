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
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.teamwork_device import TeamworkDevice
    from .activity.activity_request_builder import ActivityRequestBuilder
    from .configuration.configuration_request_builder import ConfigurationRequestBuilder
    from .health.health_request_builder import HealthRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .restart.restart_request_builder import RestartRequestBuilder
    from .run_diagnostics.run_diagnostics_request_builder import RunDiagnosticsRequestBuilder
    from .update_software.update_software_request_builder import UpdateSoftwareRequestBuilder

class TeamworkDeviceItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the devices property of the microsoft.graph.teamwork entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TeamworkDeviceItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/teamwork/devices/{teamworkDevice%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[TeamworkDeviceItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property devices for teamwork
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[TeamworkDeviceItemRequestBuilderGetRequestConfiguration] = None) -> Optional[TeamworkDevice]:
        """
        Get the properties of a Microsoft Teams-enabled device. For example, you can use this method to get the device type, hardware detail, activity state, and health status information for a device that's enabled for Teams. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TeamworkDevice]
        Find more info here: https://learn.microsoft.com/graph/api/teamworkdevice-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.teamwork_device import TeamworkDevice

        return await self.request_adapter.send_async(request_info, TeamworkDevice, error_mapping)
    
    async def patch(self,body: Optional[TeamworkDevice] = None, request_configuration: Optional[TeamworkDeviceItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[TeamworkDevice]:
        """
        Update the navigation property devices in teamwork
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TeamworkDevice]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.teamwork_device import TeamworkDevice

        return await self.request_adapter.send_async(request_info, TeamworkDevice, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[TeamworkDeviceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property devices for teamwork
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
        request_info.headers.try_add("Accept", "application/json, application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[TeamworkDeviceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the properties of a Microsoft Teams-enabled device. For example, you can use this method to get the device type, hardware detail, activity state, and health status information for a device that's enabled for Teams. This API is available in the following national cloud deployments.
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
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
    
    def to_patch_request_information(self,body: Optional[TeamworkDevice] = None, request_configuration: Optional[TeamworkDeviceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property devices in teamwork
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
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> TeamworkDeviceItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TeamworkDeviceItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return TeamworkDeviceItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def activity(self) -> ActivityRequestBuilder:
        """
        Provides operations to manage the activity property of the microsoft.graph.teamworkDevice entity.
        """
        from .activity.activity_request_builder import ActivityRequestBuilder

        return ActivityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def configuration(self) -> ConfigurationRequestBuilder:
        """
        Provides operations to manage the configuration property of the microsoft.graph.teamworkDevice entity.
        """
        from .configuration.configuration_request_builder import ConfigurationRequestBuilder

        return ConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def health(self) -> HealthRequestBuilder:
        """
        Provides operations to manage the health property of the microsoft.graph.teamworkDevice entity.
        """
        from .health.health_request_builder import HealthRequestBuilder

        return HealthRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.teamworkDevice entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restart(self) -> RestartRequestBuilder:
        """
        Provides operations to call the restart method.
        """
        from .restart.restart_request_builder import RestartRequestBuilder

        return RestartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def run_diagnostics(self) -> RunDiagnosticsRequestBuilder:
        """
        Provides operations to call the runDiagnostics method.
        """
        from .run_diagnostics.run_diagnostics_request_builder import RunDiagnosticsRequestBuilder

        return RunDiagnosticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_software(self) -> UpdateSoftwareRequestBuilder:
        """
        Provides operations to call the updateSoftware method.
        """
        from .update_software.update_software_request_builder import UpdateSoftwareRequestBuilder

        return UpdateSoftwareRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TeamworkDeviceItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class TeamworkDeviceItemRequestBuilderGetQueryParameters():
        """
        Get the properties of a Microsoft Teams-enabled device. For example, you can use this method to get the device type, hardware detail, activity state, and health status information for a device that's enabled for Teams. This API is available in the following national cloud deployments.
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
    class TeamworkDeviceItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[TeamworkDeviceItemRequestBuilder.TeamworkDeviceItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TeamworkDeviceItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

