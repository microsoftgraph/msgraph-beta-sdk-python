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

count_request_builder = lazy_import('msgraph.generated.device_management.assignment_filters.count.count_request_builder')
enable_request_builder = lazy_import('msgraph.generated.device_management.assignment_filters.enable.enable_request_builder')
get_platform_supported_properties_with_platform_request_builder = lazy_import('msgraph.generated.device_management.assignment_filters.get_platform_supported_properties_with_platform.get_platform_supported_properties_with_platform_request_builder')
get_state_request_builder = lazy_import('msgraph.generated.device_management.assignment_filters.get_state.get_state_request_builder')
validate_filter_request_builder = lazy_import('msgraph.generated.device_management.assignment_filters.validate_filter.validate_filter_request_builder')
device_and_app_management_assignment_filter = lazy_import('msgraph.generated.models.device_and_app_management_assignment_filter')
device_and_app_management_assignment_filter_collection_response = lazy_import('msgraph.generated.models.device_and_app_management_assignment_filter_collection_response')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class AssignmentFiltersRequestBuilder():
    """
    Provides operations to manage the assignmentFilters property of the microsoft.graph.deviceManagement entity.
    """
    @property
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enable(self) -> enable_request_builder.EnableRequestBuilder:
        """
        Provides operations to call the enable method.
        """
        return enable_request_builder.EnableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def validate_filter(self) -> validate_filter_request_builder.ValidateFilterRequestBuilder:
        """
        Provides operations to call the validateFilter method.
        """
        return validate_filter_request_builder.ValidateFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AssignmentFiltersRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/assignmentFilters{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[AssignmentFiltersRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The list of assignment filters
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
    
    def create_post_request_information(self,body: Optional[device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter] = None, request_configuration: Optional[AssignmentFiltersRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to assignmentFilters for deviceManagement
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
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def get(self,request_configuration: Optional[AssignmentFiltersRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device_and_app_management_assignment_filter_collection_response.DeviceAndAppManagementAssignmentFilterCollectionResponse]:
        """
        The list of assignment filters
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device_and_app_management_assignment_filter_collection_response.DeviceAndAppManagementAssignmentFilterCollectionResponse]
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
        return await self.request_adapter.send_async(request_info, device_and_app_management_assignment_filter_collection_response.DeviceAndAppManagementAssignmentFilterCollectionResponse, response_handler, error_mapping)
    
    def get_platform_supported_properties_with_platform(self,platform: Optional[str] = None) -> get_platform_supported_properties_with_platform_request_builder.GetPlatformSupportedPropertiesWithPlatformRequestBuilder:
        """
        Provides operations to call the getPlatformSupportedProperties method.
        Args:
            platform: Usage: platform='{platform}'
        Returns: get_platform_supported_properties_with_platform_request_builder.GetPlatformSupportedPropertiesWithPlatformRequestBuilder
        """
        if platform is None:
            raise Exception("platform cannot be undefined")
        return get_platform_supported_properties_with_platform_request_builder.GetPlatformSupportedPropertiesWithPlatformRequestBuilder(self.request_adapter, self.path_parameters, platform)
    
    def get_state(self,) -> get_state_request_builder.GetStateRequestBuilder:
        """
        Provides operations to call the getState method.
        Returns: get_state_request_builder.GetStateRequestBuilder
        """
        return get_state_request_builder.GetStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    async def post(self,body: Optional[device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter] = None, request_configuration: Optional[AssignmentFiltersRequestBuilderPostRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter]:
        """
        Create new navigation property to assignmentFilters for deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_post_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, device_and_app_management_assignment_filter.DeviceAndAppManagementAssignmentFilter, response_handler, error_mapping)
    
    @dataclass
    class AssignmentFiltersRequestBuilderGetQueryParameters():
        """
        The list of assignment filters
        """
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
    
    @dataclass
    class AssignmentFiltersRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AssignmentFiltersRequestBuilder.AssignmentFiltersRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AssignmentFiltersRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

