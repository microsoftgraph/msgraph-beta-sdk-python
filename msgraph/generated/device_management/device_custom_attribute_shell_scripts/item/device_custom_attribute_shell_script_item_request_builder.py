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
    from ....models import device_custom_attribute_shell_script
    from ....models.o_data_errors import o_data_error
    from .assign import assign_request_builder
    from .assignments import assignments_request_builder
    from .device_run_states import device_run_states_request_builder
    from .group_assignments import group_assignments_request_builder
    from .run_summary import run_summary_request_builder
    from .user_run_states import user_run_states_request_builder

class DeviceCustomAttributeShellScriptItemRequestBuilder():
    """
    Provides operations to manage the deviceCustomAttributeShellScripts property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceCustomAttributeShellScriptItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/deviceCustomAttributeShellScripts/{deviceCustomAttributeShellScript%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[DeviceCustomAttributeShellScriptItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property deviceCustomAttributeShellScripts for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[DeviceCustomAttributeShellScriptItemRequestBuilderGetRequestConfiguration] = None) -> Optional[device_custom_attribute_shell_script.DeviceCustomAttributeShellScript]:
        """
        The list of device custom attribute shell scripts associated with the tenant.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_custom_attribute_shell_script.DeviceCustomAttributeShellScript]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import device_custom_attribute_shell_script

        return await self.request_adapter.send_async(request_info, device_custom_attribute_shell_script.DeviceCustomAttributeShellScript, error_mapping)
    
    async def patch(self,body: Optional[device_custom_attribute_shell_script.DeviceCustomAttributeShellScript] = None, request_configuration: Optional[DeviceCustomAttributeShellScriptItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[device_custom_attribute_shell_script.DeviceCustomAttributeShellScript]:
        """
        Update the navigation property deviceCustomAttributeShellScripts in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_custom_attribute_shell_script.DeviceCustomAttributeShellScript]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import device_custom_attribute_shell_script

        return await self.request_adapter.send_async(request_info, device_custom_attribute_shell_script.DeviceCustomAttributeShellScript, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[DeviceCustomAttributeShellScriptItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property deviceCustomAttributeShellScripts for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[DeviceCustomAttributeShellScriptItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The list of device custom attribute shell scripts associated with the tenant.
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
    
    def to_patch_request_information(self,body: Optional[device_custom_attribute_shell_script.DeviceCustomAttributeShellScript] = None, request_configuration: Optional[DeviceCustomAttributeShellScriptItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property deviceCustomAttributeShellScripts in deviceManagement
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
    def assign(self) -> assign_request_builder.AssignRequestBuilder:
        """
        Provides operations to call the assign method.
        """
        from .assign import assign_request_builder

        return assign_request_builder.AssignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> assignments_request_builder.AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.deviceCustomAttributeShellScript entity.
        """
        from .assignments import assignments_request_builder

        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_run_states(self) -> device_run_states_request_builder.DeviceRunStatesRequestBuilder:
        """
        Provides operations to manage the deviceRunStates property of the microsoft.graph.deviceCustomAttributeShellScript entity.
        """
        from .device_run_states import device_run_states_request_builder

        return device_run_states_request_builder.DeviceRunStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_assignments(self) -> group_assignments_request_builder.GroupAssignmentsRequestBuilder:
        """
        Provides operations to manage the groupAssignments property of the microsoft.graph.deviceCustomAttributeShellScript entity.
        """
        from .group_assignments import group_assignments_request_builder

        return group_assignments_request_builder.GroupAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def run_summary(self) -> run_summary_request_builder.RunSummaryRequestBuilder:
        """
        Provides operations to manage the runSummary property of the microsoft.graph.deviceCustomAttributeShellScript entity.
        """
        from .run_summary import run_summary_request_builder

        return run_summary_request_builder.RunSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_run_states(self) -> user_run_states_request_builder.UserRunStatesRequestBuilder:
        """
        Provides operations to manage the userRunStates property of the microsoft.graph.deviceCustomAttributeShellScript entity.
        """
        from .user_run_states import user_run_states_request_builder

        return user_run_states_request_builder.UserRunStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DeviceCustomAttributeShellScriptItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DeviceCustomAttributeShellScriptItemRequestBuilderGetQueryParameters():
        """
        The list of device custom attribute shell scripts associated with the tenant.
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
    class DeviceCustomAttributeShellScriptItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DeviceCustomAttributeShellScriptItemRequestBuilder.DeviceCustomAttributeShellScriptItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DeviceCustomAttributeShellScriptItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

