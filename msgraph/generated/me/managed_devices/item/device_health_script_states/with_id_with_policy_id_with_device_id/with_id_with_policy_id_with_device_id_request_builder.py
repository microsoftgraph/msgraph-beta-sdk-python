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
    from ......models import device_health_script_policy_state
    from ......models.o_data_errors import o_data_error

class WithIdWithPolicyIdWithDeviceIdRequestBuilder():
    """
    Provides operations to manage the deviceHealthScriptStates property of the microsoft.graph.managedDevice entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, device_id: Optional[str] = None, id: Optional[str] = None, policy_id: Optional[str] = None) -> None:
        """
        Instantiates a new WithIdWithPolicyIdWithDeviceIdRequestBuilder and sets the default values.
        Args:
            deviceId: Property in multi-part unique identifier of deviceHealthScriptPolicyState
            id: Property in multi-part unique identifier of deviceHealthScriptPolicyState
            pathParameters: The raw url or the Url template parameters for the request.
            policyId: Property in multi-part unique identifier of deviceHealthScriptPolicyState
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/managedDevices/{managedDevice%2Did}/deviceHealthScriptStates/id='{id}',policyId='{policyId}',deviceId='{deviceId}'{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        url_tpl_params[""] = deviceId
        url_tpl_params[""] = id
        url_tpl_params[""] = policyId
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[WithIdWithPolicyIdWithDeviceIdRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property deviceHealthScriptStates for me
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[WithIdWithPolicyIdWithDeviceIdRequestBuilderGetRequestConfiguration] = None) -> Optional[device_health_script_policy_state.DeviceHealthScriptPolicyState]:
        """
        Results of device health scripts that ran for this device. Default is empty list. This property is read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_health_script_policy_state.DeviceHealthScriptPolicyState]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import device_health_script_policy_state

        return await self.request_adapter.send_async(request_info, device_health_script_policy_state.DeviceHealthScriptPolicyState, error_mapping)
    
    async def patch(self,body: Optional[device_health_script_policy_state.DeviceHealthScriptPolicyState] = None, request_configuration: Optional[WithIdWithPolicyIdWithDeviceIdRequestBuilderPatchRequestConfiguration] = None) -> Optional[device_health_script_policy_state.DeviceHealthScriptPolicyState]:
        """
        Update the navigation property deviceHealthScriptStates in me
        Args:
            body: Contains properties for policy run state of the device health script.
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_health_script_policy_state.DeviceHealthScriptPolicyState]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import device_health_script_policy_state

        return await self.request_adapter.send_async(request_info, device_health_script_policy_state.DeviceHealthScriptPolicyState, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[WithIdWithPolicyIdWithDeviceIdRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property deviceHealthScriptStates for me
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
    
    def to_get_request_information(self,request_configuration: Optional[WithIdWithPolicyIdWithDeviceIdRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Results of device health scripts that ran for this device. Default is empty list. This property is read-only.
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
    
    def to_patch_request_information(self,body: Optional[device_health_script_policy_state.DeviceHealthScriptPolicyState] = None, request_configuration: Optional[WithIdWithPolicyIdWithDeviceIdRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property deviceHealthScriptStates in me
        Args:
            body: Contains properties for policy run state of the device health script.
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
    
    @dataclass
    class WithIdWithPolicyIdWithDeviceIdRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class WithIdWithPolicyIdWithDeviceIdRequestBuilderGetQueryParameters():
        """
        Results of device health scripts that ran for this device. Default is empty list. This property is read-only.
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
    class WithIdWithPolicyIdWithDeviceIdRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[WithIdWithPolicyIdWithDeviceIdRequestBuilder.WithIdWithPolicyIdWithDeviceIdRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class WithIdWithPolicyIdWithDeviceIdRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

