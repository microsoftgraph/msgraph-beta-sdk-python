from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
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

class TeamworkDeviceItemRequestBuilder():
    """
    Provides operations to manage the devices property of the microsoft.graph.teamwork entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TeamworkDeviceItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/teamwork/devices/{teamworkDevice%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[TeamworkDeviceItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property devices for teamwork
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
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
        Get the properties of a Microsoft Teams-enabled device. For example, you can use this method to get the device type, hardware detail, activity state, and health status information for a device that's enabled for Teams.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TeamworkDevice]
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
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def to_get_request_information(self,request_configuration: Optional[TeamworkDeviceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the properties of a Microsoft Teams-enabled device. For example, you can use this method to get the device type, hardware detail, activity state, and health status information for a device that's enabled for Teams.
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
    
    def to_patch_request_information(self,body: Optional[TeamworkDevice] = None, request_configuration: Optional[TeamworkDeviceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property devices in teamwork
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
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
    
    @dataclass
    class TeamworkDeviceItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class TeamworkDeviceItemRequestBuilderGetQueryParameters():
        """
        Get the properties of a Microsoft Teams-enabled device. For example, you can use this method to get the device type, hardware detail, activity state, and health status information for a device that's enabled for Teams.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
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

    
    @dataclass
    class TeamworkDeviceItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TeamworkDeviceItemRequestBuilder.TeamworkDeviceItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class TeamworkDeviceItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

