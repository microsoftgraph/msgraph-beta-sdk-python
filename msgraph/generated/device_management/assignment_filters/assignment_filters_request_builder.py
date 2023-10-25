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
    from ...models.device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter
    from ...models.device_and_app_management_assignment_filter_collection_response import DeviceAndAppManagementAssignmentFilterCollectionResponse
    from ...models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .enable.enable_request_builder import EnableRequestBuilder
    from .get_platform_supported_properties_with_platform.get_platform_supported_properties_with_platform_request_builder import GetPlatformSupportedPropertiesWithPlatformRequestBuilder
    from .get_state.get_state_request_builder import GetStateRequestBuilder
    from .item.device_and_app_management_assignment_filter_item_request_builder import DeviceAndAppManagementAssignmentFilterItemRequestBuilder
    from .validate_filter.validate_filter_request_builder import ValidateFilterRequestBuilder

class AssignmentFiltersRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the assignmentFilters property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AssignmentFiltersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/assignmentFilters{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}", path_parameters)
    
    def by_device_and_app_management_assignment_filter_id(self,device_and_app_management_assignment_filter_id: str) -> DeviceAndAppManagementAssignmentFilterItemRequestBuilder:
        """
        Provides operations to manage the assignmentFilters property of the microsoft.graph.deviceManagement entity.
        param device_and_app_management_assignment_filter_id: The unique identifier of deviceAndAppManagementAssignmentFilter
        Returns: DeviceAndAppManagementAssignmentFilterItemRequestBuilder
        """
        if not device_and_app_management_assignment_filter_id:
            raise TypeError("device_and_app_management_assignment_filter_id cannot be null.")
        from .item.device_and_app_management_assignment_filter_item_request_builder import DeviceAndAppManagementAssignmentFilterItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceAndAppManagementAssignmentFilter%2Did"] = device_and_app_management_assignment_filter_id
        return DeviceAndAppManagementAssignmentFilterItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[AssignmentFiltersRequestBuilderGetRequestConfiguration] = None) -> Optional[DeviceAndAppManagementAssignmentFilterCollectionResponse]:
        """
        The list of assignment filters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceAndAppManagementAssignmentFilterCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.device_and_app_management_assignment_filter_collection_response import DeviceAndAppManagementAssignmentFilterCollectionResponse

        return await self.request_adapter.send_async(request_info, DeviceAndAppManagementAssignmentFilterCollectionResponse, error_mapping)
    
    def get_platform_supported_properties_with_platform(self,platform: Optional[str] = None) -> GetPlatformSupportedPropertiesWithPlatformRequestBuilder:
        """
        Provides operations to call the getPlatformSupportedProperties method.
        param platform: Usage: platform='{platform}'
        Returns: GetPlatformSupportedPropertiesWithPlatformRequestBuilder
        """
        if not platform:
            raise TypeError("platform cannot be null.")
        from .get_platform_supported_properties_with_platform.get_platform_supported_properties_with_platform_request_builder import GetPlatformSupportedPropertiesWithPlatformRequestBuilder

        return GetPlatformSupportedPropertiesWithPlatformRequestBuilder(self.request_adapter, self.path_parameters, platform)
    
    async def post(self,body: Optional[DeviceAndAppManagementAssignmentFilter] = None, request_configuration: Optional[AssignmentFiltersRequestBuilderPostRequestConfiguration] = None) -> Optional[DeviceAndAppManagementAssignmentFilter]:
        """
        Create new navigation property to assignmentFilters for deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceAndAppManagementAssignmentFilter]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter

        return await self.request_adapter.send_async(request_info, DeviceAndAppManagementAssignmentFilter, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[AssignmentFiltersRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The list of assignment filters
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
    
    def to_post_request_information(self,body: Optional[DeviceAndAppManagementAssignmentFilter] = None, request_configuration: Optional[AssignmentFiltersRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to assignmentFilters for deviceManagement
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
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> AssignmentFiltersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AssignmentFiltersRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AssignmentFiltersRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enable(self) -> EnableRequestBuilder:
        """
        Provides operations to call the enable method.
        """
        from .enable.enable_request_builder import EnableRequestBuilder

        return EnableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_state(self) -> GetStateRequestBuilder:
        """
        Provides operations to call the getState method.
        """
        from .get_state.get_state_request_builder import GetStateRequestBuilder

        return GetStateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def validate_filter(self) -> ValidateFilterRequestBuilder:
        """
        Provides operations to call the validateFilter method.
        """
        from .validate_filter.validate_filter_request_builder import ValidateFilterRequestBuilder

        return ValidateFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AssignmentFiltersRequestBuilderGetQueryParameters():
        """
        The list of assignment filters
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
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

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AssignmentFiltersRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AssignmentFiltersRequestBuilder.AssignmentFiltersRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AssignmentFiltersRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

