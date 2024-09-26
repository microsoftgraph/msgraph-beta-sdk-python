from __future__ import annotations
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
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ......models.device_health_script_policy_state import DeviceHealthScriptPolicyState
    from ......models.o_data_errors.o_data_error import ODataError

class WithIdWithPolicyIdWithDeviceIdRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the deviceHealthScriptStates property of the microsoft.graph.managedDevice entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]], device_id: Optional[str] = None, id: Optional[str] = None, policy_id: Optional[str] = None) -> None:
        """
        Instantiates a new WithIdWithPolicyIdWithDeviceIdRequestBuilder and sets the default values.
        param device_id: Property in multi-part unique identifier of deviceHealthScriptPolicyState
        param id: Property in multi-part unique identifier of deviceHealthScriptPolicyState
        param path_parameters: The raw url or the url-template parameters for the request.
        param policy_id: Property in multi-part unique identifier of deviceHealthScriptPolicyState
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['deviceId'] = device_id
            path_parameters['id'] = id
            path_parameters['policyId'] = policy_id
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/comanagedDevices/{managedDevice%2Did}/deviceHealthScriptStates/id='{id}',policyId='{policyId}',deviceId='{deviceId}'{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property deviceHealthScriptStates for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithIdWithPolicyIdWithDeviceIdRequestBuilderGetQueryParameters]] = None) -> Optional[DeviceHealthScriptPolicyState]:
        """
        Results of device health scripts that ran for this device. Default is empty list. This property is read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceHealthScriptPolicyState]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.device_health_script_policy_state import DeviceHealthScriptPolicyState

        return await self.request_adapter.send_async(request_info, DeviceHealthScriptPolicyState, error_mapping)
    
    async def patch(self,body: DeviceHealthScriptPolicyState, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DeviceHealthScriptPolicyState]:
        """
        Update the navigation property deviceHealthScriptStates in deviceManagement
        param body: Contains properties for policy run state of the device health script.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceHealthScriptPolicyState]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.device_health_script_policy_state import DeviceHealthScriptPolicyState

        return await self.request_adapter.send_async(request_info, DeviceHealthScriptPolicyState, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property deviceHealthScriptStates for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithIdWithPolicyIdWithDeviceIdRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Results of device health scripts that ran for this device. Default is empty list. This property is read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: DeviceHealthScriptPolicyState, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property deviceHealthScriptStates in deviceManagement
        param body: Contains properties for policy run state of the device health script.
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
    
    def with_url(self,raw_url: str) -> WithIdWithPolicyIdWithDeviceIdRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithIdWithPolicyIdWithDeviceIdRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithIdWithPolicyIdWithDeviceIdRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithIdWithPolicyIdWithDeviceIdRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithIdWithPolicyIdWithDeviceIdRequestBuilderGetQueryParameters():
        """
        Results of device health scripts that ran for this device. Default is empty list. This property is read-only.
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
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class WithIdWithPolicyIdWithDeviceIdRequestBuilderGetRequestConfiguration(RequestConfiguration[WithIdWithPolicyIdWithDeviceIdRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithIdWithPolicyIdWithDeviceIdRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

