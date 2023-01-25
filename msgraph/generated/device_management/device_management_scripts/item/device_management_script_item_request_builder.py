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

assign_request_builder = lazy_import('msgraph.generated.device_management.device_management_scripts.item.assign.assign_request_builder')
assignments_request_builder = lazy_import('msgraph.generated.device_management.device_management_scripts.item.assignments.assignments_request_builder')
device_management_script_assignment_item_request_builder = lazy_import('msgraph.generated.device_management.device_management_scripts.item.assignments.item.device_management_script_assignment_item_request_builder')
device_run_states_request_builder = lazy_import('msgraph.generated.device_management.device_management_scripts.item.device_run_states.device_run_states_request_builder')
device_management_script_device_state_item_request_builder = lazy_import('msgraph.generated.device_management.device_management_scripts.item.device_run_states.item.device_management_script_device_state_item_request_builder')
group_assignments_request_builder = lazy_import('msgraph.generated.device_management.device_management_scripts.item.group_assignments.group_assignments_request_builder')
device_management_script_group_assignment_item_request_builder = lazy_import('msgraph.generated.device_management.device_management_scripts.item.group_assignments.item.device_management_script_group_assignment_item_request_builder')
run_summary_request_builder = lazy_import('msgraph.generated.device_management.device_management_scripts.item.run_summary.run_summary_request_builder')
user_run_states_request_builder = lazy_import('msgraph.generated.device_management.device_management_scripts.item.user_run_states.user_run_states_request_builder')
device_management_script_user_state_item_request_builder = lazy_import('msgraph.generated.device_management.device_management_scripts.item.user_run_states.item.device_management_script_user_state_item_request_builder')
device_management_script = lazy_import('msgraph.generated.models.device_management_script')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class DeviceManagementScriptItemRequestBuilder():
    """
    Provides operations to manage the deviceManagementScripts property of the microsoft.graph.deviceManagement entity.
    """
    @property
    def assign(self) -> assign_request_builder.AssignRequestBuilder:
        """
        Provides operations to call the assign method.
        """
        return assign_request_builder.AssignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> assignments_request_builder.AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.deviceManagementScript entity.
        """
        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_run_states(self) -> device_run_states_request_builder.DeviceRunStatesRequestBuilder:
        """
        Provides operations to manage the deviceRunStates property of the microsoft.graph.deviceManagementScript entity.
        """
        return device_run_states_request_builder.DeviceRunStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group_assignments(self) -> group_assignments_request_builder.GroupAssignmentsRequestBuilder:
        """
        Provides operations to manage the groupAssignments property of the microsoft.graph.deviceManagementScript entity.
        """
        return group_assignments_request_builder.GroupAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def run_summary(self) -> run_summary_request_builder.RunSummaryRequestBuilder:
        """
        Provides operations to manage the runSummary property of the microsoft.graph.deviceManagementScript entity.
        """
        return run_summary_request_builder.RunSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_run_states(self) -> user_run_states_request_builder.UserRunStatesRequestBuilder:
        """
        Provides operations to manage the userRunStates property of the microsoft.graph.deviceManagementScript entity.
        """
        return user_run_states_request_builder.UserRunStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def assignments_by_id(self,id: str) -> device_management_script_assignment_item_request_builder.DeviceManagementScriptAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.deviceManagementScript entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_script_assignment_item_request_builder.DeviceManagementScriptAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementScriptAssignment%2Did"] = id
        return device_management_script_assignment_item_request_builder.DeviceManagementScriptAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceManagementScriptItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/deviceManagementScripts/{deviceManagementScript%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[DeviceManagementScriptItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property deviceManagementScripts for deviceManagement
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
    
    def device_run_states_by_id(self,id: str) -> device_management_script_device_state_item_request_builder.DeviceManagementScriptDeviceStateItemRequestBuilder:
        """
        Provides operations to manage the deviceRunStates property of the microsoft.graph.deviceManagementScript entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_script_device_state_item_request_builder.DeviceManagementScriptDeviceStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementScriptDeviceState%2Did"] = id
        return device_management_script_device_state_item_request_builder.DeviceManagementScriptDeviceStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[DeviceManagementScriptItemRequestBuilderGetRequestConfiguration] = None) -> Optional[device_management_script.DeviceManagementScript]:
        """
        The list of device management scripts associated with the tenant.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_management_script.DeviceManagementScript]
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
        return await self.request_adapter.send_async(request_info, device_management_script.DeviceManagementScript, error_mapping)
    
    def group_assignments_by_id(self,id: str) -> device_management_script_group_assignment_item_request_builder.DeviceManagementScriptGroupAssignmentItemRequestBuilder:
        """
        Provides operations to manage the groupAssignments property of the microsoft.graph.deviceManagementScript entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_script_group_assignment_item_request_builder.DeviceManagementScriptGroupAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementScriptGroupAssignment%2Did"] = id
        return device_management_script_group_assignment_item_request_builder.DeviceManagementScriptGroupAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[device_management_script.DeviceManagementScript] = None, request_configuration: Optional[DeviceManagementScriptItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[device_management_script.DeviceManagementScript]:
        """
        Update the navigation property deviceManagementScripts in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_management_script.DeviceManagementScript]
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
        return await self.request_adapter.send_async(request_info, device_management_script.DeviceManagementScript, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[DeviceManagementScriptItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property deviceManagementScripts for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[DeviceManagementScriptItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The list of device management scripts associated with the tenant.
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
    
    def to_patch_request_information(self,body: Optional[device_management_script.DeviceManagementScript] = None, request_configuration: Optional[DeviceManagementScriptItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property deviceManagementScripts in deviceManagement
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
    
    def user_run_states_by_id(self,id: str) -> device_management_script_user_state_item_request_builder.DeviceManagementScriptUserStateItemRequestBuilder:
        """
        Provides operations to manage the userRunStates property of the microsoft.graph.deviceManagementScript entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_script_user_state_item_request_builder.DeviceManagementScriptUserStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementScriptUserState%2Did"] = id
        return device_management_script_user_state_item_request_builder.DeviceManagementScriptUserStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class DeviceManagementScriptItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DeviceManagementScriptItemRequestBuilderGetQueryParameters():
        """
        The list of device management scripts associated with the tenant.
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
    class DeviceManagementScriptItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DeviceManagementScriptItemRequestBuilder.DeviceManagementScriptItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DeviceManagementScriptItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

