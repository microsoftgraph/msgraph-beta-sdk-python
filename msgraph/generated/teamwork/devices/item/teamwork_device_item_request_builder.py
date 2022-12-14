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

teamwork_device = lazy_import('msgraph.generated.models.teamwork_device')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
activity_request_builder = lazy_import('msgraph.generated.teamwork.devices.item.activity.activity_request_builder')
configuration_request_builder = lazy_import('msgraph.generated.teamwork.devices.item.configuration.configuration_request_builder')
health_request_builder = lazy_import('msgraph.generated.teamwork.devices.item.health.health_request_builder')
operations_request_builder = lazy_import('msgraph.generated.teamwork.devices.item.operations.operations_request_builder')
teamwork_device_operation_item_request_builder = lazy_import('msgraph.generated.teamwork.devices.item.operations.item.teamwork_device_operation_item_request_builder')
restart_request_builder = lazy_import('msgraph.generated.teamwork.devices.item.restart.restart_request_builder')
run_diagnostics_request_builder = lazy_import('msgraph.generated.teamwork.devices.item.run_diagnostics.run_diagnostics_request_builder')
update_software_request_builder = lazy_import('msgraph.generated.teamwork.devices.item.update_software.update_software_request_builder')

class TeamworkDeviceItemRequestBuilder():
    """
    Provides operations to manage the devices property of the microsoft.graph.teamwork entity.
    """
    @property
    def activity(self) -> activity_request_builder.ActivityRequestBuilder:
        """
        Provides operations to manage the activity property of the microsoft.graph.teamworkDevice entity.
        """
        return activity_request_builder.ActivityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def configuration(self) -> configuration_request_builder.ConfigurationRequestBuilder:
        """
        Provides operations to manage the configuration property of the microsoft.graph.teamworkDevice entity.
        """
        return configuration_request_builder.ConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def health(self) -> health_request_builder.HealthRequestBuilder:
        """
        Provides operations to manage the health property of the microsoft.graph.teamworkDevice entity.
        """
        return health_request_builder.HealthRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.teamworkDevice entity.
        """
        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restart(self) -> restart_request_builder.RestartRequestBuilder:
        """
        Provides operations to call the restart method.
        """
        return restart_request_builder.RestartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def run_diagnostics(self) -> run_diagnostics_request_builder.RunDiagnosticsRequestBuilder:
        """
        Provides operations to call the runDiagnostics method.
        """
        return run_diagnostics_request_builder.RunDiagnosticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_software(self) -> update_software_request_builder.UpdateSoftwareRequestBuilder:
        """
        Provides operations to call the updateSoftware method.
        """
        return update_software_request_builder.UpdateSoftwareRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TeamworkDeviceItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/teamwork/devices/{teamworkDevice%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[TeamworkDeviceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
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
    
    def create_get_request_information(self,request_configuration: Optional[TeamworkDeviceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The Teams devices provisioned for the tenant.
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
    
    def create_patch_request_information(self,body: Optional[teamwork_device.TeamworkDevice] = None, request_configuration: Optional[TeamworkDeviceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property devices in teamwork
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
    
    async def delete(self,request_configuration: Optional[TeamworkDeviceItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property devices for teamwork
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[TeamworkDeviceItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[teamwork_device.TeamworkDevice]:
        """
        The Teams devices provisioned for the tenant.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[teamwork_device.TeamworkDevice]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, teamwork_device.TeamworkDevice, response_handler, error_mapping)
    
    def operations_by_id(self,id: str) -> teamwork_device_operation_item_request_builder.TeamworkDeviceOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.teamworkDevice entity.
        Args:
            id: Unique identifier of the item
        Returns: teamwork_device_operation_item_request_builder.TeamworkDeviceOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["teamworkDeviceOperation%2Did"] = id
        return teamwork_device_operation_item_request_builder.TeamworkDeviceOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[teamwork_device.TeamworkDevice] = None, request_configuration: Optional[TeamworkDeviceItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[teamwork_device.TeamworkDevice]:
        """
        Update the navigation property devices in teamwork
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[teamwork_device.TeamworkDevice]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, teamwork_device.TeamworkDevice, response_handler, error_mapping)
    
    @dataclass
    class TeamworkDeviceItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class TeamworkDeviceItemRequestBuilderGetQueryParameters():
        """
        The Teams devices provisioned for the tenant.
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
    class TeamworkDeviceItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

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
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

