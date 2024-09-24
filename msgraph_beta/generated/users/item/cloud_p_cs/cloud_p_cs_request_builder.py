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
    from ....models.cloud_p_c import CloudPC
    from ....models.cloud_p_c_collection_response import CloudPCCollectionResponse
    from ....models.o_data_errors.o_data_error import ODataError
    from .bulk_resize.bulk_resize_request_builder import BulkResizeRequestBuilder
    from .count.count_request_builder import CountRequestBuilder
    from .get_provisioned_cloud_p_cs_with_group_id_with_service_plan_id.get_provisioned_cloud_p_cs_with_group_id_with_service_plan_id_request_builder import GetProvisionedCloudPCsWithGroupIdWithServicePlanIdRequestBuilder
    from .item.cloud_p_c_item_request_builder import CloudPCItemRequestBuilder
    from .validate_bulk_resize.validate_bulk_resize_request_builder import ValidateBulkResizeRequestBuilder

class CloudPCsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the cloudPCs property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new CloudPCsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/cloudPCs{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_cloud_p_c_id(self,cloud_p_c_id: str) -> CloudPCItemRequestBuilder:
        """
        Provides operations to manage the cloudPCs property of the microsoft.graph.user entity.
        param cloud_p_c_id: The unique identifier of cloudPC
        Returns: CloudPCItemRequestBuilder
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
        if cloud_p_c_id is None:
            raise TypeError("cloud_p_c_id cannot be null.")
        from .item.cloud_p_c_item_request_builder import CloudPCItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPC%2Did"] = cloud_p_c_id
        return CloudPCItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CloudPCsRequestBuilderGetQueryParameters]] = None) -> Optional[CloudPCCollectionResponse]:
        """
        Get cloudPCs from users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudPCCollectionResponse]
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.cloud_p_c_collection_response import CloudPCCollectionResponse

        return await self.request_adapter.send_async(request_info, CloudPCCollectionResponse, error_mapping)
    
    def get_provisioned_cloud_p_cs_with_group_id_with_service_plan_id(self,group_id: str, service_plan_id: str) -> GetProvisionedCloudPCsWithGroupIdWithServicePlanIdRequestBuilder:
        """
        Provides operations to call the getProvisionedCloudPCs method.
        param group_id: Usage: groupId='{groupId}'
        param service_plan_id: Usage: servicePlanId='{servicePlanId}'
        Returns: GetProvisionedCloudPCsWithGroupIdWithServicePlanIdRequestBuilder
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
        if group_id is None:
            raise TypeError("group_id cannot be null.")
        if service_plan_id is None:
            raise TypeError("service_plan_id cannot be null.")
        from .get_provisioned_cloud_p_cs_with_group_id_with_service_plan_id.get_provisioned_cloud_p_cs_with_group_id_with_service_plan_id_request_builder import GetProvisionedCloudPCsWithGroupIdWithServicePlanIdRequestBuilder

        return GetProvisionedCloudPCsWithGroupIdWithServicePlanIdRequestBuilder(self.request_adapter, self.path_parameters, group_id, service_plan_id)
    
    async def post(self,body: CloudPC, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CloudPC]:
        """
        Create new navigation property to cloudPCs for users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudPC]
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.cloud_p_c import CloudPC

        return await self.request_adapter.send_async(request_info, CloudPC, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CloudPCsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get cloudPCs from users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CloudPC, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create new navigation property to cloudPCs for users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> CloudPCsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CloudPCsRequestBuilder
        """
        warn(" as of 2024-07/PrivatePreview:copilotExportAPI", DeprecationWarning)
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CloudPCsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bulk_resize(self) -> BulkResizeRequestBuilder:
        """
        Provides operations to call the bulkResize method.
        """
        from .bulk_resize.bulk_resize_request_builder import BulkResizeRequestBuilder

        return BulkResizeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def validate_bulk_resize(self) -> ValidateBulkResizeRequestBuilder:
        """
        Provides operations to call the validateBulkResize method.
        """
        from .validate_bulk_resize.validate_bulk_resize_request_builder import ValidateBulkResizeRequestBuilder

        return ValidateBulkResizeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CloudPCsRequestBuilderGetQueryParameters():
        """
        Get cloudPCs from users
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
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

    
    @dataclass
    class CloudPCsRequestBuilderGetRequestConfiguration(RequestConfiguration[CloudPCsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CloudPCsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

