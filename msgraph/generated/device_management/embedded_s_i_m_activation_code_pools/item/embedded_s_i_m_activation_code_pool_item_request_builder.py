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

assign_request_builder = lazy_import('msgraph.generated.device_management.embedded_s_i_m_activation_code_pools.item.assign.assign_request_builder')
assignments_request_builder = lazy_import('msgraph.generated.device_management.embedded_s_i_m_activation_code_pools.item.assignments.assignments_request_builder')
embedded_s_i_m_activation_code_pool_assignment_item_request_builder = lazy_import('msgraph.generated.device_management.embedded_s_i_m_activation_code_pools.item.assignments.item.embedded_s_i_m_activation_code_pool_assignment_item_request_builder')
device_states_request_builder = lazy_import('msgraph.generated.device_management.embedded_s_i_m_activation_code_pools.item.device_states.device_states_request_builder')
embedded_s_i_m_device_state_item_request_builder = lazy_import('msgraph.generated.device_management.embedded_s_i_m_activation_code_pools.item.device_states.item.embedded_s_i_m_device_state_item_request_builder')
embedded_s_i_m_activation_code_pool = lazy_import('msgraph.generated.models.embedded_s_i_m_activation_code_pool')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class EmbeddedSIMActivationCodePoolItemRequestBuilder():
    """
    Provides operations to manage the embeddedSIMActivationCodePools property of the microsoft.graph.deviceManagement entity.
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
        Provides operations to manage the assignments property of the microsoft.graph.embeddedSIMActivationCodePool entity.
        """
        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_states(self) -> device_states_request_builder.DeviceStatesRequestBuilder:
        """
        Provides operations to manage the deviceStates property of the microsoft.graph.embeddedSIMActivationCodePool entity.
        """
        return device_states_request_builder.DeviceStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def assignments_by_id(self,id: str) -> embedded_s_i_m_activation_code_pool_assignment_item_request_builder.EmbeddedSIMActivationCodePoolAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.embeddedSIMActivationCodePool entity.
        Args:
            id: Unique identifier of the item
        Returns: embedded_s_i_m_activation_code_pool_assignment_item_request_builder.EmbeddedSIMActivationCodePoolAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["embeddedSIMActivationCodePoolAssignment%2Did"] = id
        return embedded_s_i_m_activation_code_pool_assignment_item_request_builder.EmbeddedSIMActivationCodePoolAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EmbeddedSIMActivationCodePoolItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/embeddedSIMActivationCodePools/{embeddedSIMActivationCodePool%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[EmbeddedSIMActivationCodePoolItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property embeddedSIMActivationCodePools for deviceManagement
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
    
    def create_get_request_information(self,request_configuration: Optional[EmbeddedSIMActivationCodePoolItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The embedded SIM activation code pools created by this account.
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
    
    def create_patch_request_information(self,body: Optional[embedded_s_i_m_activation_code_pool.EmbeddedSIMActivationCodePool] = None, request_configuration: Optional[EmbeddedSIMActivationCodePoolItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property embeddedSIMActivationCodePools in deviceManagement
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
    
    async def delete(self,request_configuration: Optional[EmbeddedSIMActivationCodePoolItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property embeddedSIMActivationCodePools for deviceManagement
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
    
    def device_states_by_id(self,id: str) -> embedded_s_i_m_device_state_item_request_builder.EmbeddedSIMDeviceStateItemRequestBuilder:
        """
        Provides operations to manage the deviceStates property of the microsoft.graph.embeddedSIMActivationCodePool entity.
        Args:
            id: Unique identifier of the item
        Returns: embedded_s_i_m_device_state_item_request_builder.EmbeddedSIMDeviceStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["embeddedSIMDeviceState%2Did"] = id
        return embedded_s_i_m_device_state_item_request_builder.EmbeddedSIMDeviceStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[EmbeddedSIMActivationCodePoolItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[embedded_s_i_m_activation_code_pool.EmbeddedSIMActivationCodePool]:
        """
        The embedded SIM activation code pools created by this account.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[embedded_s_i_m_activation_code_pool.EmbeddedSIMActivationCodePool]
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
        return await self.request_adapter.send_async(request_info, embedded_s_i_m_activation_code_pool.EmbeddedSIMActivationCodePool, response_handler, error_mapping)
    
    async def patch(self,body: Optional[embedded_s_i_m_activation_code_pool.EmbeddedSIMActivationCodePool] = None, request_configuration: Optional[EmbeddedSIMActivationCodePoolItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[embedded_s_i_m_activation_code_pool.EmbeddedSIMActivationCodePool]:
        """
        Update the navigation property embeddedSIMActivationCodePools in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[embedded_s_i_m_activation_code_pool.EmbeddedSIMActivationCodePool]
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
        return await self.request_adapter.send_async(request_info, embedded_s_i_m_activation_code_pool.EmbeddedSIMActivationCodePool, response_handler, error_mapping)
    
    @dataclass
    class EmbeddedSIMActivationCodePoolItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class EmbeddedSIMActivationCodePoolItemRequestBuilderGetQueryParameters():
        """
        The embedded SIM activation code pools created by this account.
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
    class EmbeddedSIMActivationCodePoolItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EmbeddedSIMActivationCodePoolItemRequestBuilder.EmbeddedSIMActivationCodePoolItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class EmbeddedSIMActivationCodePoolItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

